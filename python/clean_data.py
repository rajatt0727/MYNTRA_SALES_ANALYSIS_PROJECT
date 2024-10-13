import pandas as pd

# Load the data
fact_orders = pd.read_excel(r'E:\myntra_data_analysis\data\Myntra dataset.xlsx', sheet_name='fact_orders')
dim_products = pd.read_excel(r'E:\myntra_data_analysis\data\Myntra dataset.xlsx', sheet_name='dim_products ')
dim_customers = pd.read_excel(r'E:\myntra_data_analysis\data\Myntra dataset.xlsx', sheet_name='dim_customers')

# Clean fact_orders data
fact_orders.dropna(inplace=True)  # Remove missing values
fact_orders.drop_duplicates(inplace=True)  # Remove duplicate rows
fact_orders['Date'] = pd.to_datetime(fact_orders['Date'])  # Convert 'Date' to datetime format

# Clean dim_products data
dim_products.dropna(inplace=True)  # Remove missing values
dim_products.drop_duplicates(inplace=True)  # Remove duplicate rows
dim_products['Size'].fillna(0, inplace=True)  # Replace NaN with 0 in 'Size' column if needed

# Clean dim_customers data
dim_customers.dropna(inplace=True)  # Remove missing values
dim_customers.drop_duplicates(inplace=True)  # Remove duplicate rows

# Save cleaned data to CSV files for Power BI usage
fact_orders.to_csv(r'E:\myntra_data_analysis\data\fact_orders_clean.csv', index=False)
dim_products.to_csv(r'E:\myntra_data_analysis\data\dim_products_clean.csv', index=False)
dim_customers.to_csv(r'E:\myntra_data_analysis\data\dim_customers_clean.csv', index=False)#
