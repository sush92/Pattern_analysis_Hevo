import pandas as pd
import matplotlib.pyplot as plt

# Loading data from Excel sheets
path = "/Users/sushmitha/Desktop/pattern_analysis/Pattern Analysis Test.xlsx"
df = pd.read_excel(path, sheet_name='Leads - October - Sep - Aug')
url_data = pd.read_excel(path, sheet_name='Blog Data - October - Sep - Aug')

# Summarizing the data
summary = {
    "Total Leads": df.shape[0],
    "Leads by Current Status": df['Current Status'].value_counts(),
    "Leads by Type": df['Type'].value_counts(),
    "Started Free Trial": df['Started Free Trial?'].value_counts(),
    "Decision Maker": df['Decision Maker'].value_counts(),
    "Visited Pricing": df.get('Visited Pricing', pd.Series(dtype='int')).value_counts(),
    "Visited Integrations": df.get('Visited Integrations', pd.Series(dtype='int')).value_counts(),
    "Visited Platform": df.get('Visited Platform', pd.Series(dtype='int')).value_counts(),
    "Leads by Country": df['Country'].value_counts()
}

# Printing numerical results
for key, value in summary.items():
    if isinstance(value, pd.Series):
        print(f"{key}:")
        for k, v in value.items():
            print(f"{k}: {v}")
        print()
    else:
        print(f"{key}: {value}\n")

# Creating plots for visualization
fig, axes = plt.subplots(2, 2, figsize=(10, 8))  # Adjust the size if needed

# Plotting leads by current status
df['Current Status'].value_counts().plot(kind='bar', ax=axes[0, 0], color='skyblue', title='Leads by Current Status')
axes[0, 0].set_ylabel('Number of Leads')

# Plotting leads by type
df['Type'].value_counts().plot(kind='bar', ax=axes[0, 1], color='lightgreen', title='Leads by Type')
axes[0, 1].set_ylabel('Number of Leads')

# Plotting leads by country
df['Country'].value_counts().plot(kind='bar', ax=axes[1, 0], color='salmon', title='Leads by Country')
axes[1, 0].set_ylabel('Number of Leads')

# Plotting decision maker data
df['Decision Maker'].value_counts().plot(kind='bar', ax=axes[1, 1], color='orange', title='Decision Maker')
axes[1, 1].set_ylabel('Number of Leads')

plt.tight_layout()  
plt.show()
