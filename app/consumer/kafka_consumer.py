import json
from confluent_kafka import Consumer


consumer = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": "retailpulse-consumer",
        "auto.offset.reset": "earliest",
    }
)

consumer.subscribe(["retail-orders"])

print("RetailPulse Consumer Started...\n")

try:
    while True:

        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print(msg.error())
            continue

        event = json.loads(msg.value().decode("utf-8"))

        print("=" * 60)
        print(f"Order : {event['order_id']}")
        print(f"Customer : {event['customer_id']}")
        print(f"Product : {event['product_id']}")
        print(f"Amount : ₹{event['final_price']}")
        print(f"Payment : {event['payment_status']}")
        print("=" * 60)

except KeyboardInterrupt:
    print("\nStopping Consumer...")

finally:
    consumer.close()