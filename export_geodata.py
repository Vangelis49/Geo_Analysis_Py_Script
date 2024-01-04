# Importing the GeoPandas library as 'gpd'. This library helps us work with geospatial data.
import geopandas as gpd

# Defining the main function of our script. This is where our code starts running.
def main():
    # Asking the user to enter the path of the Shapefile or GeoJSON file they want to work with.
    file_path = input("Enter the path of the Shapefile or GeoJSON: ")
    # Reading the file at the given path using GeoPandas, and storing the data in a GeoDataFrame named 'gdf'.
    gdf = gpd.read_file(file_path)

    # Add centroid coordinates

    # Calculating the longitude of the centroid (geographical center) for each geometry and storing it in a new column 'centroid_lon'.
    gdf['centroid_lon'] = gdf.geometry.centroid.x
    # Calculating the latitude of the centroid for each geometry and storing it in a new column 'centroid_lat'.
    gdf['centroid_lat'] = gdf.geometry.centroid.y

    # Export to CSV

    # Preparing the file path for our output CSV file by replacing the original file extension (.shp or .geojson) with '.csv'.
    output_path = file_path.replace('.shp', '.csv').replace('.geojson', '.csv')
    # Dropping the 'geometry' column (as it's not needed in CSV) and exporting the data to a CSV file.
    # The 'index=False' part means we won't include the row numbers in our CSV.
    gdf.drop(columns='geometry').to_csv(output_path, index=False)
    # Printing a message to the console to let us know the data export is complete, and showing the path of the output file.
    print(f"Data exported to {output_path}")

# This is a standard Python practice. It ensures that the main function is only called when the script is run directly (not when imported as a module).
if __name__ == "__main__":
    main()
