import geopandas as gpd
from pathlib import Path

def main():
    while True:
        try:
            file_path = input("Enter the path of the Shapefile or GeoJSON: ")
            file_path = Path(file_path)
            if not file_path.exists() or not file_path.is_file():
                raise ValueError("Invalid file path")

            if file_path.suffix.lower() not in gpd.io.file.supported_drivers:
                raise ValueError("Unsupported file type")

            gdf = gpd.read_file(file_path)

            # Add centroid coordinates
            gdf['centroid_lon'] = gdf.geometry.centroid.x
            gdf['centroid_lat'] = gdf.geometry.centroid.y

            # Output path handling
            output_path = file_path.with_suffix('.csv')

            # Export to CSV, optionally preserving geometry
            preserve_geometry = input("Preserve geometry in output CSV? (y/n): ").lower() == 'y'
            if preserve_geometry:
                gdf.to_csv(output_path, index=False)
            else:
                gdf.drop(columns='geometry').to_csv(output_path, index=False)

            print(f"Data exported to {output_path}")
            break

        except (ValueError, gpd.errors.DriverError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
