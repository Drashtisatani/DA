import pandas as pd

# Task 1
date_strings = pd.Series(['01-04-2026', '15-06-2026', '23-08-2026', '05-11-2026', '30-12-2026'])
dates = pd.to_datetime(date_strings, format='%d-%m-%Y')
print(dates)

# Task 2
movies = pd.DataFrame({
    'title': ['Pathaan', 'Jawan', 'Animal', 'Gadar 2'],
    'release_date': ['2023-01-25', '2023-09-07', '2023-12-01', '2023-08-11'],
})
movies['release_date'] = pd.to_datetime(movies['release_date'])
movies['year'] = movies['release_date'].dt.year
movies['month'] = movies['release_date'].dt.month
movies['day'] = movies['release_date'].dt.day
print(movies)

# Task 3
next_7_days = pd.date_range(start=pd.Timestamp.today().normalize(), periods=7)
print(next_7_days)

# Task 4
zomato_gold = pd.DataFrame({
    'user_id': [1, 2, 3, 4],
    'start_date': ['2026-01-15', '2025-11-01', '2026-06-20', '2024-08-10'],
})
zomato_gold['start_date'] = pd.to_datetime(zomato_gold['start_date'])
today = pd.Timestamp.today().normalize()
zomato_gold['tenure_days'] = (today - zomato_gold['start_date']).dt.days
print(zomato_gold)
