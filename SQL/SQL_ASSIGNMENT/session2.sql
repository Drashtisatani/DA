use food_delivery_db; 

-- SESSION 2 – SELECT & FROM
-- 1
SELECT * FROM restaurants;
-- 2
SELECT name, rating FROM zomato_reviews;
-- 3
SELECT movie_name AS "Title",
       release_year AS "Year Released"
FROM movies;
-- 4
-- This query selects all product details
SELECT * FROM products;
