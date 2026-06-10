use food_delivery_db; 

-- SESSION 11
CREATE TABLE flipkart_products (
  product_id INT PRIMARY KEY,
  name VARCHAR(100),
  price INT,
  category VARCHAR(50)
);
INSERT INTO flipkart_products VALUES
(1, 'iPhone 14', 70000, 'Mobile'),
(2, 'Samsung TV', 45000, 'Electronics'),
(3, 'Nike Shoes', 1200, 'Fashion'),
(4, 'Adidas Cap', 800, 'Fashion'),
(5, 'Dell Laptop', 55000, 'Electronics'),
(6, 'OnePlus 11', 60000, 'Mobile');

CREATE TABLE user_playlists (
  playlist_id INT PRIMARY KEY,
  user_id INT,
  playlist_name VARCHAR(100)
);
INSERT INTO user_playlists VALUES
(1, 1, 'Chill Mix'),
(2, 1, 'Work Mode'),
(3, 1, 'Party Hits'),
(4, 2, 'Morning Vibes'),
(5, 3, 'Workout');

CREATE TABLE food_app_orders (
  order_id INT PRIMARY KEY,
  user_id INT,
  total_amount INT
);
INSERT INTO food_app_orders VALUES
(1, 1, 500),
(2, 1, 1200),
(3, 2, 300),
(4, 2, 800),
(5, 3, 150),
(6, 3, 2000);

-- Task 1: Restaurants with rating above average
SELECT name, rating
FROM restaurants
WHERE rating > (SELECT AVG(rating) FROM restaurants);

-- Task 2: Each product with its category average price
SELECT name,
       price,
       (SELECT ROUND(AVG(f2.price), 2)
        FROM flipkart_products f2
        WHERE f2.category = f1.category) AS avg_category_price
FROM flipkart_products f1;

-- Task 3: Users with more playlists than average
SELECT u.username, p.playlist_count
FROM users u
JOIN (
  SELECT user_id, COUNT(*) AS playlist_count
  FROM user_playlists
  GROUP BY user_id
) p ON u.id = p.user_id
WHERE p.playlist_count > (
  SELECT AVG(playlist_count)
  FROM (
    SELECT COUNT(*) AS playlist_count
    FROM user_playlists
    GROUP BY user_id
  ) avg_table
);

-- Task 4: Users who placed order above average amount
SELECT DISTINCT user_id
FROM food_app_orders
WHERE total_amount > (SELECT AVG(total_amount) FROM food_app_orders);



