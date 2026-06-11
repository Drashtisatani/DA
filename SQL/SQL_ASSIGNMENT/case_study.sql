use zometo_data;

CREATE TABLE zomato_restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    cuisines VARCHAR(200),
    rating DECIMAL(2,1),
    votes INT,
    cost_for_two INT,
    restaurant_type VARCHAR(50)
);

INSERT INTO zomato_restaurants
(id, name, location, cuisines, rating, votes, cost_for_two, restaurant_type)
VALUES
(1,'Empire Restaurant','Koramangala','North Indian, Biryani',4.5,2500,800,'Casual Dining'),

(2,'Truffles','Koramangala','American, Fast Food',4.7,4200,1200,'Cafe'),

(3,'Meghana Foods','Koramangala','Andhra, Biryani',4.6,3800,1000,'Casual Dining'),

(4,'Cafe Terra','Koramangala','Cafe, Italian',4.8,1500,1400,'Cafe'),

(5,'Punjab Grill','Koramangala','North Indian',4.4,900,1800,'Fine Dining'),

(6,'The Black Pearl','Koramangala','Continental, BBQ',4.9,2200,2200,'Fine Dining'),

(7,'Corner House','Indiranagar','Desserts, Ice Cream',4.3,1800,400,'Dessert Parlor'),

(8,'Toit','Indiranagar','Continental, Finger Food',4.5,3500,1800,'Pub'),

(9,'Biryani Zone','Indiranagar','Biryani, Mughlai',4.1,900,700,'Quick Bites'),

(10,'Cafe Coffee Day','Indiranagar','Cafe, Beverages',3.8,300,500,'Cafe'),

(11,'KFC','Indiranagar','Fast Food, Burger',3.5,450,600,'Quick Bites'),

(12,'Dominos Pizza','Indiranagar','Pizza, Fast Food',3.9,550,700,'Quick Bites'),

(13,'Poorvika Diner','BTM Layout','South Indian',2.8,350,300,'Casual Dining'),

(14,'Taste Hub','HSR Layout','Chinese',2.6,280,450,'Casual Dining'),

(15,'Foodies Point','Jayanagar','North Indian',2.9,500,600,'Quick Bites'),

(16,'Royal Feast','MG Road','Multi Cuisine',4.2,1200,2500,'Fine Dining'),

(17,'Cafe Bliss','Whitefield','Cafe, Desserts',4.0,650,900,'Cafe'),

(18,'Green Bowl','Indiranagar','Healthy Food, Salad',4.1,320,800,'Cafe'),

(19,'Burger Shack','Koramangala','Burger, Fast Food',4.3,850,700,'Quick Bites'),

(20,'Luxury Plate','Koramangala','Italian, Continental',4.7,1300,3200,'Fine Dining');

-- Query 1: Top 5 Highest Rated Restaurants in Koramangala
SELECT
    name,
    rating,
    votes
FROM zomato_restaurants
WHERE location='Koramangala'
ORDER BY rating DESC, votes DESC
LIMIT 5;

-- Query 2: Unique Cuisines in Indiranagar
SELECT
    cuisines,
    COUNT(*) AS restaurant_count
FROM zomato_restaurants
WHERE location='Indiranagar'
GROUP BY cuisines
ORDER BY restaurant_count DESC;

-- Query 3: Average Cost by Restaurant Type
SELECT
    restaurant_type,
    ROUND(AVG(cost_for_two),2) AS avg_cost
FROM zomato_restaurants
GROUP BY restaurant_type
ORDER BY avg_cost DESC;

-- Query 4: Low Rating (<3.0) and High Votes (>200)
SELECT
    name,
    location,
    rating,
    votes
FROM zomato_restaurants
WHERE rating < 3.0
AND votes > 200;

-- Query 5: Market Segmentation
SELECT
    name,
    location,
    cost_for_two,
    CASE
        WHEN cost_for_two < 500 THEN 'Budget'
        WHEN cost_for_two BETWEEN 500 AND 1500 THEN 'Mid-range'
        ELSE 'Premium'
    END AS market_segment
FROM zomato_restaurants
ORDER BY cost_for_two;

