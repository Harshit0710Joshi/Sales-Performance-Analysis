import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine(
    "postgresql+psycopg2://postgres:your_password@localhost:5432/sales_performance"
)

# SQL query
query = "SELECT * FROM clean_sales_data"

# Load into DataFrame
df = pd.read_sql(query, engine)

print(df.head())
print(df.shape)
