from threading import Thread

from flask import Flask
from flask_injector import FlaskInjector
from injector import singleton

from application.event_handler.event_handler import EventHandler
from extensions.dependency_injection import configure
from extensions.routes_extension import register_routes
from infrastructure.message_service.message_bus import MessageBus

app = Flask(__name__)

register_routes(app)
di_container = FlaskInjector(app=app, modules=[configure])

event_bus = di_container.injector.get(interface=MessageBus, scope=singleton)
event_handler = EventHandler(event_bus)

thread = Thread(target=event_handler.handle_messages)
thread.start()

if __name__ == '__main__':
    app.run()
