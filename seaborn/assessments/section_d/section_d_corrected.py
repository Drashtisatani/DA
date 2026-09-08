"""
Section D - AI-Augmented Learning
STEP 2: TEST & DEBUG (WITHOUT AI) - Corrected version.

BUG FOUND: sns.pairplot(df, hue='cuisine_type') does not raise an error when
cuisine_type contains None/NaN values - it silently DROPS every row with a
null hue value from every panel of the plot, with no warning printed. Running
the AI's original script on this dataset (150 rows, ~10% forced-null
cuisine_type) confirmed this: with seed=5, 14 rows end up with a null
cuisine_type, and only 136 of 150 points are actually plotted (verified by
counting scatter offsets) - while the console output gives no indication
that those 14 rows vanished from the analysis.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(5)
n = 150

df = pd.DataFrame({
    'order_value': np.random.uniform(100, 800, n),
    'distance_km': np.random.uniform(1, 20, n),
    'delivery_time_mins': np.random.normal(30, 8, n),
    'rating': np.random.uniform(1, 5, n),
    'discount_pct': np.random.uniform(0, 30, n),
    'cuisine_type': np.random.choice(
        ['Fast Food', 'Indian', 'Chinese', None], n, p=[0.3, 0.3, 0.3, 0.1]
    ),
})

# --- FIX: report and handle nulls in the hue column BEFORE plotting ---
n_missing = df['cuisine_type'].isna().sum()
if n_missing > 0:
    print(f"Found {n_missing} row(s) with missing cuisine_type - "
          f"filling with 'Unknown' so no data is silently dropped from the plot.")
    df['cuisine_type'] = df['cuisine_type'].fillna('Unknown')

# Pairplot coloured by cuisine_type (now includes every row)
pairplot = sns.pairplot(df, hue='cuisine_type')
pairplot.savefig('ai_pairplot_output_corrected.png', dpi=150)

# Correlation heatmap - DPI 200 as the task requires, descriptive filename
numeric_df = df.select_dtypes(include='number')
corr = numeric_df.corr()

plt.figure(figsize=(7, 6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap - Food Delivery Numeric Features')
plt.tight_layout()
plt.savefig('food_delivery_correlation_heatmap_200dpi.png', dpi=200)
plt.close('all')

print("Done - pairplot and heatmap saved (all rows retained, correct DPI).")
