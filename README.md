# 📊 Sector-Based Financial Analysis in the U.S.

This project analyzes financial statements from leading U.S. companies in the **Real Estate 🏘️, Technology 💻, and Consumer Goods 🛍️** sectors to evaluate **debt capacity** and **profitability** using Python and Pandas.

It provides visual insights, financial ratios, and sectoral trends based on historical balance sheets and income statements.

---

## 🚀 Key Features

- Load and merge balance sheets and income statements
- Compute financial ratios (debt-to-equity, profitability, etc.)
- Aggregate and compare metrics by sector
- Visualize trends and relationships across sectors and companies
- Focus on top tech firms: Apple, Amazon, Google, Meta, Microsoft

---

## 🧠 How it Works

```python
# Load Excel files and convert to data frames
file1 = r'C:\Users\acanolop\Desktop\Python development\python databases\self development projects\Balance_Sheet.xlsx'
df_balance_sheet = pd.read_excel(file1, index_col=0, engine='openpyxl')

file2 = r'C:\Users\acanolop\Desktop\Python development\python databases\self development projects\Income_Statement.xlsx'
df_income_statement = pd.read_excel(file2, index_col=0,  engine='openpyxl')

# Merge balance sheet and income statement
merged_FR = pd.merge(df_balance_sheet, df_income_statement, on=["Year", "company", "comp_type"], suffixes=('_BS', '_IS'))

# Calculate leverage ratio and sort company types with pivot table
merged_FR["leverage_ratio"] = merged_FR["Total Assets"] / merged_FR["Total Stockholder Equity"]
lever_type_ratios = merged_FR.pivot_table(index="comp_type", values="leverage_ratio")

# Calculate debt to equity ratio and sort company types with pivot table
merged_FR["debt_to_equity"] = merged_FR["Total Liab"] / merged_FR["Total Stockholder Equity"]
merged_FR.pivot_table(index="comp_type", values="debt_to_equity")

# Calculate profitability ratio and sort company types with pivot table
merged_FR["profitability_ratio"] = (merged_FR["Total Revenue"] - merged_FR["Total Operating Expenses"])/merged_FR["Total Revenue"]
profit_type_ratios = merged_FR.pivot_table(index="comp_type", values="profitability_ratio")

---

# 📊 Visualizations

### 1. Revenue Over Time by Sector
# Shows the trend in operating revenue across Real Estate, Technology, and Consumer Goods.

line_plot = sns.lineplot(data=merged_FR, x="Year", y="Operating Income", hue="comp_type")
line_plot.set_title("Operating Income along the years")

---

### 2. Profitability vs. Leverage Ratio
# Scatter plot to explore correlation between profitability and leverage.

df_ratios = merged_FR[merged_FR["comp_type"] == "real_est"] 
sns.regplot(data=df_ratios, x="leverage_ratio", y="profitability_ratio", ax=axes[0, 0])

---

### 3. Correlation Matrix
# Analyzes relationships between growth margin, profitability, debt, and liquidity.

real_est_corr = df_ratios[["gross_margin", "profitability_ratio", 
                           "debt_to_equity", "current_ratio"]
                         ].corr()

sns.heatmap(real_est_corr, ax=axes[0, 1])

---

### 4. Profitability of Top Tech Companies
# Comparison of Apple, Amazon, Google, Meta, Microsoft.

a = merged_FR[merged_FR["comp_type"] == "tech"]
c = a.pivot_table(index="company", values="profitability_ratio").reset_index() 
sns.barplot(data=c, x="company", y="profitability_ratio", ax=axes[1, 1])

---

### 5. Leverage Capacity of Top Tech Companies
# Shows debt-to-equity ratio across leading tech companies.

a = merged_FR[merged_FR["comp_type"] == "tech"]
b = a.pivot_table(index="company", values="leverage_ratio").reset_index() 
sns.barplot(data=b, x="company", y="leverage_ratio", ax=axes[1, 0])


