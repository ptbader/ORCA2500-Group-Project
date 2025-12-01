#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 08:06:16 2025

@author: valeriyabondarenko
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

#need help actually clarifying on how to run it without the file having to be mentioned in my stuff
flights = pd.read_csv("/Users/valeriyabondarenko/flights/BTS_2024_merged.csv")

nyc_airports = ["JFK", "LGA", "EWR"]
flights = flights[(flights["ORIGIN"].isin(nyc_airports))]

#removing cancelled flights
flights = flights[flights["CANCELLED"] == 0]

#indicators! 
#this ones for on time arrival delay <= 15 min
flights["on_time"] = (flights["ARR_DELAY"] <= 15).astype(int)

#this ones for long flights 1 for distance > 1500 miles
flights["long_haul"] = (flights["DISTANCE"] > 1500).astype(int)

#CO2 per passanger this is what im confused on lowkey idk 
flights["CO2_per_pas"] = np.random.uniform(40, 220, len(flights))


#### graphs! 

# boxplot first

plt.figure(figsize = (8,5))
sns.boxplot(data = flights, x = "MKT_CARRIER_AIRLINE_ID", y = "ARR_DELAY")
plt.title("Arrival Delay by Airline")
plt.xlabel("Airline")
plt.ylabel("Delay (minutes)")
plt.show()

# heatmap 

pivot = flights.pivot_table(values = "on_time",
                            index = "MKT_CARRIER_AIRLINE_ID",
                            columns = "long_haul",
                            aggfunc = "mean")

plt.figure(figsize = (6,4))
sns.heatmap(pivot, annot = True, cmap = "viridis", fmt = ".2f")
plt.title("On-time Rate by Airline and Flight Distance")
plt.ylabel("Airline")
plt.xlabel("Long Haul (1) / Short Haul (0)")
plt.show()










