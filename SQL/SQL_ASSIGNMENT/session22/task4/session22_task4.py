import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("ipl.db")
cursor = conn.cursor()

# Create matches table
cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY,
    team1 TEXT
)
""")

# Insert sample data
cursor.execute("INSERT INTO matches (team1) VALUES ('Mumbai Indians')")
cursor.execute("INSERT INTO matches (team1) VALUES ('Chennai Super Kings')")
cursor.execute("INSERT INTO matches (team1) VALUES ('Mumbai Indians')")
cursor.execute("INSERT INTO matches (team1) VALUES ('Royal Challengers Bangalore')")
cursor.execute("INSERT INTO matches (team1) VALUES ('Chennai Super Kings')")
cursor.execute("INSERT INTO matches (team1) VALUES ('Mumbai Indians')")
cursor.execute("INSERT INTO matches (team1) VALUES ('Royal Challengers Bangalore')")
cursor.execute("INSERT INTO matches (team1) VALUES ('Mumbai Indians')")

conn.commit()

# Load data into DataFrame
matches_df = pd.read_sql("SELECT * FROM matches", conn)

print(matches_df)

# Count matches per team
team_count = matches_df.groupby("team1").size()

print("\nMatches Played By Each Team:")
print(team_count)

# Create bar chart
team_count.plot(kind="bar")

plt.title("Matches Played By Each Team")
plt.xlabel("Teams")
plt.ylabel("Number of Matches")

plt.show()

conn.close()