# Myyntra Dataset End-to-End Data Analysis Project Using Python, MySQL, and Power BI

This project demonstrates a comprehensive end-to-end data analysis process using Python for data cleaning, MySQL for structured data storage, and Power BI for building interactive dashboards. The project walks through essential steps such as understanding the dataset, setting up the database, performing data cleaning, and building insightful visualizations.

## Project Structure

data_analysis_project/  
│  
├── data/  
│   ├── Myntra dataset.xlsx           # Original dataset  
│   ├── dim_products_clean.csv        # Cleaned product data for Power BI  
│   ├── dim_customers_clean.csv       # Cleaned customer data for Power BI  
│   └── fact_orders_clean.csv         # Cleaned orders data for Power BI  
│  
├── mysql_scripts/  
│   └── create_tables.sql             # SQL script to create tables in MySQL  
│  
├── python_scripts/  
│   ├── load_data.py                  # Python script to load data into MySQL  
│   ├── clean_data.py                 # Python script for data cleaning and preprocessing  
│   ├── analyze_data.py               # Python script for performing analysis on the data  
│   └── visualize_sales.py            # Python script for sales trend visualization  
│  
├── power_bi_dashboard/  
│   ├── dashboard.pbix                # Power BI project file  
│   └── dashboard_instructions.md     # Instructions for Power BI dashboard setup  
│  
└── README.md                         # Project overview and instructions (this file)

## Requirements

- Python 3.x
- MySQL (local or remote server)
- Power BI Desktop
- Required Python packages:
  - `pandas`
  - `mysql-connector-python`
  - `matplotlib`

## Dataset Overview

The dataset contains three sheets:

1. **dim_products**: Product details, including category, brand, size, and ratings.
2. **dim_customers**: Customer information, including age, city, and state.
3. **fact_orders**: Transaction data, including order date, product price, and discount.

## Steps

### 1. **Data Structure Overview**

The dataset contains three sheets (`dim_products`, `dim_customers`, and `fact_orders`). The structure is as follows:

- **dim_products**: Contains product-related information like category, sub-category, product name, brand name, size, and ratings.
- **dim_customers**: Contains customer-related information such as customer age, city, and state.
- **fact_orders**: Contains order-related information including order ID, customer ID, product ID, order date, original price, and discount percentage.

### 2. **Setting Up MySQL Database**

You can find the SQL script to create the necessary tables in the `mysql_scripts/create_tables.sql` file.

- Run the script in your MySQL Workbench or any SQL environment.

  Example:

  ```sql
  CREATE DATABASE myntra_data_analysis;
  USE myntra_data_analysis;

  -- Create tables (dim_products, dim_customers, fact_orders)
  -- Refer to the `create_tables.sql` for full details
  ```

### 3. **Data Cleaning and Loading**

The data cleaning process is handled in Python. Refer to the `python_scripts/clean_data.py` to clean the data and save the cleaned CSV files for use in Power BI.

Run the cleaning script:

```bash
python python_scripts/clean_data.py
```

After cleaning, use the `load_data.py` script to load data into MySQL:

```bash
python python_scripts/load_data.py
```

### 4. **Power BI Dashboard**

Follow the steps below to load the data into Power BI and create visualizations:

1. Open Power BI Desktop.
2. Go to **Home > Get Data > MySQL Database**.
3. Enter your MySQL server details, select the database `myntra_data_analysis`, and load the tables (`dim_products_clean.csv`, `dim_customers_clean.csv`, `fact_orders_clean.csv`).
4. Create the following key visuals:
   - **Bar Chart**: Sales by Product Category.
   - **Line Chart**: Sales Trends Over Time.
   - **Map**: Customer Distribution by State.
5. Add slicers for **Order Date**, **Category**, and **State** for interactivity.
6. Format and enhance the dashboard as needed.

## Key Visuals in Power BI

1. **Bar Chart: Sales by Product Category**
   - X-axis: `Category` (from `dim_products`)
   - Y-axis: `Original Price` (from `fact_orders`)

2. **Line Chart: Sales Trends Over Time**
   - X-axis: `Date` (from `fact_orders`)
   - Y-axis: `Original Price`

3. **Map: Customer Distribution by State**
   - Location: `State` (from `dim_customers`)
   - Size: `Customer_ID` (to show number of customers per state)

## Conclusion

This project provides a structured workflow from data cleaning and analysis using Python to visualization with Power BI, all while leveraging the efficiency of a MySQL database for data storage. The dashboard allows users to interact with the data, providing insights into customer demographics, sales trends, and product performance.

## Additional Files

The cleaned CSV files (`dim_products_clean.csv`, `dim_customers_clean.csv`, `fact_orders_clean.csv`) are included in the `data/` folder and can be used directly in Power BI or for further analysis.
