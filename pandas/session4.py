import pandas as pd

# Task 1
movies = pd.DataFrame({
    'title': ['Dangal', 'Baahubali 2', '3 Idiots', 'PK', 'Sultan', 'Bajrangi Bhaijaan'],
    'rating': [8.4, 8.2, 8.4, 8.1, 7.0, 8.1],
    'release_year': [2016, 2017, 2009, 2014, 2016, 2015],
})
print(movies.sort_values('rating', ascending=False))

# Task 2
ipl_teams = pd.DataFrame({
    'team': ['CSK', 'MI', 'RCB', 'KKR', 'GT'],
    'points': [18, 16, 14, 12, 20],
    'net_run_rate': [0.652, 0.398, 0.112, -0.221, 0.809],
})
print(ipl_teams.sort_index(ascending=False))

# Task 3
youtube_videos = pd.DataFrame({
    'video_title': ['Song Teaser', 'Movie Trailer', 'Comedy Sketch', 'Tech Review', 'Cooking Vlog'],
    'views': [1200000, 3400000, 890000, 560000, 210000],
    'likes': [95000, 210000, 62000, 38000, 15000],
})
youtube_videos = youtube_videos.sort_values('views', ascending=False)
youtube_videos = youtube_videos.reset_index(drop=True)
print(youtube_videos)

# Task 4
zomato_restaurants = pd.DataFrame({
    'restaurant': ['Curry House', 'Spice Villa', 'Noodle Bar', 'Pizza Point', 'Sweet Tooth'],
    'rating': [3.8, 4.2, 4.5, 3.9, 4.6],
})
new_order = [1] + [i for i in zomato_restaurants.index if i != 1]
print(zomato_restaurants.reindex(new_order))

# Task 5
flipkart_products = pd.DataFrame({
    'product_name': ['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E'],
    'price': [999, 1499, 599, 2999, 799],
    'discount': [10, 25, 5, 40, 15],
})
flipkart_products = flipkart_products.sort_values('discount', ascending=False)
flipkart_products = flipkart_products.reset_index(drop=True)
print(flipkart_products)
