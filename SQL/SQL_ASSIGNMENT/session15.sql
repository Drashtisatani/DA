use food_delivery_db; 



-- SESSION 15 

CREATE TABLE Deliveries (
  delivery_id INT PRIMARY KEY,
  delivery_date DATE
);
INSERT INTO Deliveries VALUES
(1, '2024-02-10'),
(2, '2024-02-15'),
(3, '2024-02-20');

CREATE TABLE Subscriptions (
  user_id INT PRIMARY KEY,
  start_date DATE,
  end_date DATE
);
INSERT INTO Subscriptions VALUES
(1, '2023-01-01', '2023-12-31'),
(2, '2023-06-01', '2024-05-31'),
(3, '2024-01-01', '2024-06-30');

CREATE TABLE AppLogins (
  user_id INT PRIMARY KEY,
  last_login_date DATE
);
INSERT INTO AppLogins VALUES
(1, '2024-01-01'),
(2, CURDATE()),
(3, DATE_SUB(CURDATE(), INTERVAL 40 DAY)),
(4, DATE_SUB(CURDATE(), INTERVAL 10 DAY));

-- Task 1: Current date and time
SELECT NOW() AS CurrentDateTime;

-- Task 2: Order date broken into year, month, day
SELECT order_id,
       order_date,
       YEAR(order_date) AS year,
       MONTH(order_date) AS month,
       DAY(order_date) AS day
FROM FlipkartOrders;

-- Task 3: Expected pickup date 2 days before delivery
SELECT delivery_date,
       DATE_SUB(delivery_date, INTERVAL 2 DAY) AS expected_pickup_date
FROM Deliveries;

-- Task 4: Subscription duration in days
SELECT user_id,
       start_date,
       end_date,
       DATEDIFF(end_date, start_date) AS total_days
FROM Subscriptions;

-- Task 5: Users who haven't logged in for 30+ days
SELECT user_id, last_login_date
FROM AppLogins
WHERE DATEDIFF(NOW(), last_login_date) > 30;