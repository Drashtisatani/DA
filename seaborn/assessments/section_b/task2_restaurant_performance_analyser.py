
import numpy as np
import pandas as pd

np.random.seed(1)

n_rows = 50
restaurant_names = ['Spice Villa', 'Curry House', 'Noodle Bar', 'Pizza Point', 'Sweet Tooth']
cities = ['Mumbai', 'Delhi', 'Bengaluru']
cuisine_types = ['North Indian', 'Chinese', 'Fast Food']

df = pd.DataFrame({
    'restaurant_name': np.random.choice(restaurant_names, n_rows),
    'city': np.random.choice(cities, n_rows),
    'order_value': np.random.uniform(150, 900, n_rows).round(2),
    'delivery_time_mins': np.random.normal(30, 8, n_rows).clip(10, None).round(1),
    'rating': np.random.normal(4.0, 0.7, n_rows).clip(1.0, 5.0).round(1),
    'cuisine_type': np.random.choice(cuisine_types, n_rows),
})

# Single groupby().agg() method chain
summary = (
    df.groupby('restaurant_name')
      .agg(
          mean_order_value=('order_value', 'mean'),
          mean_delivery_time=('delivery_time_mins', 'mean'),
          mean_rating=('rating', 'mean'),
      )
)

# Filter: mean rating > 4.0 and mean delivery time < 35 minutes
filtered = summary[(summary['mean_rating'] > 4.0) & (summary['mean_delivery_time'] < 35)]

# Sort by mean order value descending, reset index
result = filtered.sort_values('mean_order_value', ascending=False).reset_index()

print("Full source dataset (first 10 rows):")
print(df.head(10).to_string(index=False))

print("\nGrouped summary (all restaurants):")
print(summary.round(2).to_string())

print("\nFiltered & ranked result (mean_rating > 4.0 AND mean_delivery_time < 35 min):")
print(result.round(2).to_string(index=False))
