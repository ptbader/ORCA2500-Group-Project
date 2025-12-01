import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("BTS_2024_merged.csv")

# new df for time made up used in dist. plot 
df["time_made_up"] = df["DEP_DELAY"] - df["ARR_DELAY"]

#scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(df["DEP_DELAY"], df["ARR_DELAY"], alpha=0.4)
plt.title("Scatterplot: Departure Delay vs Arrival Delay")
plt.xlabel("Departure Delay (minutes)")
plt.ylabel("Arrival Delay (minutes)")
plt.grid(True)
plt.show()


# distribution plots
fig, axes = plt.subplots(3, 1, figsize=(10, 12))

#departure delay
axes[0].hist(df["DEP_DELAY"], bins=40, alpha=0.7)
axes[0].set_title("Distribution of Departure Delays")
axes[0].set_xlabel("Departure Delay (minutes)")
axes[0].set_ylabel("Frequency")

#arrival delay
axes[1].hist(df["ARR_DELAY"], bins=40, alpha=0.7)
axes[1].set_title("Distribution of Arrival Delays")
axes[1].set_xlabel("Arrival Delay (minutes)")
axes[1].set_ylabel("Frequency")

#TIme made up 
axes[2].hist(df["time_made_up"], bins=40, alpha=0.7)
axes[2].set_title("Distribution of Time Made Up (DEP_DELAY - ARR_DELAY)")
axes[2].set_xlabel("Time Made Up (minutes)")
axes[2].set_ylabel("Frequency")

plt.tight_layout()
plt.show()
