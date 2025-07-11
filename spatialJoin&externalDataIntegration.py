# 🧩 GeoPandas Lesson 5: Merging with External Data (GDP)

# === Import required libraries ===
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# === Load the shapefile ===
path = r"C:\Users\pavan.rathod\OneDrive - VCTI\Desktop\GeoPandas\files\ne_110m_admin_0_countries.shp"
world = gpd.read_file(path)

# === Load the GDP CSV ===
gdp_path = r"C:\Users\pavan.rathod\OneDrive - VCTI\Desktop\GeoPandas\files\gdp.csv"
gdp_df = pd.read_csv(gdp_path)

# === Merge GeoDataFrame with GDP DataFrame on 'ADMIN' column ===
world_merged = world.merge(gdp_df, on='ADMIN', how='left')

# === Check for missing GDP entries ===
print(world_merged[['ADMIN', 'GDP']].isnull().sum())

# === Plot countries colored by GDP ===
fig, ax = plt.subplots(figsize=(14, 8))
world_merged.plot(column='GDP', cmap='YlGnBu', legend=True, edgecolor='black', ax=ax)
plt.title("Countries by GDP")
plt.axis("off")
plt.show()
