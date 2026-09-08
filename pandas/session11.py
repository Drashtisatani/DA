import pandas as pd

# Task 1
jan_orders = pd.DataFrame({
    'order_id': [1, 2, 3],
    'item': ['Pizza', 'Burger', 'Biryani'],
    'amount': [350, 180, 420],
})
feb_orders = pd.DataFrame({
    'order_id': [4, 5, 6],
    'item': ['Momos', 'Pasta', 'Dosa'],
    'amount': [150, 280, 120],
})
all_orders = pd.concat([jan_orders, feb_orders], axis=0, ignore_index=True)
print(all_orders)

# Task 2
flipkart_products = pd.DataFrame({
    'product_id': [1, 2, 3],
    'name': ['Mouse', 'Keyboard', 'Monitor'],
})
product_ratings = pd.DataFrame({
    'rating': [4.3, 4.0, 4.6],
})
products_with_ratings = pd.concat([flipkart_products, product_ratings], axis=1)
print(products_with_ratings)

# Task 3
streams = pd.DataFrame({
    'user': ['UserA', 'UserA', 'UserB', 'UserB', 'UserC', 'UserC'],
    'day': ['Mon', 'Tue', 'Mon', 'Tue', 'Mon', 'Tue'],
    'songs_streamed': [12, 15, 8, 10, 20, 18],
})
streams_pivoted = streams.pivot(index='user', columns='day', values='songs_streamed')
print(streams_pivoted)

# Task 4
zomato_orders = pd.DataFrame({
    'restaurant': ['Spice Villa', 'Spice Villa', 'Curry House', 'Curry House'],
    'month': ['Jan', 'Feb', 'Jan', 'Feb'],
    'total_amount': [12000, 15000, 9000, 8500],
})
pivot_avg = pd.pivot_table(zomato_orders, index='restaurant', columns='month', values='total_amount', aggfunc='mean')
print(pivot_avg)

# Task 5
sales_jan = pd.DataFrame({'product': ['Kurta', 'Jeans', 'Saree'], 'sales': [4000, 3200, 5100]})
sales_feb = pd.DataFrame({'product': ['Kurta', 'Jeans', 'Saree'], 'sales': [4300, 2900, 5400]})
sales_mar = pd.DataFrame({'product': ['Kurta', 'Jeans', 'Saree'], 'sales': [3900, 3100, 6000]})
all_sales = pd.concat([sales_jan, sales_feb, sales_mar], ignore_index=True)
total_by_product = all_sales.groupby('product')['sales'].sum()
print(total_by_product)
