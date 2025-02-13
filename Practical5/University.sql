--Завдання 1
create database Shop;
USE Shop;
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category_id INT,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL
);

CREATE TABLE OrderDetails (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

INSERT INTO Customers(customer_id, customer_name, email, phone) 
VALUES
(1, 'John Doe', 'johndoe@example.com', '123-456-7890'),
(2, 'Jane Smith', 'janesmith@example.com', '987-654-3210'),
(3, 'Michael Johnson', 'michaelj@example.com', '555-123-4567'),
(4, 'Emily Davis', 'emily.davis@example.com', '444-234-5678'),
(5, 'David Wilson', 'david.wilson@example.com', '333-345-6789'),
(6, 'Sarah Brown', 'sarah.brown@example.com', '222-456-7891'),
(7, 'Daniel Lee', 'daniel.lee@example.com', '111-567-8902'),
(8, 'Olivia Martin', 'olivia.martin@example.com', '666-678-9012'),
(9, 'James Harris', 'james.harris@example.com', '777-789-0123'),
(10, 'Sophia Clark', 'sophia.clark@example.com', '888-890-1234');

INSERT INTO Categories(category_id, category_name) 
VALUES
(1, 'Electronics'),
(2, 'Clothing'),
(3, 'Home Appliances'),
(4, 'Books'),
(5, 'Sports'),
(6, 'Toys'),
(7, 'Beauty'),
(8, 'Furniture'),
(9, 'Groceries'),
(10, 'Automotive');

INSERT INTO Orders (customer_id, order_date, total_price) VALUES
(1, '2025-02-01', 250.75),
(2, '2025-02-02', 120.40),
(3, '2025-02-03', 315.00),
(4, '2025-02-04', 540.60),
(5, '2025-02-05', 95.20),
(6, '2025-02-06', 425.30),
(7, '2025-02-07', 210.50),
(8, '2025-02-08', 800.90),
(9, '2025-02-09', 150.00),
(10, '2025-02-10', 400.00);

--Завдання 2

SELECT SUM(total_price) AS total_orders_sum
FROM Orders;

SELECT customer_id, COUNT(order_id) AS order_count
FROM Orders
GROUP BY customer_id;

INSERT INTO Products (product_name, category_id, price, stock_quantity) VALUES
('Laptop', 1, 1200.99, 50),
('Smartphone', 2, 699.99, 100),
('Headphones', 3, 199.50, 150),
('Keyboard', 4, 89.99, 200),
('Mouse', 4, 39.99, 300),
('Monitor', 1, 300.75, 80),
('Smartwatch', 2, 250.00, 120),
('Tablet', 1, 499.99, 60),
('Speakers', 3, 150.00, 180),
('Camera', 2, 450.00, 70);

SELECT 
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    AVG(price) AS avg_price
FROM Products;

INSERT INTO OrderDetails (order_id, product_id, quantity, price) VALUES
(1, 1, 2, 1200.99),
(1, 2, 1, 699.99),
(2, 3, 3, 199.50),
(3, 4, 1, 89.99),
(4, 5, 5, 39.99),
(5, 6, 2, 300.75),
(6, 7, 1, 250.00),
(7, 8, 4, 499.99),
(8, 9, 1, 150.00),
(9, 10, 54534, 450.00);

SELECT p.category_id, SUM(od.quantity) AS total_sold
FROM Products p
JOIN OrderDetails od ON p.product_id = od.product_id
GROUP BY p.category_id;

SELECT p.category_id, SUM(od.quantity) AS total_sold
FROM Products p
JOIN OrderDetails od ON p.product_id = od.product_id
GROUP BY p.category_id
HAVING SUM(od.quantity) > 100;

--Завдання 3

SELECT order_id, total_price
FROM Orders
WHERE total_price > (SELECT AVG(total_price) FROM Orders);

SELECT customer_id
FROM Customers
WHERE customer_id IN (SELECT DISTINCT customer_id FROM Orders);

SELECT product_id
FROM Products
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM OrderDetails);

SELECT p.category_id, p.product_id, p.product_name, p.price
FROM Products p
WHERE p.price = (
    SELECT MAX(p2.price)
    FROM Products p2
    WHERE p2.category_id = p.category_id
);
