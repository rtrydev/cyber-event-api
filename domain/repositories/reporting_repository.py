from abc import ABC, abstractmethod
from ..models.reporting import ReportingModel


class ReportingRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[ReportingModel]:
        pass

