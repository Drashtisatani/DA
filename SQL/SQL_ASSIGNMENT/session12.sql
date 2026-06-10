use food_delivery_db; 


-- SESSION 12

CREATE TABLE SpotifyArtists (
  artist_id INT PRIMARY KEY,
  name VARCHAR(100),
  followers INT
);
INSERT INTO SpotifyArtists VALUES
(1, 'Arijit Singh', 5000000),
(2, 'Taylor Swift', 8000000),
(3, 'Ed Sheeran', 7000000),
(4, 'Shreya Ghoshal', 3000000),
(5, 'The Weeknd', 6000000);

CREATE TABLE FlipkartOrders (
  order_id INT PRIMARY KEY,
  user_id INT,
  order_date DATE,
  total_amount INT
);
INSERT INTO FlipkartOrders VALUES
(1, 1, '2023-01-15', 1000),
(2, 2, '2023-01-20', 2000),
(3, 3, '2023-02-10', 1500),
(4, 1, '2023-02-25', 3000),
(5, 2, '2023-03-05', 500),
(6, 3, '2023-03-18', 2500);

CREATE TABLE ZomatoRestaurants (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  city VARCHAR(50),
  rating DECIMAL(2,1)
);
INSERT INTO ZomatoRestaurants VALUES
(1, 'Pizza Hub', 'Ahmedabad', 4.5),
(2, 'Burger King', 'Ahmedabad', 4.2),
(3, 'Spice Villa', 'Surat', 4.8),
(4, 'Cafe Mocha', 'Surat', 3.9),
(5, 'Dosa Place', 'Mumbai', 4.1),
(6, 'Biryani House', 'Mumbai', 3.7);

CREATE TABLE IPLMatches (
  match_id INT PRIMARY KEY,
  team VARCHAR(100),
  runs INT,
  match_year INT
);
INSERT INTO IPLMatches VALUES
(1, 'Mumbai Indians', 180, 2023),
(2, 'Chennai Super Kings', 175, 2023),
(3, 'Mumbai Indians', 210, 2023),
(4, 'RCB', 160, 2023),
(5, 'Mumbai Indians', 195, 2023),
(6, 'Chennai Super Kings', 190, 2023),
(7, 'RCB', 155, 2023),
(8, 'Mumbai Indians', 220, 2023),
(9, 'Chennai Super Kings', 200, 2023),
(10, 'Mumbai Indians', 185, 2023),
(11, 'RCB', 170, 2023),
(12, 'Mumbai Indians', 205, 2023);

-- Task 1: Top 3 most followed artists
WITH TopArtists AS (
  SELECT artist_id, name, followers
  FROM SpotifyArtists
  ORDER BY followers DESC
  LIMIT 3
)
SELECT * FROM TopArtists;

-- Task 2: Month with highest total sales in 2023
WITH MonthlyTotals AS (
  SELECT DATE_FORMAT(order_date, '%m') AS month,
         SUM(total_amount) AS total_sales
  FROM FlipkartOrders
  WHERE YEAR(order_date) = 2023
  GROUP BY DATE_FORMAT(order_date, '%m')
)
SELECT * FROM MonthlyTotals
ORDER BY total_sales DESC
LIMIT 1;

-- Task 3: Recursive CTE - next 7 days
WITH RECURSIVE CalendarDays AS (
  SELECT CURDATE() AS day_date
  UNION ALL
  SELECT DATE_ADD(day_date, INTERVAL 1 DAY)
  FROM CalendarDays
  WHERE day_date < DATE_ADD(CURDATE(), INTERVAL 6 DAY)
)
SELECT * FROM CalendarDays;

-- Task 4: Restaurants in cities with avg rating above 4.0
WITH CityAvgRating AS (
  SELECT city, AVG(rating) AS avg_rating
  FROM ZomatoRestaurants
  GROUP BY city
)
SELECT z.name, z.city, z.rating
FROM ZomatoRestaurants z
JOIN CityAvgRating c ON z.city = c.city
WHERE c.avg_rating > 4.0;

-- Task 5: Teams with more than 2000 runs in 2023
WITH TeamRuns AS (
  SELECT team, SUM(runs) AS total_runs
  FROM IPLMatches
  WHERE match_year = 2023
  GROUP BY team
)
SELECT * FROM TeamRuns
WHERE total_runs > 2000;

