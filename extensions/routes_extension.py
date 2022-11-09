from application.api.routes.reporting_routes import reporting_blueprint


def register_routes(app):
    app.register_blueprint(reporting_blueprint)

