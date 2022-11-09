from injector import singleton

from application.api.controllers.reporting_controller import ReportingController
from domain.repositories.reporting_repository import ReportingRepository
from infrastructure.db.cosmos_database_provider import CosmosDatabaseProvider
from infrastructure.db.database_provider import DatabaseProvider
from infrastructure.repositories.cosmos_reporting_repository import CosmosReportingRepository


def configure(binder):
    binder.bind(ReportingRepository, to=CosmosReportingRepository, scope=singleton)
    binder.bind(ReportingController, to=ReportingController, scope=singleton)
    binder.bind(DatabaseProvider, to=CosmosDatabaseProvider, scope=singleton)
