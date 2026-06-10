use food_delivery_db; 


-- SESSION 19 
CREATE TABLE large_orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  product VARCHAR(50),
  category VARCHAR(50),
  amount INT
);

DELIMITER //
CREATE PROCEDURE InsertLargeOrders()
BEGIN
  DECLARE i INT DEFAULT 1;
  WHILE i <= 10000 DO
    INSERT INTO large_orders (user_id, product, category, amount)
    VALUES (
      FLOOR(1 + RAND() * 100),
      ELT(FLOOR(1 + RAND() * 3), 'Pizza', 'Burger', 'Pasta'),
      ELT(FLOOR(1 + RAND() * 3), 'Food', 'Electronics', 'Fashion'),
      FLOOR(100 + RAND() * 5000)
    );
    SET i = i + 1;
  END WHILE;
END //
DELIMITER ;

CALL InsertLargeOrders();

-- Task 1: Query before index (measure time)
SELECT * FROM large_orders WHERE user_id = 5;

-- Task 2: Create index and re-run
CREATE INDEX idx_user_id ON large_orders(user_id);
SELECT * FROM large_orders WHERE user_id = 5;

-- Task 3: EXPLAIN before and after index
EXPLAIN SELECT * FROM large_orders WHERE user_id = 5;

-- Task 4: Use index on category column
CREATE INDEX idx_category ON large_orders(category);
SELECT * FROM large_orders WHERE category = 'Electronics';

-- Task 5: EXPLAIN + optimization tip
EXPLAIN SELECT * FROM large_orders WHERE user_id = 5;
-- AI Suggested Optimization: Use SELECT only needed columns
-- instead of SELECT * to reduce data transfer
-- Example:
SELECT order_id, amount FROM large_orders WHERE user_id = 5;