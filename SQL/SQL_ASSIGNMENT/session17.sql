use food_delivery_db; 

-- SESSION 17 

CREATE TABLE FoodOrders (
  order_id INT PRIMARY KEY,
  user_id INT,
  total_amount INT
);
INSERT INTO FoodOrders VALUES
(1, 1, 200),
(2, 2, 500),
(3, 3, 1500),
(4, 4, 850),
(5, 5, 100);

CREATE TABLE FlipkartProducts (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  price INT
);
INSERT INTO FlipkartProducts VALUES
(1, 'T-Shirt', 400),
(2, 'Shoes', 1200),
(3, 'Laptop', 55000),
(4, 'Watch', 2500),
(5, 'Bag', 800);

CREATE TABLE SpotifyTracks (
  track_id INT PRIMARY KEY,
  track_name VARCHAR(100),
  duration_sec INT
);
INSERT INTO SpotifyTracks VALUES
(1, 'Short Song', 120),
(2, 'Medium Track', 240),
(3, 'Long Instrumental', 400),
(4, 'Quick Beat', 90),
(5, 'Epic Mix', 350);


-- Task 1: Classify food orders as Small/Medium/Large
SELECT order_id,
       total_amount,
       CASE
         WHEN total_amount < 300 THEN 'Small'
         WHEN total_amount BETWEEN 300 AND 999 THEN 'Medium'
         ELSE 'Large'
       END AS order_size
FROM FoodOrders;

-- Task 2: Movie popularity based on rating
SELECT movie_name,
       rating,
       CASE
         WHEN rating >= 8 THEN 'Blockbuster'
         WHEN rating BETWEEN 5 AND 7.9 THEN 'Hit'
         ELSE 'Average'
       END AS popularity
FROM ranked_movies;

-- Task 3: Flipkart product price category
SELECT name,
       price,
       CASE
         WHEN price < 500 THEN 'Budget'
         WHEN price BETWEEN 500 AND 2000 THEN 'Standard'
         ELSE 'Premium'
       END AS price_category
FROM FlipkartProducts;

-- Task 4: Spotify track duration label
SELECT track_name,
       duration_sec,
       CASE
         WHEN duration_sec < 180 THEN 'Short'
         WHEN duration_sec BETWEEN 180 AND 300 THEN 'Medium'
         ELSE 'Long'
       END AS duration_label
FROM SpotifyTracks;



