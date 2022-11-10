import os

from azure.servicebus import ServiceBusClient
from infrastructure.message_service.message_bus import MessageBus


class AzureServiceBus(MessageBus):
    def __init__(self):
        conn_str = os.environ.get("BUS_CONNECTION_STR")

        self.bus_client = ServiceBusClient.from_connection_string(
            conn_str=conn_str, logging_enable=True
        )

    def get_client(self):
        return self.bus_client
