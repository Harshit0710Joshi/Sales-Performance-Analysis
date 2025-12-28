-- Step 3: Data Cleaning Queries

-- Remove invalid sales
DELETE FROM superstore_sales
WHERE sales <= 0;

-- Standardize text columns
UPDATE superstore_sales
SET region = TRIM(region),
    category = TRIM(category);

-- Create clean analytical view
CREATE VIEW clean_sales_data AS
SELECT
    region,
    category,
    sales,
    profit,
    quantity
FROM superstore_sales;
