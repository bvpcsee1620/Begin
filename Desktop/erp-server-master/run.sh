#!/bin/bash

python manage.py recreate_db
python server.py
