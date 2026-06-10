use food_delivery_db; 
-- SESSION 18 

CREATE TABLE restaurant_reviews (
  review_id INT PRIMARY KEY,
  restaurant_id INT,
  city VARCHAR(50),
  rating DECIMAL(2,1)
);
INSERT INTO restaurant_reviews VALUES
(1, 1, 'Ahmedabad', 4.5),
(2, 1, 'Ahmedabad', 4.3),
(3, 2, 'Surat', 3.8),
(4, 2, 'Surat', 4.2),
(5, 3, 'Mumbai', 4.7),
(6, 3, 'Mumbai', 4.9);

CREATE TABLE restaurant_info (
  restaurant_id INT PRIMARY KEY,
  name VARCHAR(100),
  city VARCHAR(50)
);
INSERT INTO restaurant_info VALUES
(1, 'Pizza Hub', 'Ahmedabad'),
(2, 'Spice Villa', 'Surat'),
(3, 'Biryani House', 'Mumbai');

CREATE TABLE swiggy_orders (
  order_id INT PRIMARY KEY,
  order_date DATE,
  amount INT
);
INSERT INTO swiggy_orders VALUES
(1, CURDATE(), 300),
(2, CURDATE(), 500),
(3, DATE_SUB(CURDATE(), INTERVAL 5 DAY), 700),
(4, DATE_SUB(CURDATE(), INTERVAL 10 DAY), 400),
(5, DATE_SUB(CURDATE(), INTERVAL 35 DAY), 600);

-- Task 1: Create view for top rated restaurants
CREATE VIEW TopRatedRestaurants AS
SELECT ri.name,
       ROUND(AVG(rr.rating), 2) AS avg_rating,
       COUNT(rr.review_id) AS total_reviews
FROM restaurant_info ri
JOIN restaurant_reviews rr ON ri.restaurant_id = rr.restaurant_id
GROUP BY ri.name
HAVING AVG(rr.rating) > 4.0;

SELECT * FROM TopRatedRestaurants;

-- Task 2: Update view to include city
CREATE OR REPLACE VIEW TopRatedRestaurants AS
SELECT ri.name,
       ri.city,
       ROUND(AVG(rr.rating), 2) AS avg_rating,
       COUNT(rr.review_id) AS total_reviews
FROM restaurant_info ri
JOIN restaurant_reviews rr ON ri.restaurant_id = rr.restaurant_id
GROUP BY ri.name, ri.city
HAVING AVG(rr.rating) > 4.0;

SELECT * FROM TopRatedRestaurants;

-- Task 3: Try updating avg_rating through view (will fail)
-- UPDATE TopRatedRestaurants SET avg_rating = 5.0 WHERE name = 'Pizza Hub';
-- Error: avg_rating is a computed column (AVG), views with
-- aggregate functions are not updatable in MySQL.

-- Task 4: Daily order summary view (last 30 days)
CREATE VIEW DailyOrderSummary AS
SELECT order_date,
       COUNT(order_id) AS total_orders,
       SUM(amount) AS total_revenue
FROM swiggy_orders
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
GROUP BY order_date;

SELECT * FROM DailyOrderSummary;

-- Task 5: 3 Good practices for analytics views
-- 1. Always use meaningful names
--    Example: CREATE VIEW FlipkartDailySales (not VIEW1)
-- 2. Always filter only needed data using WHERE
--    Example: WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
-- 3. Never SELECT * in views, always name columns explicitly
--    Example: SELECT order_date, SUM(amount) AS revenue






