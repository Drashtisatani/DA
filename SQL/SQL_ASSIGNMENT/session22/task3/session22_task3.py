import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("zomato.db")
cursor = conn.cursor()

# Create orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    food_item TEXT
)
""")

# Insert sample data
cursor.execute("INSERT INTO orders (food_item) VALUES ('Pizza')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Burger')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Pizza')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Biryani')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Pizza')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Burger')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Biryani')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Pizza')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Burger')")
cursor.execute("INSERT INTO orders (food_item) VALUES ('Pizza')")

conn.commit()

# Load last 100 orders
query = """
SELECT *
FROM orders
ORDER BY order_id DESC
LIMIT 100
"""

orders_df = pd.read_sql(query, conn)

print("Orders Table:")
print(orders_df)

# Find top 3 most ordered food items
top3 = orders_df['food_item'].value_counts().head(3)

print("\nTop 3 Most Ordered Food Items:")
print(top3)

# Close connection
conn.close()