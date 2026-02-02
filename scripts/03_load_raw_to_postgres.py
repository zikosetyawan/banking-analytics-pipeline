import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# ======================
# Load cleaned CSV
# ======================
df = pd.read_csv("data/processed/banking_transactions_clean.csv")
print(f"Jumlah baris yang akan dimuat: {len(df)}")

# ======================
# PostgreSQL connection
# ======================
conn = psycopg2.connect(
    host="127.0.0.1",
    port=5433,
    dbname="banking_db",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

# ======================
# Create table (RAW)
# ======================
create_table_query = """
DROP TABLE IF EXISTS transactions_raw;
CREATE TABLE transactions_raw (
    customer_id TEXT,
    customer_name TEXT,
    gender TEXT,
    age INT,
    state TEXT,
    city TEXT,
    bank_branch TEXT,
    account_type TEXT,
    transaction_id TEXT,
    transaction_date DATE,
    transaction_time TEXT,
    transaction_amount NUMERIC,
    merchant_id TEXT,
    transaction_type TEXT,
    merchant_category TEXT,
    account_balance NUMERIC,
    transaction_device TEXT,
    transaction_location TEXT,
    device_type TEXT,
    is_fraud INT,
    transaction_currency TEXT,
    customer_contact TEXT,
    transaction_description TEXT,
    customer_email TEXT
);
"""
cursor.execute(create_table_query)
conn.commit()

# ======================
# Insert data (bulk)
# ======================
columns = df.columns.tolist()
values = [tuple(row) for row in df.to_numpy()]

insert_query = f"""
INSERT INTO transactions_raw ({','.join(columns)})
VALUES %s
"""

execute_values(cursor, insert_query, values)
conn.commit()

cursor.close()
conn.close()

print("✅ Data berhasil dimuat ke PostgreSQL (transactions_raw)")
