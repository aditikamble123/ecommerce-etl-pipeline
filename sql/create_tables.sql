CREATE DATABASE ecommerce_dw;
USE ecommerce_dw;

CREATE TABLE IF NOT EXISTS customers_dim (
  user_id INT PRIMARY KEY,
  country VARCHAR(50),
  customer_segment VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS products_dim (
  product_id INT PRIMARY KEY,
  category VARCHAR(50),
  price DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS date_dim (
  date_id INT PRIMARY KEY,
  order_date DATE,
  year INT,
  month INT,
  day INT
);

CREATE TABLE IF NOT EXISTS orders_fact (
  order_id INT PRIMARY KEY,
  user_id INT,
  product_id INT,
  date_id INT,
  qty INT,
  total_price DECIMAL(10,2)
);
