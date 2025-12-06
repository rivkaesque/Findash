# Findash - Financial Dashboard in Databricks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Databricks](https://img.shields.io/badge/Databricks-Compatible-orange)](https://databricks.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PySpark](https://img.shields.io/badge/PySpark-3.0+-red.svg)](https://spark.apache.org/)

A comprehensive financial dashboard built for Databricks that provides data transformations and visualizations for financial analysis.

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Using Your Own Data](#using-your-own-data)
- [Notebook Structure](#notebook-structure)
- [Visualizations](#visualizations)
- [Advanced Features](#advanced-features)
- [Customization](#customization)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)
- [Resources](#resources)

## Overview

This project recreates spreadsheet-based financial analysis using Databricks' powerful data processing and visualization capabilities. It demonstrates how to:

- Process financial data at scale using Apache Spark
- Create interactive visualizations
- Calculate key financial metrics and KPIs
- Perform advanced analytics like growth rate calculations
- Generate reports and dashboards

## Features

### Data Processing
- **Financial Transactions**: Revenue and expense tracking
- **Data Enrichment**: Automatic date parsing and categorization
- **Aggregations**: Monthly, yearly, and category-based summaries

### Visualizations
- **Revenue vs Expenses**: Time-series trends
- **Profit Analysis**: Profit margins and net income
- **Category Breakdown**: Revenue and expense distributions
- **Year-over-Year Comparison**: Annual performance metrics
- **Growth Metrics**: Month-over-month and year-over-year growth rates

### Key Performance Indicators (KPIs)
- Total Revenue and Expenses
- Net Profit and Profit Margin
- Average Monthly Revenue/Expenses
- Revenue Growth Rate
- Category Performance

## Getting Started

### Prerequisites
- Access to a Databricks workspace (AWS, Azure, or GCP)
- Basic understanding of Python and SQL

### Installation

1. **Upload the Notebook**
   - Log in to your Databricks workspace
   - Navigate to the Workspace section
   - Click "Import" and select the `financial_dashboard.py` file
   - The notebook will be imported and ready to use

2. **Run the Notebook**
   - Open the imported notebook
   - Attach it to a cluster
   - Run all cells sequentially

### Using Your Own Data

To use this dashboard with your own financial data:

1. **Prepare your data** in one of these formats:
   - CSV files in cloud storage (S3, Azure Blob, GCS)
   - Delta Lake tables
   - Database connections (JDBC)

2. **Modify the data loading section** (Cell 2):
   ```python
   # Replace the generate_financial_data() function with:
   df_transactions = spark.read.format("csv") \
       .option("header", "true") \
       .option("inferSchema", "true") \
       .load("path/to/your/data.csv")
   ```

3. **Ensure your data has these columns**:
   - `date`: Transaction date
   - `category`: Transaction category
   - `type`: "Revenue" or "Expense"
   - `amount`: Transaction amount

## Notebook Structure

The notebook is organized into the following sections:

1. **Setup and Data Generation**: Initialize Spark and create sample data
2. **Data Transformations**: Enrich data with calculated fields
3. **Monthly Summary**: Aggregate financial metrics by month
4. **Visualizations**: Various charts and graphs
5. **KPI Dashboard**: Key performance indicators
6. **Advanced Analytics**: Growth rates and trend analysis
7. **Data Export**: Save processed data to Delta Lake

## Visualizations

The notebook includes built-in Databricks visualizations that can be customized:

- **Line Charts**: For trend analysis over time
- **Bar Charts**: For category comparisons
- **Pie Charts**: For distribution analysis
- **Tables**: For detailed data views

To customize visualizations:
1. Click on the chart icon below any `display()` command
2. Select chart type and configure axes
3. Customize colors, labels, and formatting

## Advanced Features

### Delta Lake Integration
Save your processed data to Delta Lake for:
- ACID transactions
- Time travel (data versioning)
- Schema evolution
- Efficient upserts

### SQL Analytics
Query the data using Databricks SQL:
```sql
SELECT * FROM financial_monthly_summary
WHERE year = 2024 AND net_profit > 0
ORDER BY month
```

### Dashboard Creation
Create interactive dashboards:
1. Use the queries from the notebook
2. Create visualizations in Databricks SQL
3. Combine them into a dashboard
4. Schedule automatic refreshes

## Customization

### Adding New Categories
Modify the `revenue_categories` and `expense_categories` lists in the data generation function.

### Changing Date Ranges
Update the `start_date` and `end_date` variables to analyze different time periods.

### Adding New Metrics
Add custom calculations in the transformation sections using PySpark SQL functions.

## Best Practices

1. **Data Quality**: Validate your data before analysis
2. **Performance**: Use `.cache()` for frequently accessed DataFrames
3. **Security**: Use Databricks secrets for sensitive information
4. **Governance**: Leverage Unity Catalog for data governance
5. **Collaboration**: Share notebooks with team members

## Troubleshooting

### Common Issues

**Issue**: "Cluster not available"
- **Solution**: Attach the notebook to a running cluster or start a new one

**Issue**: "Out of memory errors"
- **Solution**: Use a larger cluster or optimize your queries with `.cache()` and partitioning

**Issue**: "Visualization not displaying"
- **Solution**: Ensure `display()` function is used and data is in the correct format

## Documentation

This project includes comprehensive documentation:

| Document | Description | Lines |
|----------|-------------|-------|
| [README.md](README.md) | Project overview and quick start | 200+ |
| [SETUP_GUIDE.md](SETUP_GUIDE.md) | Detailed installation and setup | 160+ |
| [METRICS_GUIDE.md](METRICS_GUIDE.md) | Financial metrics explained | 330+ |
| [EXAMPLES.md](EXAMPLES.md) | 10 real-world use cases | 400+ |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Quick command reference | 245+ |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Architecture details | 330+ |
| [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) | Complete project summary | 340+ |

**Total Documentation**: 2,000+ lines covering all aspects of the project.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open source and available under the MIT License.

## Support

For questions or issues:
- Check the Databricks documentation: https://docs.databricks.com
- Review Apache Spark documentation: https://spark.apache.org/docs/latest/
- Open an issue in this repository

## Resources

- [Databricks Documentation](https://docs.databricks.com/)
- [PySpark SQL Functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html)
- [Delta Lake Guide](https://docs.delta.io/latest/index.html)
- [Databricks Visualizations](https://docs.databricks.com/visualizations/index.html)