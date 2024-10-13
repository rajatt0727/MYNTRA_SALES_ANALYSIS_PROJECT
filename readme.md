# **Myntra Sales Analysis Power BI Dashboard**

## **Project Overview**
The **Myntra Sales Analysis Project** aims to explore, analyze, and visualize the sales, customer distribution, and product performance data of Myntra, using a Power BI dashboard. The goal of the project is to provide meaningful insights into sales trends, customer demographics, and product performance to assist in strategic business decision-making.

This README outlines the steps taken in the project, tools used, and key insights derived from the analysis.

---

## **Objectives**
- To analyze **sales performance** by product category and individual products.
- To understand **monthly sales trends** and identify any seasonal patterns.
- To analyze **customer distribution** across different geographical regions.
- To assess the impact of **discounts** on sales and revenue.
- To create an **interactive Power BI dashboard** that provides business insights and aids decision-making.

---

## **Tools Used**
- **Python**: For data cleaning, preprocessing, and initial aggregation of sales data.
- **SQL**: To create and manage the database of products, customers, and orders.
- **Power BI**: For data visualization, dashboard creation, and final analysis.

---

## **Data Used**

### 1. **cleaned_fact_orders.csv**:
   - Contains detailed order data, including:
     - Order ID
     - Customer ID
     - Product ID
     - Order Date
     - Original Price
     - Discount Percent

### 2. **monthly_sales.csv**:
   - Aggregated data showing total sales by month.
   - Columns:
     - Order Date (monthly aggregation)
     - Total Sales (Original Price)

### 3. **sales_by_category.csv**:
   - Data showing total sales by Product ID (and optionally Product Category if merged).
   - Columns:
     - Product ID
     - Total Sales (Original Price)

---

## **Data Cleaning and Preprocessing**

Before analyzing the data in Power BI, the following cleaning and transformation steps were conducted using Python:

1. **Handled missing data**:
   - Missing values in key columns were dropped.
   
2. **Removed duplicates**:
   - Ensured no duplicate records existed in the data to maintain accuracy.
   
3. **Date formatting**:
   - Converted `Order_Date` fields to datetime format for easier time-series analysis.

4. **Aggregated data**:
   - Monthly sales data and sales by product were aggregated to create summary views for easier visualization in Power BI.

---

## **Power BI Dashboard**

The Power BI dashboard consists of multiple interactive visuals that allow users to explore sales, product performance, and customer distribution. The following are the key components of the dashboard:

### 1. **Bar Chart: Sales by Product ID**
   - **Purpose**: Displays the total sales for each product.
   - **Insights**: Helps identify which products are generating the highest revenue and which may require further attention.

### 2. **Line Chart: Monthly Sales Trends**
   - **Purpose**: Visualizes the monthly sales trends over time.
   - **Insights**: Highlights seasonal peaks and troughs in sales performance, helping to identify patterns such as promotional impacts or seasonal demand.

### 3. **Map: Customer Distribution by State**
   - **Purpose**: Shows the geographical distribution of customers based on their state.
   - **Insights**: Reveals the areas with the highest customer engagement, allowing for region-specific marketing strategies and product focus.

### 4. **Card Visuals: Key Metrics**
   - **Purpose**: Displays key business metrics like:
     - **Total Sales**
     - **Total Customers**
     - **Average Discount Percent**
   - **Insights**: Provides an at-a-glance view of important performance indicators.

### 5. **Slicers: Interactive Filters**
   - **Purpose**: Allows users to filter the entire dashboard by:
     - Date (Year, Month)
     - Product Category (if merged with category data)
   - **Insights**: Enables interactive exploration of the data, allowing for focused analysis on specific products, time periods, or regions.

---

## **Key Insights**

### **A. Product Sales Analysis**
- **Top-Performing Products**: Product IDs `P001`, `P002`, and `P003` were the highest contributors to total sales.
- **Sales by Category**: (If product categories were used) Women's footwear and topwear categories generated the majority of sales.

### **B. Sales Trends**
- **Seasonal Peaks**: The months of November and December showed significant increases in sales, possibly due to festive sales or promotions.
- **Sales Decline**: Sales dipped during mid-year months like July and August, highlighting a potential opportunity for mid-year promotions.

### **C. Customer Distribution**
- **Geographical Insights**: Most customers are concentrated in states like **Maharashtra**, **Delhi**, and **Karnataka**, while some regions like **North-East India** have lower customer engagement.
- **Recommendations**: Consider targeting underperforming regions with marketing campaigns or product launches.

### **D. Discount Analysis**
- **Impact of Discounts**: Products with higher discounts showed a marked increase in sales, but profitability might need to be reviewed. Consider balancing discount strategies to maintain profit margins.

---

## **Recommendations**

1. **Stock Management**:
   - Increase stock for top-selling products and categories based on sales data.
   - Consider phasing out or re-marketing low-performing products to improve profitability.

2. **Targeted Marketing**:
   - Focus marketing efforts in high-customer regions like Maharashtra and Karnataka to drive even more engagement.
   - Run specific promotions or campaigns in regions with low engagement to attract new customers.

3. **Seasonal Promotions**:
   - Leverage high-performing months (November, December) with special promotions to maximize sales during peak demand periods.
   - Use slow months (like July and August) to create demand with targeted discounts or new product launches.

4. **Discount Strategy**:
   - Review discount levels to ensure they’re driving sufficient sales to justify reduced profit margins. Consider offering targeted discounts to specific customer segments to maintain profitability.

---

## **Project Conclusion**

The **Myntra Sales Analysis Power BI Dashboard** successfully provides a detailed overview of sales performance, product demand, and customer behavior. The insights derived from this project can help Myntra make data-driven decisions for inventory management, marketing strategies, and discount policies. By leveraging the interactive features of Power BI, stakeholders can explore the data further and uncover deeper insights that guide future business strategies.

---

## **How to Use the Dashboard**

1. **Open the Power BI Dashboard**: The `.pbix` file contains all the data visualizations and insights.
2. **Interact with the Filters**: Use slicers to explore data by date or product category.
3. **View Key Metrics**: At the top of the dashboard, key metrics like total sales, customers, and discounts are provided for easy reference.

---

## **Future Improvements**

- **Predictive Modeling**: Incorporating machine learning models to predict future sales trends based on past data.
- **Real-Time Data**: Connecting the Power BI dashboard to live data sources for real-time analysis and decision-making.
- **Customer Segmentation**: Using clustering techniques to segment customers based on behavior and purchasing patterns for more personalized marketing.

