from flask import Blueprint
from injector import inject
from ..controllers.reporting_controller import ReportingController

reporting_blueprint = Blueprint('reporting_routes', __name__)


@inject
@reporting_blueprint.route('/', methods=['GET'])
def get_all(controller: ReportingController):
    return controller.get_reports()

