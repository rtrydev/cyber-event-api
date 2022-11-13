from flask import Blueprint
from injector import inject
from ..controllers.reporting_controller import ReportingController

reporting = Blueprint('reporting_routes', __name__, url_prefix='/reporting')


@inject
@reporting.route('/', methods=['GET'])
def get_all(controller: ReportingController):
    return controller.get_reports()

