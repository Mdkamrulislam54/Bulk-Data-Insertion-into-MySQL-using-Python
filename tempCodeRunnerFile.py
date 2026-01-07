# Firstly install pip install sqlalchemy pymysql on Terminal
import pandas as pd
import mysql.connector

# Load data
df = pd.read_csv("C:\\Users\\Sajib\\Desktop\\Interactive Cares\\Vs Code+Python\\CoffeeShopSales.csv")

# Convert date format from DD/MM/YYYY to YYYY-MM-DD
df['transaction_date'] = pd.to_datetime(df['transaction_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="sqlworkbench24",
    database="RFM"
)
cursor = conn.cursor()

# Define the SQL query
sql = """
INSERT INTO transactions (
    transaction_id, transaction_date, transaction_time, transaction_qty,
    store_id, store_location, product_id, unit_price,
    product_category, product_type, product_detail
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert DataFrame to list of tuples
data = [tuple(row) for row in df.itertuples(index=False)]

# Use executemany for bulk insert
cursor.executemany(sql, data)

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("Bulk insert completed successfully!")