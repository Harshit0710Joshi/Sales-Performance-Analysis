-- Step 3: PostgreSQL Schema Creation

CREATE TABLE superstore_sales (
    ship_mode TEXT,
    segment TEXT,
    country TEXT,
    city TEXT,
    state TEXT,
    postal_code INTEGER,
    region TEXT,
    category TEXT,
    sub_category TEXT,
    sales NUMERIC,
    quantity INTEGER,
    discount NUMERIC,
    profit NUMERIC
);

-- CSV imported using pgAdmin Import/Export tool
