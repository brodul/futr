from collections import defaultdict

from futr.services.location import LocationService


class PersonLocationController(object):
    """docstring for PersonLocationController."""

    def __init__(self):
        self.location_service = LocationService()

    def get(self):
        pairs = self.location_service.get_person_locations()
        d = defaultdict(list)
        for location, person in pairs:
            d[location].append(person)
        return d

    def get_locations(self):
        return self.location_service.get_locations()

    def create_person_location(self, person, location):
        self.location_service.create_person_location(person, location)
