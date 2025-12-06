# Databricks notebook source
# MAGIC %md
# MAGIC # Financial Dashboard
# MAGIC 
# MAGIC This notebook recreates a financial dashboard with data transformations and visualizations using Databricks.
# MAGIC 
# MAGIC ## Features:
# MAGIC - Revenue and expense tracking
# MAGIC - Profit/loss calculations
# MAGIC - Monthly trends
# MAGIC - Category breakdowns
# MAGIC - Year-over-year comparisons

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Setup and Data Generation

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, avg, month, year, round as spark_round, lit, when
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType
import datetime
from datetime import datetime, timedelta
import random

# Initialize Spark session (already available in Databricks)
spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Create Sample Financial Data

# COMMAND ----------

# Generate sample financial data
def generate_financial_data():
    """Generate sample financial transactions for demonstration"""
    
    # Categories for revenue and expenses
    revenue_categories = ['Product Sales', 'Service Revenue', 'Consulting', 'Subscriptions']
    expense_categories = ['Salaries', 'Marketing', 'Office Rent', 'Utilities', 'Software', 'Travel']
    
    data = []
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    # Generate monthly transactions
    current_date = start_date
    while current_date <= end_date:
        # Revenue transactions
        for category in revenue_categories:
            amount = random.uniform(10000, 50000)
            data.append({
                'date': current_date,
                'category': category,
                'type': 'Revenue',
                'amount': round(amount, 2)
            })
        
        # Expense transactions
        for category in expense_categories:
            amount = random.uniform(2000, 15000)
            data.append({
                'date': current_date,
                'category': category,
                'type': 'Expense',
                'amount': round(amount, 2)
            })
        
        # Move to next month
        if current_date.month == 12:
            current_date = datetime(current_date.year + 1, 1, 1)
        else:
            current_date = datetime(current_date.year, current_date.month + 1, 1)
    
    return data

# Create DataFrame
financial_data = generate_financial_data()
df_transactions = spark.createDataFrame(financial_data)

