from arcgis.gis import GIS
from arcgis.mapping import WebMap

# Connect to ArcGIS Online account
gis = GIS(username="gisteam_TRCNZ")

# Define the query to search for web maps owned by "gisteam_TRCNZ"
query = "owner:gisteam_TRCNZ"

# Search for web maps based on the query
search_results = gis.content.search(query=query, item_type="Web Map", max_items=1000)

# Open the file at the desired location for writing
file_path = r"K:\CS\COMPUTER_TECHNOLOGY\GIS\Coady\web_maps_layers.txt"
with open(file_path, "w", encoding="utf-8") as file:
    # Iterate through the search results and write information about each web map to the file
    for web_map_item in search_results:
        # Create a WebMap object from the search result item
        web_map_obj = WebMap(web_map_item)
        
        # Write the title of the web map to the file
        file.write("Web Map Title: {}\n".format(web_map_item.title))
        
        # Write the URLs of layers in the web map to the file
        file.write("Layers:\n")
        for layer in web_map_obj.layers:
            if hasattr(layer, 'url'):
                file.write("{}\n".format(layer.url))
            elif hasattr(layer, 'layers'):
                # If it's a group layer, iterate through its sublayers
                for sublayer in layer.layers:
                    if hasattr(sublayer, 'url'):
                        file.write("{}\n".format(sublayer.url))
            else:
                file.write("Layer type: {}\n".format(layer.type))  # Handle differently based on layer type
    
        # Add a separator for readability
        file.write("="*50 + "\n")
