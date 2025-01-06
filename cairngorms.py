import folium
import json
import pandas as pd

with open("cairngorms.geojson", 'r') as f:
  cairngorms_geojson = json.load(f)

csv_file = "cairngorms_summits.csv"
summits_df = pd.read_csv(csv_file)

# Create a map centered on the Cairngorms
map_center = [57.07, -3.7]  # Approximate coordinates
my_map = folium.Map(location=map_center, zoom_start=8)

# Add the Cairngorms GeoJSON data to the map
folium.GeoJson(
    cairngorms_geojson,
    name="Cairngorms"
).add_to(my_map)

# Iterate through the summits in combined_df
for index, row in summits_df.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']

    tooltip = f"<b>{row['name']}</b><br>Points: {row['points']}"
    folium.Marker(
        location=[latitude, longitude],
        popup=row["name"],
        tooltip=tooltip,
        icon=folium.Icon(color="lightgreen" if row["points"] == 1 else "green" if row["points"] ==2 else "darkgreen" if row["points"] == 4 else "orange" if row["points"] == 6 else "darkred" if row["points"] == 8 else "red")
    ).add_to(my_map)

folium.LayerControl().add_to(my_map)

my_map.save('cairngorms.html')
