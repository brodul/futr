from peewee import *

from futr.database.factory import db


class Person(Model):
    name = CharField()
    # added = DateField()
    # last_visited = DateField()
    fingerprint = CharField()

    class Meta:
        database = db


class Location(Model):
    name = CharField(unique=True)

    class Meta:
        database = db


class PersonLocation(Model):
    person = ForeignKeyField(Person)
    location = ForeignKeyField(Location)

    class Meta:
        database = db
