from abc import ABC, abstractmethod


class DatabaseProvider(ABC):
    @abstractmethod
    def get_database(self):
        pass
