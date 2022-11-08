from ..enums.event_types import EventTypes


class ReportingModel:
    user_id: str
    username: str
    timestamp: int
    event_type: EventTypes
