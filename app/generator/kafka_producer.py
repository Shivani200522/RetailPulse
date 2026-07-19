import json
from confluent_kafka import Producer


conf = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(conf)


def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(
            f"Sent -> {msg.topic()} [{msg.partition()}]"
        )


def send_event(event):

    producer.produce(
        topic="retail-orders",
        value=json.dumps(
            event.model_dump(mode="json")
        ),
        callback=delivery_report
    )

    producer.poll(0)