use food_delivery_db;

-- SESSION 7 – GROUP BY
-- 1
SELECT user_id, COUNT(*) AS total_orders
FROM food_orders
GROUP BY user_id;
-- 2
SELECT payment_method, SUM(amount) AS total_spent
FROM transactions
GROUP BY payment_method;
-- 3
SELECT genre,
       SUM(box_office_collection) AS total_collection
FROM movies
GROUP BY genre
HAVING SUM(box_office_collection) > 1000000000;
-- 4
SELECT user_id,
       SUM(duration) AS total_duration
FROM playlists
GROUP BY user_id
HAVING SUM(duration) > 7200;