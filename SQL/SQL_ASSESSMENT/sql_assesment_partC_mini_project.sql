-- Section C: Mini Project
-- 1. Title: Retail Profitability & Market Segment Analysis
-- 2. Problem Statement: Identify underperforming product categories and regions by analyzing the relationship between discount rates and net profit margins.
-- 3. Dataset Recommendation: Sample Superstore Dataset (SampleSuperstore.csv) - https://www.kaggle.com/datasets/vivek468/superstore-dataset-final
-- 4. Required Deliverables: SQL script for database schema creation,multi-condition filtering queries, aggregated performance report by region,and a summary of loss-making transactions.

use assignment;
show tables;
DESCRIBE `orders`;
SELECT * FROM `orders` LIMIT 20;
SELECT COUNT(*) AS Total_Records FROM `orders`;

--  Multi-Condition Filtering Queries
-- A. High discount + loss-making transactions:
SELECT 
    `Order ID`,
    `Customer Name`,
    `Category`,
    `Sub-Category`,
    `Region`,
    `Sales`,
    `Discount`,
    `Profit`
FROM `orders`
WHERE `Discount` > 0.3 
  AND `Profit` < 0
ORDER BY `Profit` ASC
limit 10;

-- B. Underperforming products with high sales but low profit:
SELECT 
    `Order ID`,
    `Customer Name`,
    `Category`,
    `Sub-Category`,
    `Sales`,
    `Discount`,
    `Profit`
FROM `orders`
WHERE `Sales` > 1000 
  AND `Profit` < 100
  AND `Discount` > 0.2
ORDER BY `Profit` ASC;

-- C. Loss-making transactions by segment:
SELECT 
    `Order ID`,
    `Customer Name`,
    `Segment`,
    `Category`,
    `Sales`,
    `Discount`,
    `Profit`
FROM `orders`
WHERE `Profit` < 0
ORDER BY `Segment`, `Profit` ASC
limit 10;

-- 3. Aggregated Performance Report by Region
-- A. Sales, profit and discount by region:
SELECT 
    `Region`,
    COUNT(`Order ID`)            AS Total_Orders,
    ROUND(SUM(`Sales`), 2)       AS Total_Sales,
    ROUND(SUM(`Profit`), 2)      AS Total_Profit,
    ROUND(AVG(`Discount`), 2)    AS Avg_Discount,
    ROUND(SUM(`Profit`) / SUM(`Sales`) * 100, 2) AS Profit_Margin_Pct
FROM `orders`
GROUP BY `Region`
ORDER BY `Total_Profit` DESC;

-- B. Category performance by region:
SELECT 
    `Region`,
    `Category`,
    ROUND(SUM(`Sales`), 2)    AS Total_Sales,
    ROUND(SUM(`Profit`), 2)   AS Total_Profit,
    ROUND(AVG(`Discount`), 2) AS Avg_Discount
FROM `orders`
GROUP BY `Region`, `Category`
ORDER BY `Region`, `Total_Profit` DESC;

-- C. Sub-category profit margin ranking:
SELECT 
    `Sub-Category`,
    ROUND(SUM(`Sales`), 2)                        AS Total_Sales,
    ROUND(SUM(`Profit`), 2)                       AS Total_Profit,
    ROUND(AVG(`Discount`) * 100, 2)               AS Avg_Discount_Pct,
    ROUND(SUM(`Profit`) / SUM(`Sales`) * 100, 2)  AS Profit_Margin_Pct
FROM `orders`
GROUP BY `Sub-Category`
ORDER BY `Profit_Margin_Pct` ASC;

-- 4. Summary of Loss-Making Transactions
-- A. Total loss-making orders:
SELECT 
    COUNT(`Order ID`)       AS Loss_Orders,
    ROUND(SUM(`Profit`), 2) AS Total_Loss,
    ROUND(AVG(`Discount`), 2) AS Avg_Discount
FROM `orders`
WHERE `Profit` < 0;

-- B. Loss-making summary by category:
SELECT 
    `Category`,
    `Sub-Category`,
    COUNT(`Order ID`)         AS Loss_Orders,
    ROUND(SUM(`Sales`), 2)    AS Total_Sales,
    ROUND(SUM(`Profit`), 2)   AS Total_Loss,
    ROUND(AVG(`Discount`), 2) AS Avg_Discount
FROM `orders`
WHERE `Profit` < 0
GROUP BY `Category`, `Sub-Category`
ORDER BY `Total_Loss` ASC;

-- C. Loss-making summary by region:
SELECT 
    `Region`,
    COUNT(`Order ID`)         AS Loss_Orders,
    ROUND(SUM(`Profit`), 2)   AS Total_Loss,
    ROUND(AVG(`Discount`), 2) AS Avg_Discount
FROM `orders`
WHERE `Profit` < 0
GROUP BY `Region`
ORDER BY `Total_Loss` ASC;

-- Discount vs Profit Trend
SELECT 
    Discount,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Discount
ORDER BY Discount;

-- Key Findings
-- Insight Area	                    Observation
-- Worst Performing Region	            Central Region shows the weakest performance, driven by the highest average discount (0.21) and the lowest profit margin (7.92%), indicating heavy discount dependency and reduced profitability.
-- Most Loss-Making Sub-Category	    Tables is the most unprofitable sub-category, contributing approximately $17,725 in total losses, making it the highest loss driver in the dataset.
-- Primary Root Cause of Losses	    Analysis indicates a strong relationship between high discount rates (>30%) and negative profit, suggesting that aggressive discounting significantly erodes margins.
-- Best Performing Region	            The West Region demonstrates the strongest financial performance, with relatively lower discount levels and the highest profit margin, indicating efficient pricing and healthier sales strategy.