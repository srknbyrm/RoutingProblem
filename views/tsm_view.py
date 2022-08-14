from flask import Blueprint, jsonify, request

from contollers.database_operations.problem_record import get_routes, get_route
from contollers.tsm_solver import TSM

bp = Blueprint('tsm_view', __name__)


@bp.route(f'/tsm_routing', methods=['POST'])
def route_problem():
    request_data = request.get_json()
    tsm = TSM(request_data["locations"], request_data["name"])
    result = tsm.solve_tsm()
    return jsonify({"optimal_route": result[1], "total_distance": result[2]})


@bp.route(f'/get_routes', methods=['GET'])
def get_route_problems():
    response_data = get_routes()
    return jsonify(response_data)


@bp.route(f'/get_route/<id>', methods=['GET'])
def get_route_problem(id):
    response_data = get_route(id=id)
    return jsonify(response_data)
