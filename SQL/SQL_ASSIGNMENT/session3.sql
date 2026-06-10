use food_delivery_db;

-- SESSION 3 – WHERE
-- 1
SELECT * FROM restaurants
WHERE rating >= 4.5;
-- 2
SELECT * FROM movies
WHERE release_year > 2020 AND genre = 'Action';
-- 3
SELECT * FROM products
WHERE category <> 'Electronics' OR price < 500;
-- 4
SELECT * FROM users
WHERE NOT city = 'Ahmedabad' AND followers > 1000;

