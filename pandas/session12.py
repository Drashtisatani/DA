import pandas as pd

# Task 1
ipl_matches_df = pd.read_csv('ipl_matches.csv')
team_runs = ipl_matches_df.groupby('winner')['win_by_runs'].sum().reset_index()
team_runs.columns = ['team', 'total_runs']
print(team_runs)

# Task 2
zomato_orders = pd.DataFrame({
    'city': ['Mumbai', 'Mumbai', 'Delhi', 'Delhi', 'Bengaluru', 'Bengaluru'],
    'restaurant': ['Spice Villa', 'Curry House', 'Noodle Bar', 'Pizza Point', 'Sweet Tooth', 'Biryani Blues'],
    'order_amount': [450, 620, 300, 780, 250, 540],
})
avg_by_restaurant_city = zomato_orders.groupby(['city', 'restaurant']).agg(avg_order_amount=('order_amount', 'mean'))
print(avg_by_restaurant_city)

# Task 3
flipkart_sales = pd.DataFrame({
    'category': ['Electronics', 'Electronics', 'Fashion', 'Fashion', 'Home', 'Home'],
    'region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'sales': [50000, 42000, 28000, 31000, 19000, 22000],
    'units_sold': [120, 95, 340, 290, 180, 210],
})
multi_agg = flipkart_sales.groupby(['category', 'region']).agg(
    total_sales=('sales', 'sum'),
    avg_units_sold=('units_sold', 'mean'),
)
print(multi_agg)

# Task 4
regional_revenue = pd.DataFrame({
    'region': ['North', 'South', 'East', 'West', 'North', 'South'],
    'revenue': [12000, 9500, 8700, 11200, 13500, 9800],
})
regional_summary = regional_revenue.groupby('region').agg(
    total_revenue=('revenue', 'sum'),
    max_revenue=('revenue', 'max'),
    min_revenue=('revenue', 'min'),
)
print(regional_summary)

# Task 5
spotify_streams = pd.DataFrame({
    'artist': ['Arijit Singh', 'Arijit Singh', 'Rahul Sipligunj', 'Sukhwinder Singh', 'Lata Mangeshkar'],
    'genre': ['Bollywood', 'Bollywood', 'Regional', 'Bollywood', 'Classical'],
    'streams': [1800000, 2100000, 1300000, 750000, 1100000],
})
genre_summary = spotify_streams.groupby('genre').agg(
    total_streams=('streams', 'sum'),
    avg_streams=('streams', 'mean'),
).sort_values('total_streams', ascending=False)
print(genre_summary)
