use food_delivery_db;

-- SESSION 5 – DISTINCT / ORDER / LIMIT
-- 1
SELECT DISTINCT payment_method FROM transactions;
-- 2
SELECT DISTINCT city
FROM users
ORDER BY city ASC;
-- 3
SELECT * FROM bookings
ORDER BY booking_date DESC
LIMIT 5;
-- 4
SELECT name, sold_count
FROM products
ORDER BY sold_count DESC
LIMIT 10;



