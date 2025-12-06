# Quick Reference Guide

## Quick Start

### 1. Import to Databricks
```
Workspace → Import → Git → https://github.com/rivkaesque/Findash
```

### 2. Open Notebook
```
Open: financial_dashboard.py
```

### 3. Run
```
Attach to cluster → Run All
```

---

## Key Sections

| Section | Purpose | Use When |
|---------|---------|----------|
| 2 | Data Generation | Setting up demo data |
| 3 | Transformations | Processing your data |
| 4 | Monthly Summary | Reviewing trends |
| 5 | Visualizations | Creating charts |
| 6 | KPIs | Dashboard overview |
| 7 | Advanced Analytics | Deep analysis |

---

## Common Tasks

### Load Your Own Data
Replace section 2 with:
```python
df_transactions = spark.read.format("csv") \
    .option("header", "true") \
    .load("/path/to/your/data.csv")
```

### Export Results
```python
df_monthly_summary.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("financial_summary")
```

### Filter Data
```python
df_2024 = df_enriched.filter(col('year') == 2024)
```

### Custom Aggregation
```python
df_custom = df_enriched \
    .groupBy('category') \
    .agg(spark_sum('amount').alias('total'))
```

---

## Visualization Shortcuts

### After `display()`:
1. Click chart icon
2. Select type: Line / Bar / Pie
3. Set Keys (X-axis)
4. Set Values (Y-axis)
5. Add Series groupings if needed

### Chart Types:
- **Line**: Trends over time
- **Bar**: Category comparisons
- **Pie**: Distributions
- **Table**: Detailed data

---

## Key Metrics Formulas

```python
# Profit Margin
(Net Profit / Total Revenue) × 100

# Growth Rate
((Current - Previous) / Previous) × 100

# Average
Total / Count
```

---

## PySpark Common Functions

```python
# Filtering
.filter(col('type') == 'Revenue')

# Aggregation
.groupBy('category').agg(spark_sum('amount'))

# Sorting
.orderBy(col('amount').desc())

# Calculations
.withColumn('new_col', col('old_col') * 2)

# Conditional
when(col('x') > 0, 'Positive').otherwise('Negative')
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Cluster not attached | Click "Connect" and select cluster |
| Cell won't run | Check previous cells ran first |
| Visualization blank | Verify data exists with `display()` |
| Out of memory | Use larger cluster or add `.cache()` |
| Import error | Libraries pre-installed in Databricks |

---

## File Structure

```
Findash/
├── financial_dashboard.py    # Main notebook
├── sample_data.csv           # Test data
├── README.md                 # Overview
├── SETUP_GUIDE.md           # Detailed setup
├── METRICS_GUIDE.md         # Metrics explained
├── EXAMPLES.md              # Use cases
└── requirements.txt         # Dependencies
```

---

## Useful Links

- [Full Documentation](README.md)
- [Setup Instructions](SETUP_GUIDE.md)
- [Metrics Explained](METRICS_GUIDE.md)
- [Use Cases](EXAMPLES.md)

---

## Quick Commands

### Git Clone
```bash
git clone https://github.com/rivkaesque/Findash.git
```

### Check Data
```python
df_transactions.show(10)
df_transactions.count()
df_transactions.printSchema()
```

### Save Checkpoint
```python
df_enriched.cache()
```

### Clear Cache
```python
df_enriched.unpersist()
```

---

## Dashboard Checklist

- [ ] Data loaded
- [ ] Transformations applied
- [ ] Monthly summary reviewed
- [ ] Visualizations created
- [ ] KPIs calculated
- [ ] Growth analyzed
- [ ] Results exported
- [ ] Dashboard shared

---

## Keyboard Shortcuts (Databricks)

| Action | Shortcut |
|--------|----------|
| Run cell | Shift + Enter |
| Add cell below | B |
| Delete cell | D + D |
| Undo | Ctrl/Cmd + Z |
| Save | Ctrl/Cmd + S |
| Command palette | Ctrl/Cmd + Shift + P |

---

## Data Schema Required

```
date      : Date     (YYYY-MM-DD)
category  : String   (Product Sales, Marketing, etc.)
type      : String   (Revenue or Expense)
amount    : Double   (Positive number)
```

---

## Best Practices

✅ **Do:**
- Cache frequently used DataFrames
- Use meaningful column names
- Add comments to complex logic
- Test with small data first
- Schedule regular updates

❌ **Don't:**
- Run large queries without testing
- Mix different date formats
- Use negative amounts for expenses
- Forget to attach to cluster
- Commit sensitive data

---

## Support

- Issues: [GitHub Issues](https://github.com/rivkaesque/Findash/issues)
- Databricks Docs: [docs.databricks.com](https://docs.databricks.com)
- PySpark API: [spark.apache.org](https://spark.apache.org/docs/latest/api/python/)

---

**Last Updated**: December 2024
**Version**: 1.0.0
