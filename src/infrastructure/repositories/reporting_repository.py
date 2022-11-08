from domain.enums.event_types import EventTypes
from domain.repositories.reporting_repository import ReportingRepository
from domain.models.reporting import ReportingModel


class CosmosReportingRepository(ReportingRepository):
    def get_all(self) -> list[ReportingModel]:
        reporting_model = ReportingModel(
            user_id="test1",
            username="rtry",
            timestamp=123123123,
            event_type=EventTypes.UserLogon
        )
        return [
            reporting_model
        ]
