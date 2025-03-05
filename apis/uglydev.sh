#!/bin/bash
cd auth_service/
python manage.py makemigrations core_models
python manage.py migrate
python manage.py runserver 0.0.0.0:8000&

cd ../publication_service/
python manage.py makemigrations publication
python manage.py migrate
python manage.py runserver 0.0.0.0:8001 &

cd ../profile_service/
python manage.py runserver 0.0.0.0:8002 &

bash