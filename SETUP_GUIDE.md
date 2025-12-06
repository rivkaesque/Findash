# Databricks Notebook Quick Start Guide

## Option 1: Import Directly from Git (Recommended)

1. **Log in to Databricks**
   - Navigate to your Databricks workspace
   - Go to the "Workspace" section

2. **Import from Git**
   - Click on your username or a folder
   - Right-click and select "Create" → "Repo"
   - Enter the Git URL: `https://github.com/rivkaesque/Findash`
   - Click "Create Repo"

3. **Open the Notebook**
   - Navigate to the imported repo
   - Open `financial_dashboard.py`

4. **Attach to Cluster**
   - Click "Connect" at the top
   - Select an existing cluster or create a new one
   - Recommended: Use Databricks Runtime 12.0 or later

5. **Run**
   - Click "Run All" or execute cells individually

## Option 2: Manual Upload

1. **Download the Notebook**
   - Clone this repository or download `financial_dashboard.py`

2. **Import to Databricks**
   - In Databricks workspace, click "Workspace"
   - Navigate to your desired folder
   - Click "Import"
   - Select "File" and upload `financial_dashboard.py`
   - Click "Import"

3. **Run the Notebook**
   - Open the imported notebook
   - Attach to a cluster
   - Run cells sequentially

## Cluster Configuration

### Recommended Settings for Demo/Testing:
- **Databricks Runtime**: 12.0 LTS or later
- **Node Type**: Standard_DS3_v2 (Azure) or m5.xlarge (AWS)
- **Workers**: 2-4 workers for small datasets
- **Autoscaling**: Enable for production use

### For Production:
- Use larger node types based on data volume
- Enable autoscaling (2-10 workers)
- Consider using photon acceleration
- Set up automatic cluster termination

## Connecting to Your Data

### From CSV Files:
```python
df_transactions = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/path/to/your/file.csv")
```

### From Delta Lake:
```python
df_transactions = spark.read.format("delta") \
    .load("/path/to/delta/table")
```

### From Database:
```python
df_transactions = spark.read.format("jdbc") \
    .option("url", "jdbc:postgresql://host:port/database") \
    .option("dbtable", "financial_transactions") \
    .option("user", "username") \
    .option("password", dbutils.secrets.get("scope", "key")) \
    .load()
```

## Data Schema

Your data should match this schema:

| Column   | Type   | Description                    | Example        |
|----------|--------|--------------------------------|----------------|
| date     | Date   | Transaction date               | 2024-01-15     |
| category | String | Transaction category           | Product Sales  |
| type     | String | "Revenue" or "Expense"         | Revenue        |
| amount   | Double | Transaction amount (positive)  | 15000.50       |

## Customizing Visualizations

1. **Run a cell with `display()` command**
2. **Click the chart icon** below the output
3. **Select visualization type**: Bar, Line, Pie, Table, etc.
4. **Configure**:
   - Keys: X-axis values
   - Values: Y-axis values
   - Series groupings: For multiple lines/bars
   - Aggregations: Sum, Average, Count, etc.

## Creating Dashboards

1. **In the notebook**: Click "View" → "Create Dashboard"
2. **In Databricks SQL**:
   - Convert notebook cells to SQL queries
   - Create visualizations
   - Combine into a dashboard
   - Set refresh schedule

## Scheduling the Notebook

1. **Create a Job**:
   - Click "Workflows" in sidebar
   - Click "Create Job"
   - Select "Notebook" task
   - Choose your notebook

2. **Configure Schedule**:
   - Set trigger: Schedule, Continuous, or Manual
   - Configure email notifications
   - Set retry policies

3. **Run**:
   - Test with "Run Now"
   - Monitor in job runs history

## Troubleshooting

### "No cluster available"
→ Create or start a cluster, then attach the notebook

### "Library not found"
→ Libraries like PySpark are pre-installed in Databricks runtime

### "Permission denied"
→ Check folder permissions and cluster access policies

### "Out of memory"
→ Use a larger cluster or optimize data processing with caching

## Next Steps

1. **Explore the data**: Run all cells to see sample outputs
2. **Connect your data**: Replace sample data with real data sources
3. **Customize**: Modify categories, metrics, and visualizations
4. **Share**: Create dashboards and share with stakeholders
5. **Automate**: Schedule regular updates

## Additional Resources

- [Databricks Notebooks Documentation](https://docs.databricks.com/notebooks/index.html)
- [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql.html)
- [Databricks Visualizations](https://docs.databricks.com/visualizations/index.html)
- [Delta Lake Best Practices](https://docs.databricks.com/delta/best-practices.html)
