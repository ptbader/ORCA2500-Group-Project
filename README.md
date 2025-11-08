# ORCA2500-Group-Project


Foundations of Data Science Final Project Proposal
Sustainability and Punctuality across Airlines
Pierce Bader, Lera Bondarenko, Laura Robleto

Research Question: Do airlines that prioritize sustainability (lower CO₂ emissions per passenger) have better punctuality records?
Hypothesis: More carbon-efficient flights (lower CO₂ emissions per passenger for a given origin and destination) are more punctual (have fewer and smaller delays).
Rationale: Carbon efficiency is often correlated with more direct routes, fewer fuel-intensive detours, efficient aircraft utilization, and optimized flight planning. If an airline prioritizes these operational efficiencies, they may also reduce sources of delay (shorter flight time windows, less variability in routing), producing better on-time performance.
Objectives: 
Quantify the relationship between flight-level carbon emissions per passenger and punctuality (arrival delay in minutes; probability of arriving within 15 minutes).
Produce interpretable statistical estimates and visualizations to assess whether the hypothesized relationship holds and how strong it is.
Expected Outcomes: 
Descriptive statistics showing distributions of CO₂ per passenger, flight distance, scheduled flight time, and delays.
Estimates of the association between CO₂ per passenger and delay.
Subgroup analyses (short vs long haul, airlines, aircraft type).
Concrete interpretation and recommendations for airlines, regulators, and passengers.
Data Sets:
Primary flight data: U.S. flights dataset from the Bureau of Transportation Statistics (Data Set)
This dataset contains flight records for every U.S. flight between January 2022 and June 2025 for a total of 25.6 million rows. The information provided includes scheduled/actual departure and arrival times, origin/destination airport codes, carrier, aircraft type when available, and distance traveled.
→ Data suitability: This dataset provides a large sample size across carriers and airports and contains the information necessary to analyze both punctuality and matching to IATA CO₂ estimates (distance, aircraft type). The time span (2022–2025) allows us to test across seasons and years.
IATA Per Passenger CO2 emissions calculator 
The IATA Per-Passenger CO₂ emissions calculator/dataset is used to compute or estimate CO₂ emissions per passenger for each flight. IATA’s calculation methodology can be found here: IATA RECOMMENDED PRACTICE -RP 1726 - Passenger CO2 Calculation Methodology

Analysis Plan: We will conduct a structured analysis combining flight punctuality data from the Bureau of Transportation Statistics (BTS) with CO₂-per-passenger estimates based on the IATA methodology. Our plan is divided into four stages:
Data preparation, which will consist of these steps: importing and cleaning BTS flight data (BTS data set) using PANDAS DataFrames and table operations; constructing key punctuality metrics that we can measure such as departure/arrival delay, on time departures, and time made up; estimating the CO2 emission per passenger using the data sets that we have. For this project we have decided to use the three airports in the NYC area (Newark, LaGuardia, and JFK) in order to minimize the influence of factors such as weather and location, as well as reduce the amount of data we need to clean and analyze.

Data integration, in which we’ll merge data sets to get relevant info for our code, as well as adding control variables such as weather, airport congestion, etc. (in addition to cleaning the data sets and ensuring that all variables have an assigned outcome)

Exploratory data analysis, where we’ll visualise the distributions of our metrics using scatterplots of CO2 vs Delay, as well as do subgroup analysis (comparing the short vs long haul flights, airlines, and aircraft type). 

Statistical modelling and interpretation where we will linearly and logistically build regression models for punctuality on carbon efficiency, for instance using metrics like “ontime” to see the on time arrival. As well, we might do a secondary, smaller analysis by training a simple machine (Random Forest Regressor) to see if there are further complexities in our data that may be causing biases (such as, CO2 efficiency impact on shorter flights vs longer flights, flights longer than 1500 miles making up miles regardless of CO2 efficiency, etc.).

Deliverables: we’ll have regression tables and visualisations, a heatmap comparing the average CO2 emission per passenger vs punctuality, and finally, policy interpretation of whether or not sustainable practices in flights delay customers’ flights.
