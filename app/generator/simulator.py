import json
import time

from app.generator.event_generator import EventGenerator


def main():

    generator = EventGenerator()

    print("RetailPulse Simulator Started...\n")

    while True:

        event = generator.generate_order()

        print(
            json.dumps(
                event.model_dump(mode="json"),
                indent=4
            )
        )

        time.sleep(2)


if __name__ == "__main__":
    main()