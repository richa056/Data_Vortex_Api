import pandas as pd
import numpy as np

np.random.seed(42)

# -------- Round-1 – Earth historical data (1990–2024) ---------
years = list(range(1990, 2025))  # 35 values

# Earth planet info (same physicial characteristics, different year)
round1_planet = pd.DataFrame({
    'planet_id': [1]*len(years),
    'planet_name': ['Earth']*len(years),
    'year': years,
    'distance_ly': [0]*len(years),
    'mass_earth': [1.0]*len(years),
    'gravity': [9.8]*len(years),
    'atmosphere': ['N2-O2']*len(years)
})
round1_planet.to_csv('data/round1_earth_planet.csv', index=False)

# Resources – varying slightly over time
round1_res = pd.DataFrame({
    'planet_id': [1]*len(years),
    'year': years,
    'water_percentage': np.round(np.random.uniform(68, 72, len(years)),2),
    'oxygen_percentage': np.round(np.random.uniform(19.5, 21, len(years)),2),
    'soil_fertility_index': np.round(np.random.uniform(0.7, 0.9, len(years)),2),
    'vegetation_index': np.round(np.random.uniform(0.70, 0.90, len(years)),2)
})
round1_res.to_csv('data/round1_earth_resources.csv', index=False)

round1_clim = pd.DataFrame({
    'planet_id': [1]*len(years),
    'year': years,
    'avg_temp_c': np.random.randint(13, 17, len(years)),
    'radiation_level': np.random.randint(180, 240, len(years)),
    'storm_frequency': np.random.randint(8, 15, len(years))
})
round1_clim.to_csv('data/round1_earth_climate.csv', index=False)

round1_soil = pd.DataFrame({
    'planet_id': [1]*len(years),
    'year': years,
    'soil_quality': np.round(np.random.uniform(0.75, 0.90, len(years)),2),
    'mineral_index': np.round(np.random.uniform(0.70, 0.90, len(years)),2),
    'pH_level': np.round(np.random.uniform(6.5, 8.0, len(years)),2)
})
round1_soil.to_csv('data/round1_earth_soil.csv', index=False)

# --------------  Round-2, Round-3 (same as before) -----------------------
# copy/paste your previous script for round2+round3 here
# (no changes needed to those sections)

print("✅ Round-1 Earth data regenerated with 35 years (1990–2024).")
