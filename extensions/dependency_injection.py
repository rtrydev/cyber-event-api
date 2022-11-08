from injector import singleton

from application.api.controllers.reporting_controller import ReportingController
from domain.repositories.reporting_repository import ReportingRepository
from infrastructure.repositories.reporting_repository import CosmosReportingRepository


def configure(binder):
    binder.bind(ReportingRepository, to=CosmosReportingRepository, scope=singleton)
    binder.bind(ReportingController, to=ReportingController, scope=singleton)
