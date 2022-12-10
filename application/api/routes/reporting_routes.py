from flask import Blueprint
from injector import inject
from decorators.auth_decorator import auth
from ..controllers.reporting_controller import ReportingController

reporting = Blueprint('reporting_routes', __name__, url_prefix='/reporting')


@inject
@reporting.route('/', methods=['GET'])
@auth(["Admin"])
def get_all(controller: ReportingController):
    return controller.get_reports()

