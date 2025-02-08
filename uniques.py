import pandas as pd

# Load activation data from CSV
df = pd.read_csv("activation_counts.csv")

# Convert string representation of list back to actual lists
df["summit"] = df["summit"].apply(lambda x: eval(x) if isinstance(x, str) else x)

# Count unique summits per date
df["unique_summits"] = df["summit"].apply(lambda x: len(set(x)))

# Sort by number of unique summits
df_sorted = df.sort_values(by="unique_summits", ascending=False)

# Display top 10 days with most unique summits
print(df_sorted[["date", "unique_summits"]].head(10))
