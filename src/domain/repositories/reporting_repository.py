from abc import ABC, abstractmethod


class ReportingRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
