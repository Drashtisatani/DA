use food_delivery_db; 

-- SESSION 13
CREATE TABLE app_orders (
  order_id INT PRIMARY KEY,
  user_id INT,
  order_amount INT,
  app_name VARCHAR(50)
);
INSERT INTO app_orders VALUES
(1, 1, 500, 'Zomato'),
(2, 1, 300, 'Swiggy'),
(3, 2, 800, 'Zomato'),
(4, 2, 200, 'Flipkart'),
(5, 3, 1200, 'Swiggy'),
(6, 3, 400, 'Zomato'),
(7, 4, 600, 'Flipkart'),
(8, 4, 900, 'Swiggy'),
(9, 5, 150, 'Zomato'),
(10, 5, 750, 'Flipkart');

CREATE TABLE song_playlist (
  song_id INT PRIMARY KEY,
  user_id INT,
  duration_sec INT
);
INSERT INTO song_playlist VALUES
(1, 1, 200),
(2, 1, 240),
(3, 2, 180),
(4, 2, 300),
(5, 3, 150),
(6, 3, 270);

CREATE TABLE MovieRatings (
  rating_id INT PRIMARY KEY,
  user_id INT,
  movie_name VARCHAR(100),
  rating DECIMAL(2,1)
);
INSERT INTO MovieRatings VALUES
(1, 1, 'Pathaan', 4.5),
(2, 2, 'Pathaan', 4.0),
(3, 3, 'Pathaan', 3.5),
(4, 1, 'Jawan', 5.0),
(5, 2, 'Jawan', 4.5),
(6, 3, 'Jawan', 4.0);

-- Task 1: Each order amount + total of all orders
SELECT order_id,
       user_id,
       order_amount,
       SUM(order_amount) OVER() AS total_all_orders
FROM app_orders;

-- Task 2: Each order + average order per user
SELECT order_id,
       user_id,
       order_amount,
       AVG(order_amount) OVER(PARTITION BY user_id) AS avg_user_order
FROM app_orders;

-- Task 3: Each song duration + total duration per user
SELECT song_id,
       user_id,
       duration_sec,
       SUM(duration_sec) OVER(PARTITION BY user_id) AS total_user_duration
FROM song_playlist;

-- Task 4: Each rating + movie avg rating + difference
SELECT rating_id,
       user_id,
       movie_name,
       rating,
       ROUND(AVG(rating) OVER(PARTITION BY movie_name), 2) AS avg_movie_rating,
       ROUND(rating - AVG(rating) OVER(PARTITION BY movie_name), 2) AS rating_difference
FROM MovieRatings;
