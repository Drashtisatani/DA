import pandas as pd
import numpy as np
from scipy import stats

# Task 1
spotify_streams = pd.DataFrame({
    'song': ['Kesariya', 'Apna Bana Le', 'Kesariya', 'Naatu Naatu', 'Tum Hi Ho', 'Naatu Naatu'],
    'artist': ['Arijit Singh', 'Arijit Singh', 'Arijit Singh', 'Rahul Sipligunj', 'Arijit Singh', 'Rahul Sipligunj'],
    'streams': [1800000, 950000, 1800000, 1300000, 2100000, 1300000],
    'date': ['2026-08-01', '2026-08-01', '2026-08-01', '2026-08-01', '2026-08-01', '2026-08-01'],
})
spotify_streams_clean = spotify_streams.drop_duplicates(subset=['song'], keep='first')
print(spotify_streams_clean)

# Task 2
flipkart_reviews = pd.DataFrame({
    'product_id': [101, 102, 101, 103, 102, 104],
    'user_id': [1, 2, 1, 3, 2, 4],
    'rating': [5, 4, 5, 3, 4, 2],
    'review_text': ['Great', 'Good', 'Great', 'Okay', 'Good', 'Bad'],
})
before_count = flipkart_reviews.duplicated(subset=['product_id', 'user_id']).sum()
flipkart_reviews_clean = flipkart_reviews.drop_duplicates(subset=['product_id', 'user_id'])
after_count = flipkart_reviews_clean.duplicated(subset=['product_id', 'user_id']).sum()
print("Duplicates before:", before_count)
print("Duplicates after:", after_count)

# Task 3
zomato_orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'order_amount': [450, 380, 520, 410, 395, 3200, 460, 300],
})
Q1 = zomato_orders['order_amount'].quantile(0.25)
Q3 = zomato_orders['order_amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = zomato_orders[(zomato_orders['order_amount'] < lower_bound) | (zomato_orders['order_amount'] > upper_bound)]
print(outliers['order_id'].tolist())

# Task 4
ipl_tickets = pd.DataFrame({
    'date': pd.date_range('2026-04-01', periods=10),
    'tickets_sold': [12000, 13500, 11800, 42000, 12500, 13000, 12800, 11500, 13200, 12100],
})
ipl_tickets['z_score'] = stats.zscore(ipl_tickets['tickets_sold'])
print(ipl_tickets[ipl_tickets['z_score'].abs() > 2]['date'].tolist())

# Task 5
# Prompt used: "Write a pandas function using the Z-score method to find outlier
# transaction amounts in a DataFrame column."
def find_outliers_zscore(df, column, threshold=2):
    z_scores = stats.zscore(df[column])
    return df[abs(z_scores) > threshold]

paytm_transactions = pd.DataFrame({
    'transaction_id': range(1, 11),
    'amount': [500, 450, 620, 580, 490, 15000, 510, 470, 530, 495],
})
print(find_outliers_zscore(paytm_transactions, 'amount'))
