import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:your_password@localhost:5432/sales_performance"
)

df = pd.read_sql("SELECT * FROM clean_sales_data", engine)

# Basic info
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())


# Region-wise aggregation
region_summary = df.groupby("region").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    total_quantity=("quantity", "sum")
).reset_index()

print(region_summary)

# Category-wise aggregation
category_summary = df.groupby("category").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum")
).reset_index()

print(category_summary)
