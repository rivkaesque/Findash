# Example Use Cases

This document provides concrete examples of how to use the Databricks Financial Dashboard for different scenarios.

## Use Case 1: Monthly Business Review

**Scenario**: You're a business owner doing your monthly financial review.

**Steps**:
1. Open the `financial_dashboard.py` notebook in Databricks
2. Update the data source to point to your financial data
3. Run all cells to generate reports
4. Review key sections:
   - Section 4: Monthly Summary (check this month vs. last month)
   - Section 6: KPIs (overall business health)
   - Section 7.1: Growth Rate (is business growing?)

**What to Look For**:
- ✅ Revenue increasing month-over-month
- ✅ Expenses under control
- ✅ Positive profit margin
- ❌ Unexpected expense spikes
- ❌ Revenue decline

**Action Items**:
- If profit margin < 10%: Review expenses or pricing
- If growth < 0%: Analyze what changed
- If specific expense category high: Investigate and optimize

---

## Use Case 2: Year-End Financial Analysis

**Scenario**: Preparing annual reports and planning for next year.

**Steps**:
1. Load full year's data
2. Focus on Section 5.4 (Year-over-Year Comparison)
3. Review Section 7.2 (Top Revenue Categories)
4. Export processed data using Section 8

**Analysis Questions**:
- Which months were most profitable?
- What were the top revenue sources?
- Did we meet our annual targets?
- What should we budget for next year?

**Deliverables**:
- Annual revenue/expense report
- Category performance summary
- Growth trends
- Budget recommendations for next year

---

## Use Case 3: Investor Presentation

**Scenario**: Preparing financial metrics for investors.

**Key Metrics to Highlight**:
1. **Total Revenue** (Section 6 - KPIs)
2. **Net Profit** (Section 6 - KPIs)
3. **Profit Margin %** (Section 6 - KPIs)
4. **YoY Growth** (Section 5.4)
5. **Monthly Revenue Trend** (Section 5.1)

**Visualizations to Export**:
- Revenue vs Expenses line chart (shows growth trajectory)
- Year-over-Year comparison (shows scaling)
- Category breakdown (shows diversification)
- Growth rate chart (shows momentum)

**Tips**:
- Emphasize positive trends
- Explain any dips or anomalies
- Show projections based on current growth rate

---

## Use Case 4: Cost Optimization Project

**Scenario**: Need to reduce costs by 15% without impacting revenue.

**Steps**:

1. **Analyze Current Expenses**
   ```
   Run Section 5.3 - Category Breakdown
   Focus on expense categories
   ```

2. **Identify Targets**
   - Sort expenses by amount
   - Look for categories > 20% of total
   - Check for unusual increases

3. **Calculate Impact**
   ```
   For each category:
   - Current amount
   - Target reduction (15%)
   - Feasibility
   ```

4. **Monitor Results**
   - Re-run monthly
   - Track category changes
   - Measure total savings

**Example Output**:
```
Category        Current    Target     Action
Salaries        $120K      $102K      Freeze hiring
Marketing       $85K       $72K       Optimize ad spend
Office Rent     $50K       $42K       Renegotiate lease
Software        $35K       $30K       Consolidate tools
```

---

## Use Case 5: Department Budget Allocation

**Scenario**: Allocating budget across departments for next quarter.

**Steps**:

1. **Review Historical Data**
   ```
   Check Section 4 - Monthly Summary
   Calculate average monthly expenses by category
   ```

2. **Analyze Performance**
   ```
   Revenue per category: Which brings most value?
   Expense ROI: Which expenses drive revenue?
   ```

3. **Create Budget**
   ```
   Base budget: Last quarter average
   Growth factor: Expected revenue increase
   Adjustments: Strategic initiatives
   ```

4. **Set Targets**
   - Revenue targets per category
   - Expense budgets per department
   - Profit margin goals

**Budget Template**:
```
Department     Q1 Actual   Q2 Target   % Change   Justification
Marketing      $27K        $30K        +11%       New campaign
Sales          $15K        $18K        +20%       Expansion
Operations     $45K        $47K        +4%        Inflation
R&D            $20K        $25K        +25%       New product
```

---

## Use Case 6: Seasonal Business Planning

**Scenario**: You have a seasonal business (e.g., retail, tourism).

**Steps**:

1. **Identify Patterns**
   ```
   Run full-year data
   Look at Section 5.1 - Revenue over Time
   Note high and low seasons
   ```

2. **Calculate Seasonality Index**
   ```
   For each month:
   Seasonality = (Month Revenue / Average Monthly Revenue) × 100
   ```

3. **Plan Inventory and Staffing**
   ```
   High season (index > 120): Increase capacity
   Low season (index < 80): Reduce costs
   ```

4. **Forecast Next Year**
   ```
   Expected Revenue = Last Year × (1 + Growth Rate) × Seasonality Index
   ```

**Example Seasonal Pattern**:
```
Month      Revenue    Index    Action
Jan        $80K       80%      Reduce staff
Feb        $75K       75%      Minimal inventory
Mar        $95K       95%      Ramp up
Apr        $120K      120%     Peak staffing
May        $130K      130%     Maximum capacity
Jun        $125K      125%     Maintain
Jul        $110K      110%     Standard operations
Aug        $100K      100%     Average
Sep        $90K       90%      Start reduction
Oct        $85K       85%      Lower inventory
Nov        $95K       95%      Holiday prep
Dec        $150K      150%     Peak season
```

