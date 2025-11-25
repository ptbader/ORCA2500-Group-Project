import pandas as pd
import numpy as np

flights_path = r"C:\Users\laura\OneDrive\Desktop\ORCA Project\BTS_2024_merged.csv"
airport_lookup_path = r"C:\Users\laura\OneDrive\Desktop\ORCA Project\L_AIRPORT_ID.csv"
airline_lookup_path = r"C:\Users\laura\OneDrive\Desktop\ORCA Project\L_AIRLINE_ID.csv"

df = pd.read_csv(flights_path, low_memory=False)
airports = pd.read_csv(airport_lookup_path)
airlines = pd.read_csv(airline_lookup_path)

print("Loaded rows:", len(df))

#change airport destination codes to names
airports = airports.rename(columns={"Code": "DEST_AIRPORT_ID", "Description": "DEST_AIRPORT_NAME"})
df = df.merge(airports, how="left", on="DEST_AIRPORT_ID")

#change airline codes to names
airlines = airlines.rename(columns={"Code": "MKT_CARRIER_AIRLINE_ID", "Description": "AIRLINE_NAME"})
df = df.merge(airlines, how="left", on="MKT_CARRIER_AIRLINE_ID")

#filter origin airports for only NYC airports
nyc_airports = ["JFK", "LGA", "EWR"]
df = df[df["ORIGIN"].isin(nyc_airports)].copy()
print("Rows after NYC origin filter:", len(df))

#filter airport destinations for only major airports 
destination_airports = [
    "Chicago, IL: Chicago O'Hare International",
    "Miami, FL: Miami International",
    "Baltimore, MD: Baltimore/Washington International",
    "San Francisco, CA: San Francisco International",
    "Seattle, WA: Seattle/Tacoma International",
    "Los Angeles, CA: Los Angeles International",
    "Dallas/Fort Worth, TX: Dallas/Fort Worth International",
    "Denver, CO: Denver International",
    "Charlotte, NC: Charlotte Douglas International",
    "Boston, MA: Logan International",
    "Houston, TX: William P Hobby",
    "Atlanta, GA: Hartsfield-Jackson Atlanta International",
    "Phoenix, AZ: Phoenix Sky Harbor International",
    "Las Vegas, NV: Harry Reid International",
    "Orlando, FL: Orlando International",
    "Minneapolis, MN: Minneapolis/St Paul International",
    "Fort Lauderdale, FL: Fort Lauderdale-Hollywood International",
    "Detroit, MI: Detroit Metro Wayne County",
    "Philadelphia, PA: Philadelphia International",
    "Salt Lake City, UT: Salt Lake City International"
]

df = df[df["DEST_AIRPORT_NAME"].isin(destination_airports)].copy()
print("Rows after destination filter:", len(df))

#filtering for top airlines
df["AIRLINE_NAME"] = df["AIRLINE_NAME"].str.replace(r":\s[A-Z]*", "", regex=True)
commercial_airlines = [
    "American Airlines Inc.",
    "Delta Air Lines Inc.",
    "Southwest Airlines Co.",
    "United Air Lines Inc.",
    "Alaska Airlines Inc.",
    "Spirit Air Lines",
    "JetBlue Airways",
    "Frontier Airlines Inc.",
    "Allegiant Air",
    "Hawaiian Airlines Inc.",
    "PSA Airlines Inc.",
    "Endeavor Air Inc.",
    "Piedmont Airlines",
    "Porter Airlines Inc. (PAI)"
    "Mesa Airlines Inc.",
    "Sun Country Airlines d/b/a MN Airlines",
    "Breeze Airways",
    "GoJet Airlines LLC",
    "Avelo Airlines",
    "SkyWest Airlines Inc.",
    "Republic Airways",
    "Envoy Air",
    "Horizon Air",
    "Air Wisconsin Airlines Corp",
    "Cape Air",
    "Silver Airways",
    "Southern Airways Express",
    "Boutique Air",
    "JSX Air",
    "Northern Pacific Airways",
    "Western Air Express",
    "Key Lime Air",
]

df = df[df["AIRLINE_NAME"].isin(commercial_airlines)].copy()
print("Rows after Airlines Filter:", len(df))

#remove weather delays
df = df[df["WEATHER_DELAY"] <= 0]
print("Rows after weather delays filter:", len(df))

#punctuality metrics
df["ONTIME_DEP"] = (df["DEP_DELAY"] <= 15).astype(int)
df["ONTIME_ARR"] = (df["ARR_DELAY"] <= 15).astype(int)
df["TIME_MADE_UP"] = df["DEP_DELAY"] - df["ARR_DELAY"]

output_path = r"C:\Users\laura\OneDrive\Desktop\ORCA Project\BTS_2024_NYCflights_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nSaved cleaned file to:", output_path)



