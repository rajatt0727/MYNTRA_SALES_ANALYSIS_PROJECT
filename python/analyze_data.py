# File: python_scripts/analyze_data.py
import pandas as pd

# Load the cleaned data
fact_orders = pd.read_csv(r'E:\myntra_data_analysis\data\fact_orders_clean.csv')

# Perform some analysis
# Sales Trends Over Time:
sales_over_time = fact_orders.groupby(pd.to_datetime(fact_orders['Date']).dt.to_period('M')).agg({
    'Original Price': 'sum'
}).reset_index()

# Print the sales trend data
print(sales_over_time)
