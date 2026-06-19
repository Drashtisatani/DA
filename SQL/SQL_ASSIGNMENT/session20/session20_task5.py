import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv(
    "/Users/drashtisatani/Desktop/DA_mysql_assignment/session20/mi_matches_task2.csv"
)

# Filter matches won by Mumbai Indians
mi_wins = df[df["winner"] == "Mumbai Indians"]

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:Drashti%402003@127.0.0.1/food_delivery_db"
)

# Insert into MySQL table
mi_wins.to_sql(
    "mi_wins",
    con=engine,
    if_exists="replace",
    index=False
)

print("Done! mi_wins table created.")