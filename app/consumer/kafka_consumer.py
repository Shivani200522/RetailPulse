from kafka import KafkaConsumer
import json

from app.warehouse.raw_repository import save_raw_event
from app.database.order_repository import insert_order

consumer = KafkaConsumer(
    "retail-orders",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Consumer Started...\n")

try:
    for message in consumer:
        event = message.value

        insert_order(event)

        print(f"Saved Raw Event: {event['order_id']}")

except KeyboardInterrupt:
    print("\nStopping Consumer...")

finally:
    consumer.close()