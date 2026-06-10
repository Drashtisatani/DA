-- SESSION 1

CREATE DATABASE music_streaming_db;
CREATE DATABASE food_delivery_db;

-- MySQL vs PostgreSQL (3 Differences)

-- 1. Use case

-- MySQL: Best for simple web applications
-- PostgreSQL: Best for complex data and analytics
-- Example: MySQL → WordPress, PostgreSQL → Instagram

-- 2. Features

-- MySQL: Basic SQL features
-- PostgreSQL: Advanced features (JSON, complex queries)
-- Example: MySQL → Facebook (early use), PostgreSQL → Uber

-- 3. Flexibility

-- MySQL: Less flexible
-- PostgreSQL: Highly flexible and customizable
-- Example: MySQL → Shopify, PostgreSQL → Netflix


use food_delivery_db; 

CREATE TABLE restaurants (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  rating DECIMAL(2,1)
);

INSERT INTO restaurants (name, rating) VALUES
('Pizza Hub', 4.6),
('Burger King', 4.2),
('Cafe Coffee Day', 4.5),
('Spice Villa', 4.8);

CREATE TABLE movies (
  id INT AUTO_INCREMENT PRIMARY KEY,
  movie_name VARCHAR(100),
  release_year INT,
  genre VARCHAR(50),
  box_office_collection BIGINT
);

INSERT INTO movies VALUES
(1, 'Avengers Endgame', 2019, 'Action', 2790000000),
(2, 'Pathaan', 2023, 'Action', 1050000000),
(3, 'Interstellar', 2014, 'Sci-Fi', 677000000),
(4, 'John Wick 4', 2023, 'Action', 440000000);

CREATE TABLE products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  price INT,
  category VARCHAR(50),
  sold_count INT
);

INSERT INTO products VALUES
(1, 'iPhone 14', 70000, 'Electronics', 500),
(2, 'Shoes Nike', 1200, 'Fashion', 800),
(3, 'Laptop Dell', 55000, 'Electronics', 300),
(4, 'T-Shirt', 400, 'Fashion', 1000);

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100),
  city VARCHAR(50),
  followers INT
);

INSERT INTO users VALUES
(1, 'Aarav', 'Ahmedabad', 1500),
(2, 'Neha', 'Surat', 900),
(3, 'Raj', 'Vadodara', 2000),
(4, 'Simran', 'Mumbai', 500);

CREATE TABLE songs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  song_name VARCHAR(100),
  artist_name VARCHAR(100)
);

INSERT INTO songs VALUES
(1, 'Love Story', 'Taylor Swift'),
(2, 'Shape of You', 'Ed Sheeran'),
(3, 'Arijit Special', 'Arijit Singh'),
(4, 'Believer', 'Imagine Dragons');

CREATE TABLE food_orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  amount INT
);

INSERT INTO food_orders VALUES
(1, 1, 500),
(2, 2, 300),
(3, 1, 700),
(4, 3, 400);

CREATE TABLE transactions (
  transaction_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  amount INT,
  payment_method VARCHAR(50)
);

INSERT INTO transactions VALUES
(1, 1, 500, 'UPI'),
(2, 2, 1000, 'Card'),
(3, 3, 700, 'UPI'),
(4, 1, 300, 'Cash');

CREATE TABLE bookings (
  id INT AUTO_INCREMENT PRIMARY KEY,
  booking_date DATE
);

INSERT INTO bookings (booking_date) VALUES
('2025-06-01'),
('2025-06-02'),
('2025-06-03'),
('2025-06-04');

CREATE TABLE spotify_playlists (
  playlist_id INT,
  user_id INT,
  song_id INT
);

INSERT INTO spotify_playlists VALUES
(1, 1, 1),
(1, 1, 2),
(2, 2, 3),
(3, 3, 4);

CREATE TABLE bookmyshow_reviews (
  review_id INT AUTO_INCREMENT PRIMARY KEY,
  movie_id INT,
  rating DECIMAL(2,1)
);

INSERT INTO bookmyshow_reviews VALUES
(1, 1, 4.5),
(2, 1, 4.0),
(3, 2, 4.8),
(4, 3, 3.9);

CREATE TABLE paytm_transactions (
  txn_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  amount INT
);

INSERT INTO paytm_transactions VALUES
(1, 1, 200),
(2, 1, 500),
(3, 2, 100),
(4, 3, 900);

CREATE TABLE myntra_orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  total_price INT
);

INSERT INTO myntra_orders VALUES
(1, 1, 1000),
(2, 1, 1500),
(3, 2, 500),
(4, 3, 2000);

CREATE TABLE zomato_reviews (
  id INT,
  name VARCHAR(100),
  rating DECIMAL(2,1)
);

INSERT INTO zomato_reviews VALUES
(1, 'Pizza Hub', 4.5),
(2, 'Burger King', 4.2);

CREATE TABLE playlists (
  playlist_id INT,
  user_id INT,
  song_id INT,
  duration INT
);

INSERT INTO playlists VALUES
(1,1,101,2000),
(1,1,102,3000),
(2,2,103,2500),
(3,3,104,8700);
