from abc import ABC, abstractmethod


class MessageHandler(ABC):
    @abstractmethod
    def handle_messages(self):
        pass
