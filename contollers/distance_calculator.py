import pgeocode
import haversine as hs


class DistanceCalculator:
    def find_geo_from_postal_code_and_country(self, country_code, postal_code):
        """
        :param country_code: Country abbreviation (i.e. tr, fr, usa)
        :param postal_code: Postal Code of Location
        :return: Geo-Location as tupple ex: (latitude, longitude)
        """
        nomi = pgeocode.Nominatim(country_code)
        location = nomi.query_postal_code(postal_code)
        latitude = location["latitude"]
        longitude = location["longitude"]
        return latitude, longitude

    def create_coordinate_list(self, locations):
        """
        :param locations: It's a list that keeps name of location, country and postal codes as a dictionary
                            ex: [{"name":"A","country_code": "tr", "postal_code: "35090"},
                            {"name":"B","country_code": "fr", "longitude: "75013"}]
                                or
                            [{"name":"B","latitude": "75013", "longitude: "75013"}]
        :return: It returns a dictionary list that contains location name and coordinates of that location
        """
        geo_locations = list()
        for location in locations:
            print(location.keys())
            if "postal_code" in location.keys():
                latitude, longitude = self.find_geo_from_postal_code_and_country(country_code=location["country_code"],
                                                                                 postal_code=location["postal_code"])
                geo_locations.append({"name": location["name"], "coordinates": (latitude, longitude)})
            else:
                geo_locations.append(
                    {"name": location["name"],
                     "coordinates": (float(location["latitude"]), float(location["longitude"]))})
        return geo_locations

    def create_distance_matrix(self, coordinates):
        """
            :param coordinates: It's a list that keeps country and postal codes as a dictionary
                                ex: [{"name": "B", "coordinates": (latitude, longitude)]},
                                {"name": "A", "coordinates": (latitude, longitude)]}]
            :return: It returns a distance matrix (i.e. 2D list)
        """
        distance_matrix = dict()
        for i in range(len(coordinates)):  # TODO Calculates distance 2 time check algorithm later on
            for j in range(len(coordinates)):
                if coordinates[j]["name"] is coordinates[i]["name"]:
                    distance_matrix[(i + 1, j + 1)] = 100000
                    continue
                distance = hs.haversine(coordinates[i]["coordinates"], coordinates[j]["coordinates"])
                distance_matrix[(i + 1, j + 1)] = distance
        return distance_matrix

# Test
# coordinate_list = create_coordinate_list([{"name": "A", "country_code": "tr", "postal_code": "35090"},
#                                           {"name": "B", "country_code": "fr", "postal_code": "75013"},
#                                           {"name": "C", "country_code": "tr", "postal_code": "45900"},
#                                           {"name": "D", "country_code": "fr", "postal_code": "35800"}])

# coordinate_list = create_coordinate_list([{"name": "B", "latitude": "75013", "longitude": "35800"}])
#
# print(coordinate_list)
#
# distances = create_distance_matrix(coordinate_list)
#
# print(distances)
