from application.api.routes.reporting_routes import reporting


def register_routes(app):
    app.register_blueprint(reporting)

