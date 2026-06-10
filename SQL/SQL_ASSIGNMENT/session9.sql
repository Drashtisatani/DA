use food_delivery_db;

-- SESSION 9 
-- TASK 1: FULL OUTER JOIN
SELECT i.name AS influencer_name, b.name AS brand_name
FROM influencers i
LEFT JOIN brands b ON i.city = b.city
UNION
SELECT i.name AS influencer_name, b.name AS brand_name
FROM influencers i
RIGHT JOIN brands b ON i.city = b.city;


-- TASK 2: SELF JOIN (nested playlists)
CREATE TABLE nested_playlists (
  id INT PRIMARY KEY,
  playlist_name VARCHAR(50),
  parent_playlist_id INT
);

INSERT INTO nested_playlists VALUES
(1, 'My Music', NULL),
(2, 'Chill Vibes', 1),
(3, 'Work Mode', 1),
(4, 'Lo-Fi Beats', 2);

-- Show each playlist with its parent playlist name
SELECT p.playlist_name AS playlist,
       parent.playlist_name AS parent_playlist
FROM nested_playlists p
LEFT JOIN nested_playlists parent ON p.parent_playlist_id = parent.id;


-- TASK 3: CROSS JOIN (users & offers)

CREATE TABLE offer_users (
  id INT PRIMARY KEY,
  user_name VARCHAR(50)
);

CREATE TABLE offers (
  id INT PRIMARY KEY,
  offer_title VARCHAR(50)
);

INSERT INTO offer_users VALUES
(1, 'Aarav'),
(2, 'Neha'),
(3, 'Raj');

INSERT INTO offers VALUES
(1, '10% Off'),
(2, 'Free Delivery'),
(3, 'Buy 1 Get 1');

-- CROSS JOIN: every user gets every offer
SELECT u.user_name, o.offer_title
FROM offer_users u
CROSS JOIN offers o;


-- TASK 4: SELF JOIN (employees & managers)
CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  manager_id INT
);
INSERT INTO employees VALUES
(1, 'Ankit', NULL),
(2, 'Priya', 1),
(3, 'Rahul', 1),
(4, 'Simran', 2);

-- Show each employee with their manager name
SELECT e.name AS employee,
       m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- Show only top-level managers (no manager)
SELECT name AS top_manager
FROM employees
WHERE manager_id IS NULL;


-- TASK 5: SELF JOIN (users in same city)
SELECT a.username AS user1,
       b.username AS user2,
       a.city
FROM app_users a
JOIN app_users b ON a.city = b.city
WHERE a.user_id < b.user_id;
