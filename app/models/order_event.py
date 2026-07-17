from app.models.base_event import BaseEvent


class OrderEvent(BaseEvent):
    """
    Represents a retail order event.
    """

    order_id: str

    customer_id: str

    product_id: str

    store_id: str

    quantity: int

    unit_price: float

    discount_percent: float

    final_price: float

    payment_method: str

    payment_status: str