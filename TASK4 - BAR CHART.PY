# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame( Sales, COGS, Country, Year, Quarter, Month, Day, Discount Band, Discounts, Gross Sales, Manufacturing Price, Month Name, Month Number, Product, Profit, Sale Price, Segment, Units Sold, Year.1)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import seaborn as sns

dataset.columns = [col.strip().replace(" ", "_").replace(".", "_") for col in dataset.columns]

plt.figure(figsize=(10,6))
sns.barplot(x="Product", y="Sales", data=dataset, estimator=sum, ci=None, palette="Set2")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
