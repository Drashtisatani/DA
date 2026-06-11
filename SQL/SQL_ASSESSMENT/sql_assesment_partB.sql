use assignment;

-- Section B: Practical Task

-- 1. Execute a query to retrieve the first 20 records from the orders table to verify data ingestion.
	SELECT *
	FROM `orders`
	LIMIT 20;


-- 2. Select Order ID, Order Date, Sales, and Profit, applying a column alias to display Sales as Total_Sales.
	SELECT 
		`Order ID`,
		`Order Date`,
		`Sales` AS `Total_Sales`,
		`Profit`
	FROM `orders`;
--     
--     
-- 3. Filter the dataset to isolate all high-value transactions where the Sales figure exceeds 5000.
		SELECT 
			`Order ID`,
			`Customer Name`,
			`Category`,
			`Sub-Category`,
			`Sales`,
			`Profit`
		FROM `orders`
		WHERE `Sales` > 5000
		ORDER BY `Sales` DESC;
--         

-- 4. Generate a report of the top 10 most profitable orders by sorting the records by Profit in descending order.
		SELECT 
			`Order ID`,
			`Customer Name`,
			`Category`,
			`Sales`,
			`Profit`
		FROM `orders`
		ORDER BY `Profit` DESC
		LIMIT 10;

