import pgeocode
from models.delivery_point import DeliveryPoint


def find_geo(country_code, postal_code):
    nomi = pgeocode.Nominatim(country_code)
    location = nomi.query_postal_code(postal_code)
    latitude = location["latitude"]
    longitude = location["longitude"]
    nomi.query_postal_code()
    return latitude, longitude


def calculate_distance(locations):
    """
    :param locations: It's a list that keeps country and postal codes as a dictionary
            ex: [{"country_code": "tr", "postal_code: "35090"}, {"country_code": "tr", "postal_code: "35080"}]
    :return: It returns a distance matrix (i.e. 2D list)
    """
    geo_locations = list()
    for location in locations:
        geo_locations.append(find_geo(country_code=location["country_code"], postal_code=location["postal_code"]))


