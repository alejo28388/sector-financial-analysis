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



