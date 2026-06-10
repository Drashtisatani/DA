use food_delivery_db;

-- SESSION 8 

CREATE TABLE app_users (
  user_id INT PRIMARY KEY,
  username VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE orders_j8 (
  order_id INT PRIMARY KEY,
  user_id INT,
  product VARCHAR(50),
  amount INT
);


INSERT INTO app_users VALUES
(1,'Aarav','Ahmedabad'),
(2,'Neha','Surat'),
(3,'Raj','Mumbai');

INSERT INTO orders_j8 VALUES
(101,1,'Pizza',500),
(102,1,'Burger',300),
(103,2,'Pasta',400),
(104,3,'Biryani',600),
(105,4,'Sandwich',200);

-- 2. INNER JOIN
SELECT u.username, o.product
FROM app_users u
INNER JOIN orders_j8 o
ON u.user_id = o.user_id;
--  3. LEFT JOIN
SELECT u.username, o.product
FROM app_users u
LEFT JOIN orders_j8 o
ON u.user_id = o.user_id;
 -- 4. RIGHT JOIN
SELECT o.order_id, u.username
FROM app_users u
RIGHT JOIN orders_j8 o
ON u.user_id = o.user_id;
 
 
-- TASK 5
CREATE TABLE CustomerSegments (
  segment_id INT PRIMARY KEY,
  segment_name VARCHAR(50)
);

INSERT INTO CustomerSegments VALUES
(1, 'Gold'),
(2, 'Silver'),
(3, 'Bronze');


ALTER TABLE app_users ADD segment_id INT;

UPDATE app_users SET segment_id = 1 WHERE user_id = 1;
UPDATE app_users SET segment_id = 2 WHERE user_id = 2;
UPDATE app_users SET segment_id = 3 WHERE user_id = 3;


SELECT u.username,
       cs.segment_name,
       SUM(o.amount) AS total_order_amount
FROM app_users u
LEFT JOIN CustomerSegments cs ON u.segment_id = cs.segment_id
LEFT JOIN orders_j8 o ON u.user_id = o.user_id
GROUP BY u.username, cs.segment_name;
