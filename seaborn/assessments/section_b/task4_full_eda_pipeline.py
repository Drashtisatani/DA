import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---- Generate (NumPy, seed=7) ----
np.random.seed(7)
n = 200

order_value = np.random.uniform(100, 800, n)
distance_km = np.random.uniform(1, 20, n)
delivery_time_mins = np.random.normal(30, 8, n)
rating = np.random.uniform(1.0, 5.0, n)
discount_pct = np.random.uniform(0, 30, n)

df = pd.DataFrame({
    'order_value': order_value,
    'distance_km': distance_km,
    'delivery_time_mins': delivery_time_mins,
    'rating': rating,
    'discount_pct': discount_pct,
})

# ---- Clean (Pandas): introduce 5% nulls into delivery_time_mins and rating, then fill with median ----
n_nulls = int(n * 0.05)

null_idx_time = np.random.choice(df.index, size=n_nulls, replace=False)
df.loc[null_idx_time, 'delivery_time_mins'] = np.nan

null_idx_rating = np.random.choice(df.index, size=n_nulls, replace=False)
df.loc[null_idx_rating, 'rating'] = np.nan

print(f"Nulls introduced -> delivery_time_mins: {df['delivery_time_mins'].isna().sum()}, "
      f"rating: {df['rating'].isna().sum()}")

df['delivery_time_mins'] = df['delivery_time_mins'].fillna(df['delivery_time_mins'].median())
df['rating'] = df['rating'].fillna(df['rating'].median())

print(f"Nulls after fill -> delivery_time_mins: {df['delivery_time_mins'].isna().sum()}, "
      f"rating: {df['rating'].isna().sum()}")

# ---- Enrich (Pandas): derived speed column + qcut speed band ----
df['delivery_speed_kmph'] = df['distance_km'] / (df['delivery_time_mins'] / 60)
df['speed_band'] = pd.qcut(df['delivery_speed_kmph'], q=3, labels=['Slow', 'Normal', 'Fast'])

print("\nSpeed band counts (should be ~equal-frequency):")
print(df['speed_band'].value_counts())

print("\nDataFrame preview after cleaning + enrichment:")
print(df.head(8).round(2).to_string(index=False))

# ---- Visualise (Seaborn) ----
numeric_cols = ['order_value', 'distance_km', 'delivery_time_mins', 'rating',
                 'discount_pct', 'delivery_speed_kmph']
corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(8, 6.5))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix - Food Delivery Numeric Features')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=150)
plt.close()
print("\nSaved chart: correlation_heatmap.png (DPI 150)")

g = sns.pairplot(
    df, vars=['order_value', 'distance_km', 'delivery_time_mins', 'rating'],
    hue='speed_band'
)
g.figure.suptitle('Pairplot: Order Value, Distance, Delivery Time, Rating (by Speed Band)', y=1.02)
g.savefig('pairplot.png', dpi=150)
plt.close('all')
print("Saved chart: pairplot.png (DPI 150)")
