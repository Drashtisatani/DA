import pandas as pd

# Task 1
users = pd.DataFrame({
    'username': ['CoolDude', 'foodieQueen', 'TravelBug99', 'ArtsyAvi', 'GamerZone'],
})
users['username'] = users['username'].str.lower()
print(users)

# Task 2
songs = pd.Series(['Kesariya Remix', 'Apna Bana Le', 'Tum Hi Ho Remix', 'Naatu Naatu'])
songs_clean = songs.str.replace('Remix', '', regex=False).str.strip()
print(songs_clean)

# Task 3
zomato_reviews = pd.DataFrame({
    'review': [
        'The delivery was super fast!',
        'Food quality was excellent.',
        'Late delivery ruined the experience.',
        'Great taste but expensive.',
        'Delivery guy was very polite.',
    ]
})
print(zomato_reviews[zomato_reviews['review'].str.contains('delivery', case=False)])

# Task 4
flipkart_categories = pd.Series([
    'Electronics/Mobiles/Smartphones',
    'Home/Kitchen/Appliances',
    'Fashion/Men/Shirts',
    'Electronics/Laptops/Gaming',
])
main_category = flipkart_categories.str.split('/').str[0]
categories_df = pd.DataFrame({'full_category': flipkart_categories, 'main_category': main_category})
print(categories_df)

# Task 5
youtube_titles = pd.Series(['My First Vlog', 'Cooking Tutorial Ep 1', 'Tech Review 2026'])
youtube_titles_transformed = youtube_titles.str.upper().str.replace(' ', '_')
print(youtube_titles_transformed)
