import json
import time

from app.generator.event_generator import EventGenerator
from app.generator.kafka_producer import send_event

from app.generator.kafka_producer import (
    send_event,
    producer
)

def main():

    generator = EventGenerator()

    print("RetailPulse Simulator Started...\n")

    while True:

        event = generator.generate_order()

        send_event(event)

        print(f"Sent Order {event.order_id} to Kafka")
        time.sleep(2)
        producer.flush()


if __name__ == "__main__":
    main()