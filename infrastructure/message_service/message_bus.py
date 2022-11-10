from abc import ABC, abstractmethod


class MessageBus(ABC):
    @abstractmethod
    def get_client(self):
        pass
