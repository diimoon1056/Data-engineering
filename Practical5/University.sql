create database University;

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

INSERT INTO orders()
