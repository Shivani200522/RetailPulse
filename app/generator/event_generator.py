import random
import uuid
from datetime import datetime

import numpy as np

from app.generator.business_rules import BusinessRules
from app.generator.data_loader import MasterDataLoader
from app.models.order_event import OrderEvent


class EventGenerator:

    def __init__(self):

        self.loader = MasterDataLoader()
        self.rules = BusinessRules()

    def generate_order(self):

        customer = self.loader.customers.sample(1).iloc[0]

        store = self.loader.stores.sample(1).iloc[0]

        month = datetime.now().month

        month_weights = self.rules.get_month_weights(month)

        products = self.loader.products.copy()

        weights = []

        for _, product in products.iterrows():

            weights.append(
                month_weights.get(product["category"], 1.0)
            )

        probabilities = np.array(weights)

        probabilities = probabilities / probabilities.sum()

        product = products.iloc[
            np.random.choice(
                len(products),
                p=probabilities
            )
        ]

        quantity = random.randint(1, 3)

        discount = random.choice([0, 5, 10, 15, 20])

        final_price = round(
            product["price"] * quantity * (1 - discount / 100),
            2,
        )

        payment_methods = self.rules.get_payment_methods()

        payment_method = random.choices(
            list(payment_methods.keys()),
            weights=list(payment_methods.values()),
            k=1,
        )[0]

        payment_status = (
            "SUCCESS"
            if random.random()
            < self.rules.get_payment_success_rate()
            else "FAILED"
        )

        return OrderEvent(

            event_type="ORDER_CREATED",

            order_id=f"ORD-{uuid.uuid4().hex[:10].upper()}",

            customer_id=customer["customer_id"],

            product_id=product["product_id"],

            store_id=store["store_id"],

            quantity=quantity,

            unit_price=float(product["price"]),

            discount_percent=discount,

            final_price=final_price,

            payment_method=payment_method,

            payment_status=payment_status,
        )