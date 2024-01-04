import geopandas as gpd
from pathlib import Path

def main():
    file_path = input("Enter the path of the Shapefile or GeoJSON: ")
    file_path = Path(file_path)

    if not file_path.exists() or file_path.suffix.lower() not in ['.shp', '.geojson']:
        print("Invalid file path or unsupported file type.")
        return

    gdf = gpd.read_file(file_path)

    print("Please select an option:")
    print("1. Keep geometry column and don't reproject.")
    print("2. Drop geometry column and don't reproject.")
    print("3. Reproject and calculate accurate centroids.")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '3':
        epsg_code = input("Enter the EPSG code for reprojection: ")
        gdf = gdf.to_crs(epsg=int(epsg_code))
        gdf['centroid_lon'] = gdf.geometry.centroid.x
        gdf['centroid_lat'] = gdf.geometry.centroid.y

    output_path = file_path.with_suffix('.csv')

    if choice == '1':
        gdf.to_csv(output_path, index=False)
    elif choice in ['2', '3']:
        gdf.drop(columns='geometry').to_csv(output_path, index=False)

    print(f"Data exported to {output_path}")

if __name__ == "__main__":
    main()
