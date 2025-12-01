import pandas as pd
import numpy as np

flights_path = r"C:\Users\laura\OneDrive\Desktop\ORCA Project\BTS_2024_merged.csv"
airline_lookup_path = r"C:\Users\laura\OneDrive\Desktop\ORCA Project\L_AIRLINE_ID.csv"

df = pd.read_csv(flights_path, low_memory=False)
airlines = pd.read_csv(airline_lookup_path)

print("Loaded rows:", len(df))

#change airline codes to names
airlines = airlines.rename(columns={"Code": "MKT_CARRIER_AIRLINE_ID", "Description": "AIRLINE_NAME"})
df = df.merge(airlines, how="left", on="MKT_CARRIER_AIRLINE_ID")

#filter origin airports for only NYC airports
nyc_airports = ["JFK", "LGA", "EWR"]
df = df[df["ORIGIN"].isin(nyc_airports)].copy()
print("Rows after NYC origin filter:", len(df))

output_path = r"C:\Users\laura\OneDrive\Desktop\ORCA Project\BTS_2024_NYCflights_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nSaved cleaned file to:", output_path)



