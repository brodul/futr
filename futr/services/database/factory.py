import os
import urlparse

from peewee import PostgresqlDatabase

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])


def db_factory():
    db = PostgresqlDatabase(
        url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )

    return db


db = db_factory()
