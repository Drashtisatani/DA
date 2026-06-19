################################## task 1 #################################################

import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    cuisine TEXT,
    rating REAL
)
""")

# Clear old data (optional)
cursor.execute("DELETE FROM restaurants")

# Insert sample data
cursor.execute("INSERT INTO restaurants (name, cuisine, rating) VALUES ('Spice Villa', 'Indian', 4.5)")
cursor.execute("INSERT INTO restaurants (name, cuisine, rating) VALUES ('Pizza Hub', 'Italian', 4.2)")
cursor.execute("INSERT INTO restaurants (name, cuisine, rating) VALUES ('Dragon Wok', 'Chinese', 4.1)")
cursor.execute("INSERT INTO restaurants (name, cuisine, rating) VALUES ('Burger Point', 'American', 3.9)")
cursor.execute("INSERT INTO restaurants (name, cuisine, rating) VALUES ('Tandoori House', 'Indian', 4.7)")

conn.commit()

# Load table into pandas DataFrame
query = "SELECT * FROM restaurants"
df = pd.read_sql(query, conn)

# Display first 5 rows
print(df.head())

# Close connection
conn.close()