import pandas as pd
import numpy as np

# Task 1
ipl_df = pd.read_csv('pandas_ipl_matches.csv')
print(ipl_df.head(5))

# Task 2
ipl_df = ipl_df[ipl_df['winner'].notna()]
ipl_df = ipl_df.reset_index(drop=True)
print(ipl_df.shape)

# Task 3
conditions = [
    ipl_df['win_by_runs'] > 0,
    ipl_df['win_by_wickets'] > 0,
]
choices = ['Runs', 'Wickets']
ipl_df['match_margin_type'] = np.select(conditions, choices, default='Tie/No Result')
print(ipl_df[['team1', 'team2', 'winner', 'win_by_runs', 'win_by_wickets', 'match_margin_type']].head(10))

# Task 4
team_home_cities = pd.DataFrame({
    'team': ['Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore',
              'Kolkata Knight Riders', 'Rajasthan Royals'],
    'home_city': ['Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Jaipur'],
})
ipl_df = ipl_df.merge(team_home_cities.rename(columns={'team': 'team1', 'home_city': 'team1_home_city'}),
                       on='team1', how='left')
ipl_df = ipl_df.merge(team_home_cities.rename(columns={'team': 'team2', 'home_city': 'team2_home_city'}),
                       on='team2', how='left')
print(ipl_df[['team1', 'team1_home_city', 'team2', 'team2_home_city']].head(10))

# Task 5
wins_per_season = ipl_df.pivot_table(index='winner', columns='season', values='id', aggfunc='count', fill_value=0)
max_wins_per_team_season = wins_per_season.stack()
top3 = max_wins_per_team_season.sort_values(ascending=False).head(3)
print(top3)
