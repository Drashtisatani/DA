use food_delivery_db;

-- SESSION 6 – AGGREGATE FUNCTIONS
-- 1
SELECT SUM(amount) AS total_spent
FROM food_orders;
-- 2
SELECT COUNT(song_id) AS total_songs
FROM spotify_playlists;
-- 3
SELECT ROUND(AVG(rating), 1) AS avg_rating
FROM bookmyshow_reviews;
-- 4
SELECT MIN(amount) AS min_amount,
       MAX(amount) AS max_amount
FROM paytm_transactions;
-- 5
SELECT user_id,
       COUNT(order_id) AS total_orders,
       ROUND(AVG(total_price), 2) AS avg_order,
       MAX(total_price) AS max_order
FROM myntra_orders
GROUP BY user_id;
