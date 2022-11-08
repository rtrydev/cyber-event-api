from flask import Flask
from flask_injector import FlaskInjector

from extensions.dependency_injection import configure
from extensions.routes_extension import register_routes

app = Flask(__name__)

register_routes(app)
FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run()
