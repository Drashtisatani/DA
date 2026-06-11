use assignment;

-- Section A: Concept Application 

-- 1. What is the functional difference between SELECT * and specifying column names, and when is each preferred?
	-- SELECT * returns every column in the table. 
	-- Specifying column names returns only what you ask for.
	-- SELECT * FROM orders;                 -- returns all columns
	-- SELECT city FROM orders;              -- returns only these two

	-- When to use each:
	-- Use SELECT * for quick exploration and previewing table structure
	-- Use named columns in production queries — faster, avoids fetching unwanted data, and safer when tables change



-- 2. Which keyword renames a column in the output, and does this alias change the actual table structure in the database?
	-- The keyword is AS. 
	-- It renames a column only in the output — 
	-- the actual table structure in the database is not changed at all.
	-- SELECT Profit AS net_profit FROM orders;
	-- The alias exists only for that query's result. Once the query ends, it's gone.

-- 3. Why does wrapping a numeric value in quotes (e.g., create a data type conflict in SQL?
	-- Writing '100' instead of 100 tells SQL it is a string, not a number. 
	-- This causes a data type conflict when the column stores numeric data.

	-- WHERE Sales > '100'   -- string comparison, can give wrong results
	-- WHERE Sales > 100     -- correct numeric comparison

	-- String comparison is alphabetical, not arithmetic




-- 4. Contrast the results of ORDER BY Profit DESC versus ASC when the goal is to identify the top 10 most profitable orders
	-- ORDER BY Profit DESC — sorts highest to lowest → first 10 rows = profit
	-- ORDER BY Profit ASC — sorts lowest to highest → first 10 rows = loss

	-- SELECT `Order ID`, Profit
	-- FROM orders
	-- ORDER BY Profit DESC
	-- LIMIT 10;

-- 5. What is the T-SQL equivalent of the LIMIT clause in MS SQL Server, and why does syntax vary across SQL engines?
	-- 	MS SQL Server does not support LIMIT. It uses TOP instead:	
	-- 	SELECT TOP 10 'Order_ID', Profit
	-- 	FROM orders
	-- 	ORDER BY Profit DESC;
	-- 	Why syntax varies: Each database engine was built independently and added features before a universal standard existed.
	--     LIMIT was never part of the original ANSI SQL standard, so every vendor solved it differently.


-- 6. Explain the logical execution order of a query containing SELECT, WHERE, ORDER BY, and LIMIT clauses. 
	-- 	The order you write a query and the order the database executes it are different:
	-- 	1. FROM        → identify the table(s) to read
	-- 	2. WHERE       → filter rows based on condition
	-- 	3. GROUP BY    → group the filtered rows
	-- 	4. HAVING      → filter the groups
	-- 	5. SELECT      → pick which columns to show
	-- 	6. ORDER BY    → sort the final result
	-- 	7. LIMIT       → cut to N rows





