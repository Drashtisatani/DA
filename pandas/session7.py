import pandas as pd

# Task 1
flipkart_sales = pd.DataFrame({
    'ProductName': ['Wireless Mouse', 'Keyboard', 'Monitor', 'Webcam', 'USB Hub'],
    'Price': [599, 899, 8999, 1499, 499],
    'Qty': [3, 2, 1, 2, 4],
})
flipkart_sales['TotalValue'] = flipkart_sales['Price'] * flipkart_sales['Qty']
print(flipkart_sales)

# Task 2
food_items = pd.DataFrame({
    'Item': ['Pizza', 'Burger', 'Pasta', 'Sandwich'],
    'Price': [350, 180, 280, 150],
    'Qty': [1, 2, 1, 3],
})
food_items['DiscountedPrice'] = food_items['Price'].apply(lambda p: p * 0.9)
print(food_items)

# Task 3
def format_number(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)

instagram_posts = pd.DataFrame({
    'PostID': [1, 2, 3, 4],
    'Likes': [1500, 2500000, 850, 42000],
    'Comments': [120, 15000, 45, 980],
})
if hasattr(instagram_posts, 'applymap'):
    instagram_posts[['Likes', 'Comments']] = instagram_posts[['Likes', 'Comments']].applymap(format_number)
else:
    # applymap() was removed in pandas 3.0+; .map() on a DataFrame is its direct replacement
    instagram_posts[['Likes', 'Comments']] = instagram_posts[['Likes', 'Comments']].map(format_number)
print(instagram_posts)

# Task 4
zomato_orders = pd.DataFrame({
    'Restaurant': ['Spice Villa', 'Curry House', 'Noodle Bar', 'Pizza Point'],
    'Price': [320, 250, 180, 400],
    'Qty': [2, 1, 3, 1],
    'DeliveryCharge': [40, 30, 35, 45],
})
zomato_orders['FinalAmount'] = zomato_orders.apply(lambda row: (row['Price'] * row['Qty']) + row['DeliveryCharge'], axis=1)
print(zomato_orders)

# Task 5
# Prompt used: "Write pandas code to add a GST column to a DataFrame of Myntra
# orders, where GST = 5% of (Price * Qty)."
myntra_orders = pd.DataFrame({
    'Item': ['T-Shirt', 'Jeans', 'Jacket'],
    'Price': [799, 1499, 2999],
    'Qty': [2, 1, 1],
})
myntra_orders['GST'] = myntra_orders['Price'] * myntra_orders['Qty'] * 0.05
print(myntra_orders)
# What I learned from the AI's explanation:
# 1. GST here is computed on the pre-tax order value (Price * Qty), not on Price alone.
# 2. Vectorised column math (no apply/lambda needed) is enough since the formula
#    only combines existing columns arithmetically, unlike Task 4's row-wise logic.
