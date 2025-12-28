import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:your_password@localhost:5432/sales_performance"
)

df = pd.read_sql("SELECT * FROM clean_sales_data", engine)

# 1. Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(x="region", y="sales", data=df, estimator=sum)
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.xlabel("Region")
plt.show()

# 2. Profit by Category
plt.figure(figsize=(8,5))
sns.barplot(x="category", y="profit", data=df, estimator=sum)
plt.title("Total Profit by Category")
plt.ylabel("Profit")
plt.xlabel("Category")
plt.show()

# 3. Sales vs Profit Scatter
plt.figure(figsize=(8,5))
sns.scatterplot(x="sales", y="profit", hue="category", data=df)
plt.title("Sales vs Profit by Category")
plt.show()
