import os

from infrastructure.message_service.message_bus import MessageBus


class EventHandler:
    def __init__(self, message_bus: MessageBus):
        self.queue_name = os.environ.get("QUEUE_NAME")
        self.bus_client = message_bus.get_client()

    def handle_messages(self):
        with self.bus_client:
            receiver = self.bus_client.get_queue_receiver(
                queue_name=self.queue_name
            )
            with receiver:
                for msg in receiver:
                    print(msg)
                    receiver.complete_message(msg)
