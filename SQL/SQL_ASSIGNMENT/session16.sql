use food_delivery_db; 


-- SESSION 16 

CREATE TABLE full_users (
  id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50)
);
INSERT INTO full_users VALUES
(1, 'Aarav', 'Shah'),
(2, 'Neha', 'Patel'),
(3, 'Raj', 'Mehta');

CREATE TABLE song_titles (
  id INT PRIMARY KEY,
  song_title VARCHAR(100)
);
INSERT INTO song_titles VALUES
(1, 'tum hi ho'),
(2, 'shape of you'),
(3, 'kesariya');

CREATE TABLE food_items (
  id INT PRIMARY KEY,
  item_code VARCHAR(50)
);
INSERT INTO food_items VALUES
(1, '  PIZZA01  '),
(2, ' BURGER02 '),
(3, '  PASTA03');

CREATE TABLE imdb_movies (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  imdb_id VARCHAR(20)
);
INSERT INTO imdb_movies VALUES
(1, 'Pathaan', 'tt1234567'),
(2, 'Jawan', 'tt7654321'),
(3, 'Dunki', 'tt9876543');

CREATE TABLE sku_products (
  id INT PRIMARY KEY,
  sku_code VARCHAR(50)
);
INSERT INTO sku_products VALUES
(1, 'MOB-123-XY'),
(2, 'LAP-456-AB'),
(3, 'TAB-789-CD');

-- Task 1: CONCAT first and last name
SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM full_users;

-- Task 2: Song titles in uppercase
SELECT UPPER(song_title) AS song_title_upper
FROM song_titles;

-- Task 3: Trim spaces from item_code
SELECT TRIM(item_code) AS clean_item_code
FROM food_items;

-- Task 4: Extract last 7 chars of imdb_id
SELECT name,
       RIGHT(imdb_id, 7) AS movie_number
FROM imdb_movies;

-- Task 5: Replace dashes with underscores in sku_code
SELECT REPLACE(sku_code, '-', '_') AS updated_sku
FROM sku_products;
