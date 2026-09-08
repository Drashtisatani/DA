import pandas as pd

# Task 1
movies = pd.DataFrame({
    'title': ['Pathaan', 'Jawan', 'Animal', 'Gadar 2', '12th Fail', 'RRR'],
    'genre': ['Action', 'Action', 'Drama', 'Action', 'Drama', 'Action'],
    'rating': [7.0, 7.1, 6.7, 7.5, 8.9, 7.9],
    'box_office': [543, 640, 550, 525, 71, 1200],
})
print(movies.loc[:, ['title', 'rating']])

# Task 2
flipkart_products = pd.DataFrame({
    'product_name': [f'Product_{i}' for i in range(1, 16)],
    'category': ['Electronics', 'Fashion', 'Home', 'Electronics', 'Fashion',
                 'Home', 'Electronics', 'Fashion', 'Home', 'Electronics',
                 'Fashion', 'Home', 'Electronics', 'Fashion', 'Home'],
    'price': [999, 499, 1200, 2999, 799, 350, 1499, 599, 899, 3499,
              299, 1100, 2499, 449, 749],
})
print(flipkart_products.iloc[0:10, :])

# Task 3
zomato_orders = pd.DataFrame({
    'restaurant': ['Spice Villa', 'Curry House', 'Noodle Bar', 'Pizza Point', 'Sweet Tooth',
                    'Biryani Blues', 'Cafe Delight', 'Wok Express'],
    'order_amount': [620, 350, 480, 720, 210, 890, 150, 540],
    'delivery_time': [32, 28, 25, 40, 20, 45, 15, 30],
})
print(zomato_orders[zomato_orders['order_amount'] > 500])

# Task 4
spotify_df = pd.DataFrame({
    'song': ['Kesariya', 'Apna Bana Le', 'Tum Hi Ho', 'Naatu Naatu', 'Chaiyya Chaiyya', 'Lag Ja Gale'],
    'artist': ['Arijit Singh', 'Arijit Singh', 'Arijit Singh', 'Rahul Sipligunj', 'Sukhwinder Singh', 'Lata Mangeshkar'],
    'streams': [1800000, 950000, 2100000, 1300000, 750000, 1100000],
    'duration': [258, 275, 262, 165, 290, 195],
})
print(spotify_df.query('streams > 1000000 and duration < 180'))

# Task 5
ipl_matches_df = pd.DataFrame({
    'team1': ['CSK', 'MI', 'RCB', 'KKR', 'GT', 'RR'],
    'team2': ['MI', 'RCB', 'KKR', 'GT', 'RR', 'CSK'],
    'winner': ['CSK', 'RCB', 'KKR', 'GT', 'RR', 'CSK'],
    'total_runs': [175, 340, 165, 210, 195, 245],
})
print(ipl_matches_df[(ipl_matches_df['total_runs'] >= 180) & (ipl_matches_df['total_runs'] <= 220)])
