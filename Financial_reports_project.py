import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charge the data bases into the data frames

file1 = r'C:\Users\acanolop\Desktop\Python development\python databases\self development projects\Balance_Sheet.xlsx'
df_balance_sheet = pd.read_excel(file1, index_col=0, engine='openpyxl')

file2 = r'C:\Users\acanolop\Desktop\Python development\python databases\self development projects\Income_Statement.xlsx'
df_income_statement = pd.read_excel(file2, index_col=0,  engine='openpyxl')

# Merging the balance sheet and income statement using two key columns stored as merged_FR
merged_FR = pd.merge(df_balance_sheet, df_income_statement, on=["Year", "company", "comp_type"], suffixes=('_BS', '_IS'))
#print(merged_FR.head())


line_plot = sns.lineplot(data=merged_FR, x="Year", y="Operating Income", hue="comp_type")
line_plot.set_title("Operating Income along the years")
plt.show()

# 1. Computing Financial Ratios
#Calculating the leverage ratio: measure the level that the company has regarding the cuantity of assets taking into account the equity leverage, if the result is close to zero it means the company is financing with the equity resourses, to keep their economical activity. 
merged_FR["leverage_ratio"] = merged_FR["Total Assets"] / merged_FR["Total Stockholder Equity"]

lever_type_ratios = merged_FR.pivot_table(index="comp_type", values="leverage_ratio")
#lever_type_ratios.get(key=)
print(lever_type_ratios)
highest_leverage = lever_type_ratios.max()
#print("The company type industry with the highest leverage ratio is: ")    
print("with a ratio by:", highest_leverage)

#Calculating the current ratio: measure the capacity the company has to face the current debts in a shot time period (< 1 year) taking into account the current assets, if the result is close to zero it means the company does not have the enough capacity to financing the current. 
merged_FR["current_ratio"] = merged_FR["Total Current Assets"] / merged_FR["Total Current Liabilities"]
merged_FR.pivot_table(index="comp_type", values="current_ratio")

#Calculating average debt-to-equity ratio: measure the level that the company has to finance its debts, taking into account the equity capital, if the result is close to zero it means the company face its debts with the equity resourses.  
merged_FR["debt_to_equity"] = merged_FR["Total Liab"] / merged_FR["Total Stockholder Equity"]
merged_FR.pivot_table(index="comp_type", values="debt_to_equity")

# 2. Computing Profitability ratios: How company can generate profits from its revenue
#Gross margin: measure the percentage of revenue after covering the direct cost associated with the producing or delivering products and services, if the percentage is high it means the comany is having good revenue results.
merged_FR["gross_margin"] =  (merged_FR["Total Revenue"] - merged_FR["Cost Of Goods Sold"])/merged_FR["Total Revenue"]
merged_FR.pivot_table(index="comp_type", values="gross_margin")

#Operating margin: measure the percentage of revenue after covering all the operating expenses, excluding interest and taxes, if the percentage is high it means the comany is having good revenue results, after handling the operational expenses and costs. 
merged_FR["profitability_ratio"] = (merged_FR["Total Revenue"] - merged_FR["Total Operating Expenses"])/merged_FR["Total Revenue"]

profit_type_ratios = merged_FR.pivot_table(index="comp_type", values="profitability_ratio")
print(profit_type_ratios)
lowest_profitability = profit_type_ratios.min()
print("The company type with the lowest profitability ratio is:", lowest_profitability)

# creating figure and axes for the subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

#Find the relationship between leverage and profitability ratios in real state key industry+
df_ratios = merged_FR[merged_FR["comp_type"] == "real_est"] 
sns.regplot(data=df_ratios, x="leverage_ratio", y="profitability_ratio", ax=axes[0, 0])

#Heat map to identify the relationship between ratios in real state
real_est_corr = df_ratios[["gross_margin", "profitability_ratio", 
                           "debt_to_equity", "current_ratio"]
                         ].corr()

sns.heatmap(real_est_corr, ax=axes[0, 1])

#Let's visualize leverage and profitability ratio by company in the tech industry
a = merged_FR[merged_FR["comp_type"] == "tech"]
b = a.pivot_table(index="company", values="leverage_ratio").reset_index() 
sns.barplot(data=b, x="company", y="leverage_ratio", ax=axes[1, 0])

c = a.pivot_table(index="company", values="profitability_ratio").reset_index() 
sns.barplot(data=c, x="company", y="profitability_ratio", ax=axes[1, 1])

#add titles and labels to the subplots
axes[0, 0].set_title('Leverage vs Profitability ratios')
axes[0, 1].set_title('correlationship between ratios')
axes[1, 0].set_title('Leverage Ratio in Tech industry')
axes[1, 1].set_title('Profitability Ratio in Tech industry')

#adjust spaces between subplots
plt.tight_layout()

plt.show()