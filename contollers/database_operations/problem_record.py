from models import *
from .insert_data import insert_data
from .get_data import *


def record_problem(name, locations, objective, output):
    """
    :param name:
    :param locations: [{"name": "Ankara", "latitude": "123123", "longitude": "35090"},
                         {"name": "Izmir", "latitude": "123123", "longitude": "35090"},
                         {"name": "Adana", "latitude": "123123", "longitude": "35090"},
                         {"name": "Istanbul", "latitude": "123123", "longitude": "35090"}]
    :param objective: Float Number
    :param output: List of locations by their order
    :return: Boolean, either record succeed or not
    """
    try:
        if objective != 0:
            route = Route(name=name, optimal_solution=objective)
            insert_data(route)
            route_id = route.id
            if route_id is not None:
                for location in locations:
                    loc = Location(**location)
                    insert_data(loc)
                    loc_id = loc.id
                    order_no = output.index(location["name"]) + 1
                    insert_data(LocationRoute(fk_route_id=route_id, fk_location_id=loc_id, order_no=order_no))
            return True
    except Exception as ex:
        print(ex)
        return False


def get_routes():
    response_list = get_all_routes_data(Route, LocationRoute, Location)
    return response_list


def get_route(id):
    route = get_route_data(Route, LocationRoute, Location, id)
    return route
