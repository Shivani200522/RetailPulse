from app.warehouse.db import get_connection

conn = get_connection()
cur = conn.cursor()


cur.execute("""

CREATE TABLE IF NOT EXISTS raw_orders(

id SERIAL PRIMARY KEY,

payload JSONB,

received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

""")



cur.execute("""

CREATE TABLE IF NOT EXISTS dim_customer(

customer_id VARCHAR(20) PRIMARY KEY,

age INT,

gender VARCHAR(10),

city VARCHAR(50),

income_level VARCHAR(20)

);

""")

cur.execute("""

CREATE TABLE IF NOT EXISTS dim_product(

product_id VARCHAR(20) PRIMARY KEY,

product_name VARCHAR(100),

category VARCHAR(50),

brand VARCHAR(50),

price NUMERIC

);

""")

cur.execute("""

CREATE TABLE IF NOT EXISTS dim_store(

store_id VARCHAR(20) PRIMARY KEY,

city VARCHAR(50),

store_type VARCHAR(30)

);

""")

cur.execute("""

CREATE TABLE IF NOT EXISTS fact_orders(

event_id UUID PRIMARY KEY,

order_id VARCHAR(30),

customer_id VARCHAR(20),

product_id VARCHAR(20),

store_id VARCHAR(20),

quantity INT,

unit_price NUMERIC,

discount_percent NUMERIC,

final_price NUMERIC,

payment_method VARCHAR(30),

payment_status VARCHAR(20),

event_timestamp TIMESTAMP,

FOREIGN KEY(customer_id) REFERENCES dim_customer(customer_id),

FOREIGN KEY(product_id) REFERENCES dim_product(product_id),

FOREIGN KEY(store_id) REFERENCES dim_store(store_id)

);

""")

conn.commit()

cur.close()
conn.close()

print("Warehouse Ready.")