from app.database.db import get_connection


def insert_order(order):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO raw_orders(
            order_id,
            customer_id,
            product_id,
            store_id,
            quantity,
            unit_price,
            discount_percent,
            final_price,
            payment_method,
            payment_status,
            event_timestamp
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT(order_id) DO NOTHING
        """,
        (
            order["order_id"],
            order["customer_id"],
            order["product_id"],
            order["store_id"],
            order["quantity"],
            order["unit_price"],
            order["discount_percent"],
            order["final_price"],
            order["payment_method"],
            order["payment_status"],
            order["event_timestamp"]
        )
    )

    conn.commit()
    cur.close()
    conn.close()