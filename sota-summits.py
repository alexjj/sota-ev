import requests
import json

# List of URLs
urls = [
    "https://api2.sota.org.uk/api/regions/GM/ES",
    "https://api2.sota.org.uk/api/regions/GM/CS",
    "https://api2.sota.org.uk/api/regions/GM/WS",
    "https://api2.sota.org.uk/api/regions/GM/SS"
]

# Function to retrieve and join data from the given URLs
def fetch_and_join_data(urls):
    all_data = []

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            summits = data["summits"]
            all_data.extend(summits)  # Join the results
        else:
            print(f"Failed to retrieve data from {url}")

    return all_data

# Fetch data from URLs and join the results
joined_data = fetch_and_join_data(urls)

# Save the joined data to a JSON file
file_path = 'gm_sota_data.json'
with open(file_path, 'w') as json_file:
    json.dump(joined_data, json_file, indent=4)

print(f"Data saved to {file_path}")
