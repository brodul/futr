import peewee

from futr.services.database.models.person import Person, PersonLocation, Location
from futr.services.database.factory import db


class LocationService(object):
    def __init__(self, db=db):
        self.db = db
        self.bootstrap_db()
        self.bootstrap_assets()

    def bootstrap_db(self):
        self.db.connect()
        self.db.create_tables([Person, PersonLocation, Location], safe=True)

    def bootstrap_assets(self):
        location_names = [
            'Piramida',
            'Pivnica union',
            'Pivnica Siska',
            'Hood Burger',
            'Piramida',
            'Valvasor',
            'Romeo',
            'Roba',
        ]
        for name in location_names:
            location, _ = Location.get_or_create(name=name)
            location.save()

    def get_person(self, fingerprint):
        pass

    def get_locations(self):
        return [location.name for location in Location.select()]

    def get_person_locations(self):
        return [(person_location.location.name, person_location.person.name)
                for person_location in PersonLocation.select()]

    def create_person_location(self, person, location):
        location, _ = Location.get_or_create(name=location)
        person, _ = Person.get_or_create(name=person, fingerprint='')
        person.save()
        person_location, _ = PersonLocation.get_or_create(person=person, location=location)
        person_location.save()
