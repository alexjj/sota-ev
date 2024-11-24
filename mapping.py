import folium
import json
from folium.plugins import MarkerCluster

# Load JSON data
file_path = 'charge_points_data.json'

with open(file_path, 'r') as file:
    data = json.load(file)

# Create a map centered on Scotland
m = folium.Map(location=[56.4907, -4.2026], zoom_start=7)

# Create a MarkerCluster to group nearby markers efficiently
marker_cluster = MarkerCluster().add_to(m)

# Iterate through the features and plot each point
for feature in data['features']:
    coordinates = feature['geometry']['coordinates']
    properties = feature['properties']
    address = properties.get('address', {})
    connectors = properties.get('connectorGroups', [])
    tariff = properties.get('tariff', {})

    # Extract address details
    sitename = address.get('sitename', 'Unknown Site')
    street = address.get('street', '')
    city = address.get('city', '')
    postcode = address.get('postcode', '')

    # Extract tariff details
    tariff_amount = tariff.get('amount', 'N/A')
    tariff_currency = tariff.get('currency', 'N/A')
    tariff_description = tariff.get('description', 'No description available')

    # Extract connector details
    connector_info = ''
    for group in connectors:
        for connector in group['connectors']:
            connector_info += f"""
            <b>Connector ID:</b> {connector['connectorID']}<br>
            <b>Type:</b> {connector['connectorType']}<br>
            <b>Plug Type:</b> {connector['connectorPlugTypeName']}<br>
            <b>Max Charge Rate:</b> {connector['connectorMaxChargeRate']} kW<br><hr>
            """

    # Construct popup information
    popup_info = f"""
    <b>Site:</b> {sitename}<br>
    <b>Address:</b> {street}, {city}, {postcode}<br><br>
    <b>Connectors:</b><br>{connector_info}
    <b>Tariff:</b> {tariff_amount} {tariff_currency}<br>
    {tariff_description}
    """

    # Add markers to the map
    folium.Marker(
        location=[float(coordinates[0]), float(coordinates[1])],
        icon=folium.Icon(
            icon="charging-station",
            color="black",
            prefix="fa"
        ),
        popup=folium.Popup(popup_info, max_width=300)
    ).add_to(marker_cluster)


    # Add marker to the map
#    folium.Marker(
#        location=[float(coordinates[0]), float(coordinates[1])],  # Convert strings to floats
#        popup=folium.Popup(popup_info, max_width=300)
#    ).add_to(m)


## SOTA DATA
# Load JSON data
with open('gm_sota_data.json') as f:
    sota = json.load(f)

def get_color_by_activation_count(points):
    if points == 1:
        return "green"
    elif points == 2:
        return "darkgreen"
    elif points == 4:
        return "blue"
    elif points == 6:
        return "orange"
    elif points == 8:
        return "purple"
    else:
        return "red"

for summit in sota:
    latitude = summit["latitude"]
    longitude = summit["longitude"]
    name = summit["name"]
    summit_code = summit["summitCode"]
    activation_count = summit["activationCount"]
    points = summit['points']

    # Determine marker color based on activationCount
    marker_color = get_color_by_activation_count(points)

    # Create a popup with the summit's information
    popup_info = f"Name: {name}<br>Summit Code: {summit_code}<br>Points: {points}<br>Activation Count: {activation_count}"

    # Create the marker and add to the map
    folium.Marker(
        location=[latitude, longitude],
        icon=folium.Icon(
            icon="mountain",
            color=marker_color,
            prefix="fa"
            ),
        popup=folium.Popup(popup_info, max_width=300)
    ).add_to(m)


# Save or display the map
m.save('index.html')
print("Map saved as 'map.html'")
