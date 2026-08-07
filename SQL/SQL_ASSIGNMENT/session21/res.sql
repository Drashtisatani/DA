CREATE DATABASE RestaurantDB;

USE RestaurantDB;

CREATE TABLE Restaurants (
    restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cuisine VARCHAR(50) NOT NULL,
    rating DECIMAL(2,1) NOT NULL
);

INSERT INTO Restaurants (name, cuisine, rating)
VALUES
('Dragon Palace', 'Chinese', 4.7),
('Spice Villa', 'South Indian', 4.5),
('Bombay Bites', 'North Indian', 4.2),
('Pizza Hub', 'Italian', 3.9),
('Wok Express', 'Chinese', 4.3),
('Dosa Corner', 'South Indian', 4.8),
('Burger Town', 'Fast Food', 3.6),
('Tandoori House', 'North Indian', 4.6),
('Pasta Point', 'Italian', 4.1),
('Sushi World', 'Japanese', 4.9);

SELECT * FROM Restaurants;

