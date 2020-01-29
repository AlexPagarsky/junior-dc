--1
CREATE DATABASE shop;


--2
CREATE USER 'shop'@'localhost' IDENTIFIED BY 'shop7@Shop';
GRANT ALL PRIVILEGES ON shop.* TO 'shop'@'localhost';


--3
CREATE USER 'viewer'@'localhost' IDENTIFIED BY 'view7@View';
GRANT SELECT ON shop.* TO 'viewer'@'%';


--4
CREATE TABLE categories (
    category_name VARCHAR(255) PRIMARY KEY
);


--5
INSERT INTO categories (category_name) VALUES
('PC'),
('smartphone'),
('laptop'),
('keyboard'),
('mouse'),
('speakers'),
('monitor');


--6
CREATE TABLE goods (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255) REFERENCES categories(category_name),
    price NUMERIC(16, 2) NOT NULL
);


--7
INSERT INTO goods (name, category, price) VALUES
    ('razer smth', 'mouse', 1.00),
    ('acer  240ghz', 'monitor', 1.00),
    ('macbook', 'laptop', 1.00),
    ('sony', 'speakers', 1.00),
    ('a4tech', 'keyboard', 1.00),
    ('razer smth2', 'keyboard', 1.00),
    ('acer gaming', 'mouse', 1.00);


--8
UPDATE goods SET price = 3.5
WHERE id = 1;


--9
UPDATE goods SET price = price * 1.1;


--10
DELETE FROM goods
WHERE id = 2;


--11
SELECT * FROM goods
ORDER BY name;


--12
SELECT * FROM goods
ORDER BY price DESC;


--13
SELECT * FROM goods
ORDER BY price DESC
LIMIT 3;


--14
SELECT * FROM goods
ORDER BY price ASC
LIMIT 3;


--15
SELECT * FROM goods
ORDER BY price DESC
LIMIT 3 OFFSET 3;


--16
SELECT * FROM goods
ORDER BY price DESC
LIMIT 1;


--17
SELECT * FROM goods
ORDER BY price ASC
LIMIT 1;


--18
SELECT COUNT(*) FROM goods;


--19
SELECT AVG(price) FROM goods;


--20
CREATE VIEW most_exp AS
(SELECT * FROM goods ORDER BY price DESC LIMIT 3);