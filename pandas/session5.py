import pandas as pd
import numpy as np

# Task 1
ipl_players = pd.DataFrame({
    'player_name': ['V Kohli', 'MS Dhoni', 'R Sharma', 'H Pandya', 'J Bumrah', 'KL Rahul'],
    'team': ['RCB', 'CSK', 'MI', 'MI', 'MI', 'LSG'],
    'age': [35, np.nan, 36, 30, np.nan, 31],
})
ipl_players.to_csv('ipl_players.csv', index=False)
ipl_players_loaded = pd.read_csv('ipl_players.csv')
print(ipl_players_loaded[ipl_players_loaded['age'].isnull()])

# Task 2
food_orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6],
    'customer_name': ['Aarav', 'Diya', 'Kabir', 'Meera', 'Rohan', 'Sara'],
    'delivery_rating': [4.5, np.nan, 3.8, np.nan, 4.2, 4.9],
})
cleaned_orders = food_orders.dropna(subset=['delivery_rating'])
print(cleaned_orders)

# Task 3
flipkart_reviews = pd.DataFrame({
    'product_id': [101, 102, 103, 104, 105],
    'rating': [4.5, np.nan, 3.8, np.nan, 4.2],
})
flipkart_reviews['rating'] = flipkart_reviews['rating'].fillna(flipkart_reviews['rating'].mean())
print(flipkart_reviews)

# Task 4
spotify_playlist = pd.DataFrame({
    'song': ['Kesariya', 'Apna Bana Le', 'Tum Hi Ho', 'Naatu Naatu', 'Lag Ja Gale'],
    'duration': [258, np.nan, 262, np.nan, 195],
})
spotify_playlist['duration'] = spotify_playlist['duration'].fillna(spotify_playlist['duration'].median())
spotify_playlist.to_csv('spotify_playlist_cleaned.csv', index=False)
print(spotify_playlist)

# Task 5
# Prompt used: "How do I replace missing values in a pandas DataFrame column with zero?"
# AI-suggested code: df['followers'] = df['followers'].fillna(0)
instagram_users = pd.DataFrame({
    'username': ['cooldude', 'foodiequeen', 'travelbug', 'artsyavi', 'gamerzone'],
    'followers': [1200, np.nan, 54000, np.nan, 32000],
})
instagram_users['followers'] = instagram_users['followers'].fillna(0)
print(instagram_users)
