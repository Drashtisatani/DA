use food_delivery_db; 

-- SESSION 20 

CREATE TABLE ipl_matches (
  match_id INT PRIMARY KEY,
  team1 VARCHAR(100),
  team2 VARCHAR(100),
  winner VARCHAR(100),
  venue VARCHAR(100),
  match_date DATE
);
INSERT INTO ipl_matches VALUES
(1, 'Mumbai Indians', 'CSK', 'Mumbai Indians', 'Wankhede', '2023-04-05'),
(2, 'RCB', 'KKR', 'KKR', 'Chinnaswamy', '2023-04-06'),
(3, 'Mumbai Indians', 'RCB', 'Mumbai Indians', 'Wankhede', '2023-04-10'),
(4, 'CSK', 'KKR', 'CSK', 'Chepauk', '2023-04-12'),
(5, 'Mumbai Indians', 'KKR', 'KKR', 'Eden Gardens', '2023-04-15');

-- Task 1: Table already created above (ipl_matches)
-- To load from CSV in MySQL Workbench:
-- Server > Data Import > Import from CSV

-- Task 2: Select Mumbai Indians matches
SELECT * FROM ipl_matches
WHERE team1 = 'Mumbai Indians' OR team2 = 'Mumbai Indians';
-- Export: In MySQL Workbench, right click result > Export as CSV > mi_matches.csv

-- Task 3: Total matches per team (for Excel import)
SELECT team1 AS team, COUNT(*) AS matches_played
FROM ipl_matches
GROUP BY team1
UNION ALL
SELECT team2, COUNT(*)
FROM ipl_matches
GROUP BY team2;

-- Task 4: Wins per team (for Power BI chart)
SELECT winner, COUNT(*) AS total_wins
FROM ipl_matches
GROUP BY winner;

-- Task 5: Python code to insert mi_wins
/*
import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv('mi_matches.csv')

# Filter Mumbai Indians wins
mi_wins = df[df['winner'] == 'Mumbai Indians']

# Connect to MySQL
engine = create_engine('mysql+pymysql://root:password@localhost/food_delivery_db')

# Insert into new table
mi_wins.to_sql('mi_wins', con=engine, if_exists='replace', index=False)

print("Done! mi_wins table created.")
*/




