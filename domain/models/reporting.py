from ..enums.event_types import EventTypes
from dataclasses import dataclass


@dataclass
class ReportingModel:
    user_id: str
    username: str
    timestamp: int
    event_type: EventTypes
