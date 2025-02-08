import requests
import pandas as pd
import time

# Load summits from file
with open("summits.txt", "r") as file:
    summits = [line.strip() for line in file if line.strip()]

# Create an empty list to store activation data
activation_data = []

# Query API for each summit
for summit in summits:
    url = f"https://api-db2.sota.org.uk/api/activations/{summit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        activations = response.json()
        for activation in activations:
            activation_data.append({
                "summit": summit,
                "date": activation["activationDate"],
                "callsign": activation["ownCallsign"]  # Added callsign to data
            })
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {summit}: {e}")


# Create DataFrame
df = pd.DataFrame(activation_data)

# Count activations per day and collect summits
day_summits = df.groupby("date").agg({"summit": list, "callsign": "count"}).reset_index()
day_summits.rename(columns={"callsign": "activations"}, inplace=True)

# Sort by most activations
day_summits_sorted = day_summits.sort_values(by="activations", ascending=False)

# Save results to CSV
day_summits_sorted.to_csv("activation_counts.csv", index=False)

# Display the results
print(day_summits_sorted.head(10))
