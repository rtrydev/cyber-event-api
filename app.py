from threading import Thread

from flask import Flask
from flask_injector import FlaskInjector
from injector import singleton

from extensions.dependency_injection import configure
from extensions.routes_extension import register_routes

app = Flask(__name__)

register_routes(app)
di_container = FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run()
