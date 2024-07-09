#!/bin/sh

# Check if Redis is installed
if ! command -v redis-server &> /dev/null
then
    echo "redis-server could not be found, please install Redis using 'brew install redis'."
    exit
fi

# Start Redis server
redis-server --daemonize yes


# Run migrations
python manage.py makemigrations migration_content_publisher
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py createsuperuserifnotexists

python manage.py loaddata initial_app_purposes
python manage.py loaddata initial_learning_categories

# Check if a Celery worker is already running and kill it if it is
CELERY_WORKER_PID=$(pgrep -f "celery -A BusinessAppsCloudMoveTeamsAssist worker")

if [ -n "$CELERY_WORKER_PID" ]; then
    echo "Killing existing Celery worker with PID: $CELERY_WORKER_PID"
    kill -9 $CELERY_WORKER_PID
fi

# Start a new Celery worker
celery -A BusinessAppsCloudMoveTeamsAssist worker --loglevel=info &

# Start the server
python manage.py runserver



