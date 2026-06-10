use food_delivery_db; 

-- SESSION 10 
-- TASK 1: Create tables and insert data

CREATE TABLE AppOrders (
  order_id INT PRIMARY KEY,
  customer_name VARCHAR(50),
  amount INT,
  order_date DATE
);

CREATE TABLE InStoreOrders (
  order_id INT PRIMARY KEY,
  customer_name VARCHAR(50),
  amount INT,
  order_date DATE
);

INSERT INTO AppOrders VALUES
(1, 'Aarav', 250, '2024-01-10'),
(2, 'Priya', 400, '2024-01-11'),
(3, 'Rahul', 150, '2024-01-12');

INSERT INTO InStoreOrders VALUES
(4, 'Sonal', 300, '2024-01-10'),
(5, 'Priya', 400, '2024-01-11'),
(6, 'Mihir', 500, '2024-01-13');


-- TASK 2: UNION (unique customer names only)
SELECT customer_name FROM AppOrders
UNION
SELECT customer_name FROM InStoreOrders;

-- TASK 3: UNION ALL (all orders including duplicates)
SELECT order_id, customer_name, amount, order_date FROM AppOrders
UNION ALL
SELECT order_id, customer_name, amount, order_date FROM InStoreOrders;

-- TASK 4: Difference between UNION and UNION ALL
SELECT customer_name FROM AppOrders
UNION
SELECT customer_name FROM InStoreOrders;


SELECT customer_name FROM AppOrders
UNION ALL
SELECT customer_name FROM InStoreOrders;
