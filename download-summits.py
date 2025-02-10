import requests
import json
import time

# Input and output files
input_file = "summits.txt"
output_file = "summits_data.json"
api_url = "https://api-db2.sota.org.uk/api/activations/{}"

# Read summit codes from file
with open(input_file, "r") as f:
    summits = [line.strip() for line in f if line.strip()]

# Dictionary to store all results
all_data = {}

# Loop through each summit and query API
for summit in summits:
    try:
        response = requests.get(api_url.format(summit))
        if response.status_code == 200:
            all_data[summit] = response.json()
        else:
            print(f"Error fetching {summit}: {response.status_code}")
            all_data[summit] = {"error": response.status_code}
    except Exception as e:
        print(f"Exception for {summit}: {e}")
        all_data[summit] = {"error": str(e)}

    time.sleep(1)  # Avoid excessive API requests

# Save results to JSON file
with open(output_file, "w") as f:
    json.dump(all_data, f, indent=2)

print(f"Saved results to {output_file}")



