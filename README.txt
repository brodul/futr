futr README
==================

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/pip install -e .

- start postgres on localhost e.g. `docker run  postgres  -p 5432:5432`

- DATABASE_URL="postgres://postgres:mysecretpassword@localhost/postgres" $VENV/bin/pserve --reload development.ini
