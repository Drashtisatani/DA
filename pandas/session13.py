import pandas as pd

# Task 1
ipl_2023_batsmen = pd.DataFrame({
    'player_name': ['S Iyer', 'F du Plessis', 'V Kohli', 'Shubman Gill', 'Y Jaiswal',
                     'D Padikkal', 'D Conway', 'R Tewatia', 'S Samson', 'H Pandya',
                     'R Sharma', 'KL Rahul', 'MS Dhoni', 'AB de Villiers', 'D Warner'],
    'runs': [351, 730, 639, 890, 625, 373, 672, 218, 452, 351, 412, 500, 280, 0, 516],
    'matches': [12, 14, 14, 17, 14, 12, 12, 14, 13, 14, 14, 14, 15, 0, 12],
    'average': [35.1, 60.8, 46.5, 59.3, 44.6, 33.9, 61.1, 24.2, 34.8, 27.0, 32.6, 45.5, 23.3, 0, 46.9],
    'strike_rate': [128.5, 141.2, 122.8, 157.1, 155.6, 128.0, 138.0, 154.0, 135.2, 129.8, 130.2, 133.0, 104.0, 0, 155.0],
})
print(ipl_2023_batsmen.head(10))

# Task 2
runs = ipl_2023_batsmen['runs']
print("Mean:", runs.mean())
print("Median:", runs.median())
print("Mode:", runs.mode().tolist())
print("Min:", runs.min())
print("Max:", runs.max())

# Task 3
zomato_favs = pd.DataFrame({
    'name': ['Spice Villa', 'Curry House', 'Noodle Bar', 'Pizza Point', 'Sweet Tooth'],
    'rating': [4.2, 3.8, 4.5, 3.9, 4.6],
    'votes': [1200, 850, 2100, 630, 1450],
    'avg_cost': [600, 450, 500, 350, 300],
})
correlation = zomato_favs['rating'].corr(zomato_favs['votes'])
print("Correlation (rating vs votes):", correlation)

# Task 4
print(ipl_2023_batsmen.describe())
# Insight: 'AB de Villiers' has 0 matches/runs (did not play the season), which drags
# the mean average and strike rate down and shows up as the min=0 in describe().

# Task 5
# Prompt used: "Suggest two univariate or bivariate analyses for an IPL batsmen
# dataset with columns player_name, runs, matches, average, strike_rate."
# AI's two suggestions:
#   1. Bivariate: correlation between 'matches' played and 'runs' scored.
#   2. Univariate: distribution/spread (std dev) of 'strike_rate' across all batsmen.
# Implemented below: suggestion 1.
matches_runs_corr = ipl_2023_batsmen['matches'].corr(ipl_2023_batsmen['runs'])
print("Correlation (matches vs runs):", matches_runs_corr)