# Display sample data
display(df_transactions.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Data Transformations

# COMMAND ----------

# Add year and month columns for easier analysis
df_enriched = df_transactions \
    .withColumn('year', year(col('date'))) \
    .withColumn('month', month(col('date'))) \
    .withColumn('amount_signed', 
                when(col('type') == 'Revenue', col('amount'))
                .otherwise(-col('amount')))

# Cache the enriched dataframe for better performance
df_enriched.cache()

display(df_enriched.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Monthly Summary

# COMMAND ----------

# Calculate monthly revenue, expenses, and profit
df_monthly_summary = df_enriched \
    .groupBy('year', 'month') \
    .agg(
        spark_sum(when(col('type') == 'Revenue', col('amount')).otherwise(0)).alias('total_revenue'),
        spark_sum(when(col('type') == 'Expense', col('amount')).otherwise(0)).alias('total_expenses'),
        spark_sum(col('amount_signed')).alias('net_profit')
    ) \
    .orderBy('year', 'month')

# Display monthly summary
display(df_monthly_summary)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Visualizations

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5.1 Revenue vs Expenses Over Time

# COMMAND ----------

# Monthly trend visualization
display(df_monthly_summary)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5.2 Profit Margin Analysis

# COMMAND ----------

# Calculate profit margin
df_profit_margin = df_monthly_summary \
    .withColumn('profit_margin_pct', 
                spark_round((col('net_profit') / col('total_revenue')) * 100, 2))

display(df_profit_margin)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5.3 Category Breakdown

# COMMAND ----------

# Revenue by category
df_revenue_by_category = df_enriched \
    .filter(col('type') == 'Revenue') \
    .groupBy('category') \
    .agg(spark_sum('amount').alias('total_amount')) \
    .orderBy(col('total_amount').desc())

display(df_revenue_by_category)

# COMMAND ----------

# Expense by category
df_expense_by_category = df_enriched \
    .filter(col('type') == 'Expense') \
    .groupBy('category') \
    .agg(spark_sum('amount').alias('total_amount')) \
    .orderBy(col('total_amount').desc())

display(df_expense_by_category)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5.4 Year-over-Year Comparison

# COMMAND ----------

# Yearly summary
df_yearly_summary = df_enriched \
    .groupBy('year') \
    .agg(
        spark_sum(when(col('type') == 'Revenue', col('amount')).otherwise(0)).alias('total_revenue'),
        spark_sum(when(col('type') == 'Expense', col('amount')).otherwise(0)).alias('total_expenses'),
        spark_sum(col('amount_signed')).alias('net_profit')
    ) \
    .orderBy('year')

display(df_yearly_summary)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Key Performance Indicators (KPIs)

# COMMAND ----------

# Calculate overall KPIs
total_revenue = df_enriched.filter(col('type') == 'Revenue').agg(spark_sum('amount')).collect()[0][0]
total_expenses = df_enriched.filter(col('type') == 'Expense').agg(spark_sum('amount')).collect()[0][0]
net_profit = total_revenue - total_expenses
avg_monthly_revenue = total_revenue / 24  # 24 months of data
avg_monthly_expenses = total_expenses / 24

# Create KPI summary
kpi_data = [
    {'metric': 'Total Revenue', 'value': round(total_revenue, 2)},
    {'metric': 'Total Expenses', 'value': round(total_expenses, 2)},
    {'metric': 'Net Profit', 'value': round(net_profit, 2)},
    {'metric': 'Profit Margin %', 'value': round((net_profit / total_revenue) * 100, 2)},
    {'metric': 'Avg Monthly Revenue', 'value': round(avg_monthly_revenue, 2)},
    {'metric': 'Avg Monthly Expenses', 'value': round(avg_monthly_expenses, 2)}
]

df_kpi = spark.createDataFrame(kpi_data)
display(df_kpi)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Advanced Analytics

# COMMAND ----------

# MAGIC %md
# MAGIC ### 7.1 Monthly Growth Rate

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import lag

# Calculate month-over-month growth
window_spec = Window.orderBy('year', 'month')

df_growth = df_monthly_summary \
    .withColumn('prev_revenue', lag('total_revenue').over(window_spec)) \
    .withColumn('revenue_growth_pct', 
                spark_round(((col('total_revenue') - col('prev_revenue')) / col('prev_revenue')) * 100, 2)) \
    .filter(col('prev_revenue').isNotNull())

display(df_growth)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 7.2 Top Revenue Categories

# COMMAND ----------

# Show top revenue generating categories with percentages
df_revenue_breakdown = df_enriched \
    .filter(col('type') == 'Revenue') \
    .groupBy('category') \
    .agg(spark_sum('amount').alias('total_amount'))

total_rev = df_revenue_breakdown.agg(spark_sum('total_amount')).collect()[0][0]

df_revenue_pct = df_revenue_breakdown \
    .withColumn('percentage', spark_round((col('total_amount') / lit(total_rev)) * 100, 2)) \
    .orderBy(col('total_amount').desc())

display(df_revenue_pct)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. Export Data

# COMMAND ----------

# MAGIC %md
# MAGIC You can save the processed data to Delta Lake tables for further analysis:
# MAGIC 
# MAGIC ```python
# MAGIC # Save to Delta Lake
# MAGIC df_monthly_summary.write.format("delta").mode("overwrite").saveAsTable("financial_monthly_summary")
# MAGIC df_revenue_by_category.write.format("delta").mode("overwrite").saveAsTable("financial_revenue_by_category")
# MAGIC df_expense_by_category.write.format("delta").mode("overwrite").saveAsTable("financial_expense_by_category")
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC 
# MAGIC This notebook provides:
# MAGIC 1. **Data Generation**: Sample financial data with revenues and expenses
# MAGIC 2. **Transformations**: Monthly aggregations, profit calculations, and growth metrics
# MAGIC 3. **Visualizations**: 
# MAGIC    - Revenue vs Expenses trends
# MAGIC    - Profit margin analysis
# MAGIC    - Category breakdowns
# MAGIC    - Year-over-year comparisons
# MAGIC 4. **KPIs**: Key business metrics
# MAGIC 5. **Advanced Analytics**: Growth rates and percentage breakdowns
# MAGIC 
# MAGIC To use this notebook:
# MAGIC 1. Upload it to your Databricks workspace
# MAGIC 2. Run each cell sequentially
# MAGIC 3. Use the built-in visualization tools to customize charts
# MAGIC 4. Replace the sample data with your actual financial data
