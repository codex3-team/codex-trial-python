#!/bin/sh

# Collect static files
echo "---- Collect static files ----"
./manage.py collectstatic --noinput

# Apply database migrations
#echo "---- Apply database migrations ----"
./manage.py migrate


exec "$@"