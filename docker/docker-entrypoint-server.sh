#!/bin/bash
pip install -r ../server/requirements/local.txt
python ../server/manage.py migrate --noinput
python ../server/manage.py collectstatic --noinput
exec "$@"