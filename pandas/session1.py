import pandas as pd

# Task 1
fav_cricket_teams = pd.Series(['CSK', 'MI', 'RCB', 'KKR', 'GT'])
print(fav_cricket_teams)

# Task 2
food_orders = pd.DataFrame({
    'Item': ['Butter Chicken', 'Margherita Pizza', 'Veg Biryani'],
    'Restaurant': ['Curry House', 'Pizza Point', 'Spice Villa'],
    'Price': [320, 249, 180],
})
print(food_orders)

# Task 3
followers = pd.Series([1200, 54000, 780, 150000, 32000],
                       index=['influencer_A', 'influencer_B', 'influencer_C', 'influencer_D', 'influencer_E'])
print(followers)
print("Highest followers:", followers.idxmax(), "-", followers.max())
print("Lowest followers:", followers.idxmin(), "-", followers.min())

# Task 4
playlist = pd.DataFrame({
    'Song': ['Kesariya', 'Apna Bana Le', 'Tum Hi Ho', 'Naatu Naatu'],
    'Artist': ['Arijit Singh', 'Arijit Singh', 'Arijit Singh', 'Rahul Sipligunj'],
    'Duration': [4.28, 4.55, 4.22, 3.45],
})
print(playlist)
print(playlist[['Song', 'Duration']])
