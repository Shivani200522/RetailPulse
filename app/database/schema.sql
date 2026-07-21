CREATE TABLE IF NOT EXISTS raw_orders (

    order_id VARCHAR(30) PRIMARY KEY,

    customer_id VARCHAR(20),
    product_id VARCHAR(20),
    store_id VARCHAR(20),

    quantity INT,

    unit_price DOUBLE PRECISION,
    discount_percent DOUBLE PRECISION,
    final_price DOUBLE PRECISION,

    payment_method VARCHAR(30),
    payment_status VARCHAR(20),

    event_timestamp TIMESTAMP
);