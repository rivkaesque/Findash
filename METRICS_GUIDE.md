# Financial Dashboard Metrics Guide

This document explains the metrics, calculations, and insights provided by the Databricks Financial Dashboard.

## Table of Contents
1. [Basic Metrics](#basic-metrics)
2. [Derived Metrics](#derived-metrics)
3. [Visualizations](#visualizations)
4. [How to Interpret](#how-to-interpret)

## Basic Metrics

### Revenue
**Definition**: Income generated from business operations.

**Categories in Dashboard**:
- Product Sales
- Service Revenue
- Consulting
- Subscriptions

**Calculation**: Sum of all revenue transactions
```python
total_revenue = sum(amount WHERE type = 'Revenue')
```

### Expenses
**Definition**: Costs incurred in business operations.

**Categories in Dashboard**:
- Salaries
- Marketing
- Office Rent
- Utilities
- Software
- Travel

**Calculation**: Sum of all expense transactions
```python
total_expenses = sum(amount WHERE type = 'Expense')
```

### Net Profit
**Definition**: Revenue minus expenses.

**Formula**:
```
Net Profit = Total Revenue - Total Expenses
```

**Interpretation**:
- Positive: Business is profitable
- Negative: Business is operating at a loss
- Zero: Break-even

## Derived Metrics

### Profit Margin
**Definition**: Percentage of revenue that remains as profit.

**Formula**:
```
Profit Margin % = (Net Profit / Total Revenue) × 100
```

**Interpretation**:
- 0-5%: Low margin (tight profit)
- 5-10%: Average margin
- 10-20%: Good margin
- 20%+: Excellent margin

**Industry Benchmarks**:
- Retail: 2-6%
- Software/SaaS: 15-25%
- Consulting: 10-20%
- Manufacturing: 5-10%

### Average Monthly Revenue
**Definition**: Mean revenue per month.

**Formula**:
```
Avg Monthly Revenue = Total Revenue / Number of Months
```

**Use**: Forecasting and budgeting

### Average Monthly Expenses
**Definition**: Mean expenses per month.

**Formula**:
```
Avg Monthly Expenses = Total Expenses / Number of Months
```

**Use**: Budget planning and cost control

### Month-over-Month Growth Rate
**Definition**: Percentage change from previous month.

**Formula**:
```
MoM Growth % = ((Current Month Revenue - Previous Month Revenue) / Previous Month Revenue) × 100
```

**Interpretation**:
- Positive: Growing revenue
- Negative: Declining revenue
- 0: Stagnant

**Healthy Growth Rates**:
- Startup: 15-25% monthly
- Growth stage: 5-15% monthly
- Mature: 2-5% monthly

### Year-over-Year Growth
**Definition**: Percentage change from same period last year.

**Formula**:
```
YoY Growth % = ((Current Year - Previous Year) / Previous Year) × 100
```

**Interpretation**: Better for seasonal businesses

## Visualizations

### 1. Revenue vs Expenses Over Time (Line Chart)
**Purpose**: Track financial trends

**How to Read**:
- X-axis: Time (months/quarters)
- Y-axis: Amount ($)
- Lines: Revenue (should be above) and Expenses (should be below)

**Key Insights**:
- Widening gap = Increasing profitability
- Narrowing gap = Decreasing profitability
- Crossing lines = Loss periods

### 2. Monthly Profit (Bar Chart)
**Purpose**: Identify profitable and loss-making periods

**How to Read**:
- Positive bars (green): Profitable months
- Negative bars (red): Loss months
- Height: Magnitude of profit/loss

**Action Items**:
- Investigate loss months for causes
- Replicate success patterns from high-profit months

### 3. Category Breakdown (Pie Chart)
**Purpose**: Understand revenue/expense composition

**How to Read**:
- Each slice: Category
- Slice size: Proportion of total

**Insights**:
- Revenue: Which products/services drive income
- Expenses: Where money is spent

**Red Flags**:
- Any single category > 50% of expenses
- Revenue concentrated in one category (risk)

### 4. Profit Margin Trend (Line Chart)
**Purpose**: Track profitability efficiency over time

**How to Read**:
- Y-axis: Profit margin percentage
- Trend line direction indicates improving or declining efficiency

**Target**: Aim for stable or increasing trend

### 5. Year-over-Year Comparison (Grouped Bar Chart)
**Purpose**: Compare annual performance

**How to Read**:
- Groups: Years
- Bars: Revenue, Expenses, Profit
- Height: Amount

**Analysis**:
- Compare heights across years
- Look for consistent growth patterns

## How to Interpret

### Healthy Financial Dashboard Indicators

✅ **Good Signs**:
1. Revenue growing faster than expenses
2. Positive and increasing profit margin
3. Consistent or improving MoM growth
4. Diversified revenue streams
5. Controlled expense growth
6. Positive YoY growth

❌ **Warning Signs**:
1. Expenses growing faster than revenue
2. Declining profit margins
3. Negative growth trends
4. Revenue dependent on single category
5. Unexplained expense spikes
6. Inconsistent profitability

### Monthly Review Checklist

Use this checklist when reviewing your dashboard:

- [ ] Is revenue meeting targets?
- [ ] Are expenses within budget?
- [ ] Is profit margin healthy for the industry?
- [ ] Are there any unusual spikes or drops?
- [ ] Is growth rate sustainable?
- [ ] Which categories need attention?
- [ ] Are there seasonal patterns?
- [ ] What actions are needed?

### Quarterly Analysis

Every quarter, analyze:

1. **Trend Analysis**: 
   - Are we moving in the right direction?
   - What's the growth rate?

2. **Variance Analysis**:
   - Budget vs. Actual
   - Year vs. Previous year

3. **Category Review**:
   - Top revenue generators
   - Largest expense items
   - Opportunities for optimization

4. **Forward Planning**:
   - Forecast next quarter
   - Set targets
   - Identify risks and opportunities

## Advanced Interpretations

### Cash Flow Implications
While this dashboard shows profit/loss:
- Profit ≠ Cash
- Consider: Accounts receivable, payable, inventory
- Monitor: Days Sales Outstanding (DSO)

### Breakeven Analysis
**Breakeven Point**: Revenue = Expenses

**Formula**:
```
Breakeven = Fixed Costs / (1 - (Variable Costs / Revenue))
```

Calculate to understand minimum revenue needed.

### Return on Investment (ROI)
For marketing and other investments:

**Formula**:
```
ROI % = ((Revenue from Investment - Cost of Investment) / Cost of Investment) × 100
```

### Runway Calculation
For startups with current cash:

**Formula**:
```
Runway (months) = Cash on Hand / Average Monthly Burn Rate
```

Where Burn Rate = Monthly Expenses - Monthly Revenue (if negative profit)

## Taking Action

### When Profit Margin is Low
1. Analyze expense categories
2. Identify cost-cutting opportunities
3. Review pricing strategy
4. Improve operational efficiency

### When Growth is Stagnant
1. Review marketing effectiveness
2. Explore new revenue streams
3. Analyze customer retention
4. Consider market expansion

### When Expenses are High
1. Benchmark against industry standards
2. Review vendor contracts
3. Automate processes
4. Consolidate services

## Customizing Metrics

Add custom metrics relevant to your business:

### Customer Metrics
- Customer Acquisition Cost (CAC)
- Customer Lifetime Value (CLV)
- Churn Rate

### Operational Metrics
- Revenue per Employee
- Gross Margin by Product
- Operating Expense Ratio

### Industry-Specific Metrics
- SaaS: MRR, ARR, Churn
- Retail: Inventory Turnover
- Manufacturing: Production Cost per Unit

## Resources

- [Financial Ratio Analysis](https://www.investopedia.com/financial-ratios-4689817)
- [KPI Dashboard Best Practices](https://www.klipfolio.com/resources/kpi-examples)
- [Financial Metrics Guide](https://www.wallstreetprep.com/knowledge/financial-metrics/)

---

**Note**: This dashboard provides insights based on transaction data. For complete financial analysis, integrate with:
- Balance Sheet data
- Cash Flow statements
- Budget vs. Actual reports
- Forecasting models
