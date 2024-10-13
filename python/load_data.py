import pandas as pd
import mysql.connector

# Load the Excel file
file_path = r'E:\myntra_data_analysis\data\Myntra dataset.xlsx'
xls = pd.ExcelFile(file_path)

# Load each sheet into a DataFrame
dim_products = pd.read_excel(xls, sheet_name='dim_products ')
dim_customers = pd.read_excel(xls, sheet_name='dim_customers')
fact_orders = pd.read_excel(xls, sheet_name='fact_orders')

# Clean the data
# Remove duplicates
dim_products.drop_duplicates(subset='Product ID', keep='last', inplace=True)
dim_customers.drop_duplicates(subset='Customer ID', keep='last', inplace=True)
fact_orders.drop_duplicates(subset='Order ID', keep='last', inplace=True)

# Handle NaN values
dim_products['Size'] = dim_products['Size'].fillna(0)  # Replace NaN with 0

# Function to load data into MySQL
def load_data_to_mysql(data, table_name):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rtrip@0727",
        database="myntra_data_analysis"
    )
    cursor = connection.cursor()

    for _, row in data.iterrows():
        # Use INSERT IGNORE to avoid duplicate entry errors
        sql = f"INSERT IGNORE INTO {table_name} VALUES ({','.join(['%s'] * len(row))})"
        cursor.execute(sql, tuple(row))

    connection.commit()
    connection.close()

# Load cleaned data into MySQL tables
load_data_to_mysql(dim_products, 'dim_products')
load_data_to_mysql(dim_customers, 'dim_customers')
load_data_to_mysql(fact_orders, 'fact_orders')