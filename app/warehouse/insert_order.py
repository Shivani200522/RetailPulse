from app.warehouse.db import get_connection


def insert_order(event):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO fact_orders(
            event_id,
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
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (event_id) DO NOTHING
        """,
        (
            event["event_id"],
            event["order_id"],
            event["customer_id"],
            event["product_id"],
            event["store_id"],
            event["quantity"],
            event["unit_price"],
            event["discount_percent"],
            event["final_price"],
            event["payment_method"],
            event["payment_status"],
            event["event_timestamp"],
        ),
    )

    conn.commit()

    cur.close()
    conn.close()