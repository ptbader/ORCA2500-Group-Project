import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("FinalSustainabilityDataset.csv")
IATA_FACTOR = 3.16  # kg CO₂ per kg fuel

df["Total_CO2_kg"] = df["TOTAL FUEL CONSUMPTION KG"] * IATA_FACTOR
df["CO2_per_pax"] = df["Total_CO2_kg"] / df["Total Pax"]

df = df.dropna(subset=["CO2_per_pax", "ARR_DELAY"])


#linreg 
x = df["CO2_per_pax"]
y = df["ARR_DELAY"]

#regression statistics
reg = stats.linregress(x, y)

slope = reg.slope
intercept = reg.intercept
r_value = reg.rvalue
p_value = reg.pvalue
std_err = reg.stderr

r_squared = r_value**2    # R² value
 #95% confidence interval setup
alpha = 0.05
df_n = len(x) - 2
t_crit = stats.t.ppf(1 - alpha/2, df_n)
slope_ci_lower = slope - t_crit * std_err
slope_ci_upper = slope + t_crit * std_err
intercept_stderr = reg.intercept_stderr
intercept_ci_lower = intercept - t_crit * intercept_stderr
intercept_ci_upper = intercept + t_crit * intercept_stderr

print("----- Regression Statistics -----")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R²: {r_squared}")
print(f"P-value (slope significance): {p_value}")
print(f"95% CI for slope: [{slope_ci_lower}, {slope_ci_upper}]")
print(f"95% CI for intercept: [{intercept_ci_lower}, {intercept_ci_upper}]")
print("----------------------------------")
# ---------------------------------------------

# regression line for plot
y_pred = slope * x + intercept

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.4, label="Flights")
plt.plot(x, y_pred, color="red", linewidth=2, label="Regression Line")

plt.title("CO₂ per Passenger vs Arrival Delay")
plt.xlabel("CO₂ per Passenger (kg CO₂)")
plt.ylabel("Arrival Delay (minutes)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#distrubution plot: CO2 per pax
plt.figure(figsize=(10, 6))
plt.hist(df["CO2_per_pax"], bins=40, alpha=0.75)
plt.title("Distribution of CO₂ per Passenger")
plt.xlabel("CO₂ per passenger (kg CO₂)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#distribution plot: arrival delays
plt.figure(figsize=(10, 6))
plt.hist(df["ARR_DELAY"], bins=40, alpha=0.75)
plt.title("Distribution of Arrival Delays")
plt.xlabel("Arrival Delay (minutes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

#distribution plot: time made up 
df["time_made_up"] = df["DEP_DELAY"] - df["ARR_DELAY"]

plt.figure(figsize=(10, 6))
plt.hist(df["time_made_up"], bins=40, alpha=0.75)
plt.title("Distribution of Time Made Up (DEP_DELAY - ARR_DELAY)")
plt.xlabel("Time Made Up (minutes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
