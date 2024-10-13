-- Create the database
CREATE DATABASE myntra_data_analysis;
USE myntra_data_analysis;

-- Create the Products table
CREATE TABLE dim_products (
    Product_ID VARCHAR(10) PRIMARY KEY,
    Category VARCHAR(50),
    Sub_category VARCHAR(50),
    Product_Name VARCHAR(100),
    Brand_Name VARCHAR(50),
    Size INT,
    Color VARCHAR(20),
    Ratings INT
);

-- Create the Customers table
CREATE TABLE dim_customers (
    Customer_ID VARCHAR(10) PRIMARY KEY,
    Customer_Age INT,
    City VARCHAR(50),
    State VARCHAR(50)
);

-- Create the Orders table
CREATE TABLE fact_orders (
    Order_ID VARCHAR(10) PRIMARY KEY,
    Customer_ID VARCHAR(10),
    Product_ID VARCHAR(10),
    Order_Date DATE,
    Original_Price DECIMAL(10, 2),
    Discount_Percent DECIMAL(5, 2),
    FOREIGN KEY (Customer_ID) REFERENCES dim_customers(Customer_ID),
    FOREIGN KEY (Product_ID) REFERENCES dim_products(Product_ID)
);
