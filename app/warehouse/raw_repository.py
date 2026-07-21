from app.warehouse.db import get_connection
import json


def save_raw_event(event: dict):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO raw_orders(payload)
        VALUES (%s)
        """,
        (json.dumps(event),)
    )

    conn.commit()

    cur.close()
    conn.close()