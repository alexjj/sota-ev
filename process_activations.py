import json
import csv
from collections import defaultdict
from datetime import datetime

# Input and output files
input_file = "summits_data.json"
output_file = "activations_per_day.csv"

# Load the JSON data
with open(input_file, "r") as f:
    data = json.load(f)

# Dictionary to count activations per day
activations_per_day = defaultdict(lambda: {"count": 0, "summits": set()})

# Process each summit and its activations
for summit, activations in data.items():
    if isinstance(activations, list):  # Ensure it's valid data
        for activation in activations:
            date = activation["activationDate"].split("T")[0]  # Extract YYYY-MM-DD
            activations_per_day[date]["count"] += 1
            activations_per_day[date]["summits"].add(summit)

# Convert summit sets to sorted lists for CSV storage
for date in activations_per_day:
    activations_per_day[date]["summits"] = sorted(activations_per_day[date]["summits"])

# Write to CSV
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Activations", "Summits"])
    for date, info in sorted(activations_per_day.items(), key=lambda x: x[0]):
        writer.writerow([date, info["count"], ", ".join(info["summits"])])

# Print top 10 days with most activations
top_10 = sorted(activations_per_day.items(), key=lambda x: x[1]["count"], reverse=True)[:10]
print("Top 10 days with most activations:")
for date, info in top_10:
    print(f"{date}: {info['count']} activations, Summits: {', '.join(info['summits'])}")

