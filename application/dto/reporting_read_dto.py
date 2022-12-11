from dataclasses import dataclass


@dataclass
class ReportingReadDto:
    user_id: str
    username: str
    timestamp: int
    event_type: str
    old_role: str
    new_role: str
