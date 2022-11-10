from threading import Thread

from flask import Flask
from flask_injector import FlaskInjector
from injector import singleton

from application.event_handler.message_handler import MessageHandler
from extensions.dependency_injection import configure
from extensions.routes_extension import register_routes

app = Flask(__name__)

register_routes(app)
di_container = FlaskInjector(app=app, modules=[configure])

event_handler = di_container.injector.get(interface=MessageHandler, scope=singleton)

thread = Thread(target=event_handler.handle_messages)
thread.start()

if __name__ == '__main__':
    app.run()
