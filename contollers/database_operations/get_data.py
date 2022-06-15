from models import Session
import copy

session = Session()


def get_all_routes_data(Route, LocationRoute, Location):
    data = session.query(Route.id, Route.name, Route.optimal_solution, Location.name).filter(
        LocationRoute.fk_route_id == Route.id,
        LocationRoute.fk_location_id == Location.id).order_by(LocationRoute.fk_route_id).all()
    """
        Grouping data according to route id and storing them inside of the list
    """
    route_list = list()
    grouped_route = list()
    route_id = data[0][0]
    for item in data:
        if item[0] == route_id:
            grouped_route.append(item)
        else:
            route_list.append(copy.deepcopy(grouped_route))
            route_id = item[0]
            grouped_route.clear()
            grouped_route.append(item)

    response_list = list()
    for route in route_list:
        response_list.append(prepare_response(route))
    return response_list


def get_route_data(Route, LocationRoute, Location, id):
    data = session.query(Route.id, Route.name, Route.optimal_solution, Location.name).filter(
        LocationRoute.fk_route_id == Route.id,
        LocationRoute.fk_location_id == Location.id).filter(Route.id == id).order_by(LocationRoute.order_no).all()
    return prepare_response(data)


def prepare_response(data):
    response_as_dict = dict()
    location_list = list()
    response_as_dict["id"] = data[0][0]
    response_as_dict["name"] = data[0][1]
    response_as_dict["travelled_distance"] = data[0][2]
    for item in data:
        location_list.append(item[3])
    response_as_dict["travel_order"] = location_list
    return response_as_dict
