use food_delivery_db;

-- SESSION 4 – LIKE / BETWEEN / IN
-- 1
SELECT * FROM restaurants
WHERE name LIKE '%Cafe';
-- 2
SELECT * FROM products
WHERE price BETWEEN 500 AND 1500;
-- 3
SELECT * FROM users
WHERE city IN ('Ahmedabad', 'Surat', 'Vadodara');
-- 4
SELECT * FROM songs
WHERE artist_name LIKE '%ar%';
