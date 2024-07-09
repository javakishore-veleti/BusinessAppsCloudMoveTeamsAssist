#!/bin/sh

# Run migrations
python manage.py makemigrations migration_content_publisher
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py createsuperuserifnotexists

python manage.py loaddata initial_app_purposes
python manage.py loaddata initial_learning_categories

# Start the server
python manage.py runserver
