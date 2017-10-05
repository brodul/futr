#! /usr/bin/env python
from futr.database import db
from futr.database.models.person import PersonLocation

if __name__ == '__main__':
    db.connect()
    PersonLocation.drop_table(fail_silently=True)
    PersonLocation.create_table()
    db.close()
