use food_delivery_db; 


-- SESSION 14 
CREATE TABLE ranked_songs (
  song_id INT PRIMARY KEY,
  artist VARCHAR(100),
  song_name VARCHAR(100),
  streams INT
);
INSERT INTO ranked_songs VALUES
(1, 'Arijit Singh', 'Tum Hi Ho', 5000000),
(2, 'Arijit Singh', 'Channa Mereya', 4500000),
(3, 'Arijit Singh', 'Kesariya', 6000000),
(4, 'Taylor Swift', 'Anti-Hero', 7000000),
(5, 'Taylor Swift', 'Shake It Off', 6500000),
(6, 'Taylor Swift', 'Love Story', 5500000);

CREATE TABLE ranked_movies (
  movie_id INT PRIMARY KEY,
  genre VARCHAR(50),
  movie_name VARCHAR(100),
  rating DECIMAL(2,1)
);
INSERT INTO ranked_movies VALUES
(1, 'Action', 'Pathaan', 4.5),
(2, 'Action', 'Jawan', 4.8),
(3, 'Action', 'Tiger 3', 4.0),
(4, 'Comedy', 'Fukrey 3', 3.8),
(5, 'Comedy', 'Dream Girl 2', 4.2),
(6, 'Comedy', 'Tu Jhoothi', 4.0);

CREATE TABLE Influencers_rank (
  id INT PRIMARY KEY,
  platform VARCHAR(50),
  name VARCHAR(100),
  followers INT
);
INSERT INTO Influencers_rank VALUES
(1, 'Instagram', 'Riya', 500000),
(2, 'Instagram', 'Karan', 800000),
(3, 'Instagram', 'Meera', 300000),
(4, 'Instagram', 'Raj', 900000),
(5, 'YouTube', 'Aarav', 1200000),
(6, 'YouTube', 'Neha', 700000),
(7, 'YouTube', 'Simran', 1500000),
(8, 'YouTube', 'Dev', 600000);

-- Task 1: ROW_NUMBER per user ordered by order date
SELECT order_id,
       user_id,
       order_amount,
       ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY order_id DESC) AS row_num
FROM app_orders;

-- Task 2: RANK songs by streams within each artist
SELECT song_id,
       artist,
       song_name,
       streams,
       RANK() OVER(PARTITION BY artist ORDER BY streams DESC) AS stream_rank
FROM ranked_songs;

-- Task 3: DENSE_RANK movies by rating within genre
SELECT movie_id,
       genre,
       movie_name,
       rating,
       DENSE_RANK() OVER(PARTITION BY genre ORDER BY rating DESC) AS rating_rank
FROM ranked_movies;

-- Task 4: Top 3 influencers per platform
SELECT id, platform, name, followers, row_num
FROM (
  SELECT id,
         platform,
         name,
         followers,
         ROW_NUMBER() OVER(PARTITION BY platform ORDER BY followers DESC) AS row_num
  FROM Influencers_rank
) ranked
WHERE row_num <= 3;
