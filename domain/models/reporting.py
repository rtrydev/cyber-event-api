from ..enums.event_types import EventTypes
from dataclasses import dataclass


@dataclass
class ReportingModel:
    user_id: str
    username: str
    timestamp: int
    event_type: EventTypes
    old_role: str = None
    new_role: str = None
