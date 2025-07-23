# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame( Sales, COGS, Country, Year, Quarter, Month, Day, Discount Band, Discounts, Gross Sales, Manufacturing Price, Month Name, Month Number, Product, Profit, Sale Price, Segment, Units Sold, Year.1)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dataset.columns = [col.strip().replace(" ", "_").replace(".", "_") for col in dataset.columns]

dataset["Month_Name"] = pd.Categorical(dataset["Month_Name"], 
                                       categories=["January", "February", "March", "April", "May", "June", 
                                                   "July", "August", "September", "October", "November", "December"],
                                       ordered=True)

monthly_sales = dataset.groupby("Month_Name")["Sales"].sum().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x="Month_Name", y="Sales", marker='o')
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
