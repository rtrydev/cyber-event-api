from injector import singleton

from application.api.controllers.reporting_controller import ReportingController


def configure(binder):
    binder.bind(ReportingController, to=ReportingController, scope=singleton)
