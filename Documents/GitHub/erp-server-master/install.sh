#!/bin/bash

sudo apt-get update
sudo apt-get install postgresql postgresql-contrib libpq-dev
pip install -r requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
