import pandas as pd
import glob
import os

folder = r"C:\Users\laura\OneDrive\Desktop\ORCA Project\Months"
csv_files = glob.glob(os.path.join(folder, "*.csv"))

df_list = [pd.read_csv(f, low_memory=False) for f in csv_files]

df_merged = pd.concat(df_list, ignore_index=True)
df_merged.to_csv(r"C:\Users\laura\Downloads\BTS_2024_merged.csv", index=False)

print("Merged dataset saved.")
