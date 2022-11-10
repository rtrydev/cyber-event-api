from datetime import datetime
import json
import os

from injector import inject

from application.event_handler.message_handler import MessageHandler
from domain.enums.event_types import map_event
from domain.models.reporting import ReportingModel
from domain.repositories.reporting_repository import ReportingRepository
from infrastructure.message_service.message_bus import MessageBus


class ReportingMessageHandler(MessageHandler):
    @inject
    def __init__(self, message_bus: MessageBus, reporting_repository: ReportingRepository):
        self.queue_name = os.environ.get("QUEUE_NAME")
        self.reporting_repository = reporting_repository
        self.bus_client = message_bus.get_client()

    def handle_messages(self):
        with self.bus_client:
            receiver = self.bus_client.get_queue_receiver(
                queue_name=self.queue_name
            )
            with receiver:
                for msg in receiver:
                    print(f"[{datetime.now()}] Received message: " + str(msg))
                    report = self._create_model(msg)

                    if report:
                        self.reporting_repository.add(report)
                        print(f"[{datetime.now()}] Adding message to db")
                    else:
                        print(f"[{datetime.now()}] Invalid message")

                    receiver.complete_message(msg)

    def _create_model(self, message):
        message_as_dict = json.loads(str(message))
        event_type = message_as_dict.get("Event")
        value = message_as_dict.get("Value")

        if not event_type or not value:
            return None

        return ReportingModel(
            user_id=value.get("UserId"),
            username=value.get("Username"),
            timestamp=value.get("UnixTimeStamp"),
            event_type=map_event.get(event_type)
        )
