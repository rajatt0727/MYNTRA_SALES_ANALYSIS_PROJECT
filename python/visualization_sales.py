# File: python_scripts/visualize_sales.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
fact_orders = pd.read_csv(r'E:\myntra_data_analysis\data\fact_orders_clean.csv')

# Sales Trends Over Time
sales_over_time = fact_orders.groupby(pd.to_datetime(fact_orders['Date']).dt.to_period('M')).agg({
    'Original Price': 'sum'
}).reset_index()

# Plot the sales trends
plt.figure(figsize=(10, 6))
plt.plot(sales_over_time['Date'].astype(str), sales_over_time['Original Price'])
plt.title('Sales Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()