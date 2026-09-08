import pandas as pd

# Task 1
ipl_df = pd.read_csv('pandas_ipl_matches.csv')
print(ipl_df.head(10))

# Task 2
mobile_expenses = pd.DataFrame({
    'Date': ['2026-08-01', '2026-08-03', '2026-08-05', '2026-08-08', '2026-08-12',
              '2026-08-15', '2026-08-18', '2026-08-21', '2026-08-25', '2026-08-29'],
    'Category': ['Recharge', 'App Purchase', 'Subscription', 'Recharge', 'Accessories',
                 'App Purchase', 'Subscription', 'Recharge', 'Repair', 'App Purchase'],
    'Amount': [299, 99, 149, 299, 450, 199, 149, 299, 899, 49],
})
mobile_expenses.to_excel('mobile_expenses.xlsx', index=False)
mobile_expenses_loaded = pd.read_excel('mobile_expenses.xlsx')
print(mobile_expenses_loaded.tail(3))

# Task 3
zomato_df = pd.DataFrame({
    'restaurant': ['Spice Villa', 'Curry House', 'Noodle Bar', 'Pizza Point', 'Sweet Tooth',
                    'Biryani Blues', 'Cafe Delight', 'Wok Express'],
    'city': ['Mumbai', 'Delhi', 'Bengaluru', 'Delhi', 'Mumbai', 'Hyderabad', 'Pune', 'Bengaluru'],
    'cuisine': ['North Indian', 'North Indian', 'Chinese', 'Fast Food', 'Desserts',
                'Biryani', 'Cafe', 'Chinese'],
    'rating': [4.2, 3.8, 4.5, 3.9, 4.6, 4.3, None, 4.0],
    'avg_cost_for_two': [600, 450, 500, 350, 300, 550, 250, 480],
})
print(zomato_df.describe())
print(zomato_df.info())
# Insight 1: 1 restaurant has a missing rating value (Cafe Delight)
# Insight 2: average rating across the listed restaurants is above 4.0

# Task 4
filtered_data = ipl_df.head(20)
filtered_data.to_csv('filtered_data.csv', index=False)

# Task 5
spotify_songs = pd.DataFrame({
    'song': ['Kesariya', 'Apna Bana Le', 'Tum Hi Ho', 'Naatu Naatu', 'Chaiyya Chaiyya'],
    'artist': ['Arijit Singh', 'Arijit Singh', 'Arijit Singh', 'Rahul Sipligunj', 'Sukhwinder Singh'],
    'streams_millions': [180, 95, 210, 130, 75],
})
spotify_songs.to_excel('spotify_songs.xlsx', index=False, sheet_name='Analysis2024')
