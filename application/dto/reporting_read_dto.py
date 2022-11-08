from dataclasses import dataclass


@dataclass
class ReportingReadDto:
    user_id: str
    username: str
    timestamp: int
    event_type: str
