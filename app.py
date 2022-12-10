from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector
from extensions.dependency_injection import configure
from extensions.routes_extension import register_routes

app = Flask(__name__)
CORS(app)

register_routes(app)
di_container = FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run()
