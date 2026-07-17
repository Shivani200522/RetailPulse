from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class BaseEvent(BaseModel):
    """
    Base model shared by all events in the RetailPulse platform.
    """

    event_id: str = Field(default_factory=lambda: str(uuid4()))
    event_type: str
    event_timestamp: datetime = Field(default_factory=datetime.utcnow)
    source: str = "RetailPulse-Simulator"