import pandas as pd

# Task 1
users = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5],
    'username': ['aarav', 'diya', 'kabir', 'meera', 'rohan'],
    'city': ['Mumbai', 'Delhi', 'Bengaluru', 'Pune', 'Hyderabad'],
})
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106, 107],
    'user_id': [1, 2, 1, 3, 6, 2, 7],
    'order_amount': [450, 620, 300, 780, 250, 410, 590],
})
inner_join = pd.merge(users, orders, on='user_id', how='inner')
print(inner_join)

# Task 2
left_join = pd.merge(users, orders, on='user_id', how='left')
print(left_join)

# Task 3
restaurants = pd.DataFrame({
    'restaurant_id': [1, 2, 3, 4],
    'name': ['Spice Villa', 'Curry House', 'Noodle Bar', 'Pizza Point'],
    'city': ['Mumbai', 'Delhi', 'Bengaluru', 'Delhi'],
})
zomato_reviews = pd.DataFrame({
    'review_id': [201, 202, 203, 204],
    'restaurant_id': [1, 2, 5, 3],
    'rating': [4.2, 3.8, 4.0, 4.5],
    'reviewer_city': ['Mumbai', 'Delhi', 'Chennai', 'Bengaluru'],
})
outer_join = pd.merge(restaurants, zomato_reviews, on='restaurant_id', how='outer')
print(outer_join)

# Task 4
playlists = pd.DataFrame({
    'playlist_id': [1, 2, 3, 4],
    'user_id': [1, 2, 3, 1],
    'genre': ['Pop', 'Rock', 'Hip-Hop', 'Classical'],
    'city': ['Mumbai', 'Delhi', 'Bengaluru', 'Delhi'],
})
user_profiles = pd.DataFrame({
    'user_id': [1, 2, 3],
    'username': ['aarav', 'diya', 'kabir'],
    'city': ['Mumbai', 'Delhi', 'Bengaluru'],
})
matched = pd.merge(playlists, user_profiles, on=['user_id', 'city'])
print(matched)

# Task 5
# Prompt used: "Write pandas code to merge two DataFrames: Flipkart products
# (product_id, name, category) and product ratings (rating_id, product_id, rating)."
flipkart_products = pd.DataFrame({
    'product_id': [1, 2, 3, 4],
    'name': ['Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics'],
})
product_ratings = pd.DataFrame({
    'rating_id': [501, 502, 503, 504],
    'product_id': [1, 2, 5, 3],
    'rating': [4.3, 4.0, 3.9, 4.6],
})
right_join = pd.merge(flipkart_products, product_ratings, on='product_id', how='right')
print(right_join)