---

## Use Case 7: Profitability by Product Line

**Scenario**: Understanding which products/services are most profitable.

**Modifications Needed**:
Add 'product_line' column to your data.

**Analysis**:
```python
# In notebook, add this cell:
df_product_profitability = df_enriched \
    .groupBy('product_line') \
    .agg(
        spark_sum(when(col('type') == 'Revenue', col('amount')).otherwise(0)).alias('revenue'),
        spark_sum(when(col('type') == 'Expense', col('amount')).otherwise(0)).alias('expenses'),
        spark_sum(col('amount_signed')).alias('profit')
    ) \
    .withColumn('profit_margin', 
                spark_round((col('profit') / col('revenue')) * 100, 2)) \
    .orderBy(col('profit').desc())

display(df_product_profitability)
```

**Insights**:
- Which products are most profitable?
- Which products are loss-leaders?
- Where to focus marketing?
- What to discontinue?

---

## Use Case 8: Cash Flow Forecasting

**Scenario**: Predicting next quarter's cash position.

**Steps**:

1. **Calculate Historical Average**
   ```
   Avg Monthly Revenue
   Avg Monthly Expenses
   Avg Monthly Profit
   ```

2. **Identify Trends**
   ```
   Growth rate from Section 7.1
   Seasonal patterns
   Known upcoming changes
   ```

3. **Create Forecast**
   ```
   Month 1 = Last Month × (1 + Growth Rate) × Seasonality
   Month 2 = Month 1 × (1 + Growth Rate) × Seasonality
   Month 3 = Month 2 × (1 + Growth Rate) × Seasonality
   ```

4. **Scenario Planning**
   - Best case: +20% growth
   - Expected: Current growth rate
   - Worst case: -10% decline

**Forecast Table**:
```
Month      Best Case   Expected   Worst Case   Action Plan
Next+1     $150K       $120K      $95K         Monitor
Next+2     $165K       $126K      $90K         Alert if < $100K
Next+3     $180K       $132K      $85K         Emergency plan if < $95K
```

---

## Use Case 9: Benchmark Against Industry

**Scenario**: Comparing your metrics to industry standards.

**Your Metrics** (from Section 6):
- Profit Margin: 15%
- Growth Rate: 8% monthly
- Revenue per Category

**Industry Benchmarks** (research required):
- SaaS: 20-30% profit margin
- Retail: 2-6% profit margin
- Consulting: 10-20% profit margin

**Comparison**:
```
Metric              Your Business   Industry Avg   Status
Profit Margin       15%            12%            ✅ Above
Growth Rate         8%             5%             ✅ Above
Revenue/Employee    $120K          $150K          ⚠️ Below
Operating Expenses  65%            70%            ✅ Better
```

**Actions**:
- ✅ Maintain profit margin
- ⚠️ Improve revenue per employee (productivity)
- ✅ Keep expense control practices

---

## Use Case 10: Board Meeting Dashboard

**Scenario**: Creating an executive summary for board meeting.

**Key Slides**:

1. **Executive Summary**
   - Total Revenue: $X
   - Total Profit: $Y
   - Profit Margin: Z%
   - Status: ✅ On track / ⚠️ Needs attention

2. **Growth Metrics**
   - MoM Growth: %
   - YoY Growth: %
   - Trend: 📈 Upward / 📉 Downward

3. **Financial Health**
   - Revenue vs. Expenses chart
   - Profit trend
   - Key category performance

4. **Highlights**
   - Major wins
   - Challenges
   - Upcoming opportunities

5. **Action Items**
   - Strategic decisions needed
   - Resource allocation
   - Risk mitigation

**One-Page Summary Template**:
```
Q3 2024 Financial Summary

Revenue:        $1.2M  (+15% QoQ)
Expenses:       $950K  (+8% QoQ)
Profit:         $250K  (+45% QoQ)
Margin:         20.8%  (▲ +4.2%)

Top Categories:
✓ Product Sales:     $500K (42%)
✓ Service Revenue:   $400K (33%)
✓ Subscriptions:     $300K (25%)

Key Achievements:
• Crossed $1M revenue milestone
• Improved margin by 4 points
• Reduced marketing cost per acquisition

Focus Areas:
→ Expand sales team
→ Optimize supply chain
→ Launch new product line

Status: 🟢 On Track
```

---

## Tips for All Use Cases

### Data Quality
- Ensure consistent date formats
- Validate amounts (no negatives for revenue/expenses)
- Check for duplicate entries
- Verify category names are standardized

### Visualization Best Practices
- Use consistent colors (green for revenue, red for expenses)
- Label axes clearly
- Add titles to all charts
- Include time ranges in titles

### Sharing Results
- Export visualizations as images
- Save DataFrames to Delta tables
- Create dashboards for real-time access
- Schedule automated reports

### Regular Reviews
- Daily: Check yesterday's transactions
- Weekly: Review week's summary
- Monthly: Full dashboard analysis
- Quarterly: Strategic planning session
- Annually: Year-end review and budgeting

---

Remember: The dashboard is a tool for insights, not just data display. Always ask:
1. What story does the data tell?
2. What decisions does this inform?
3. What actions should we take?
