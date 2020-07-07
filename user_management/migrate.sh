#!/usr/bin/env bash

if [ -d venv ]; then
    echo "Virtual environment already existed"
fi

activate () {
    echo "souring"
    # using note file in current folder for export environment variable
    source setenv
}

activate
pip install -r requirements.txt
#pip list
env
if [ -d migrations ]; then
    echo "Migrations already existed"
    rm -fr migrations
fi
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
