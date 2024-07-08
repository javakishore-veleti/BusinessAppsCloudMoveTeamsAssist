# BusinessAppsCloudMoveTeamsAssist
An intelligent co-worker chatbot for enterprise-level Microsoft Teams to assist with cloud migration using Hugging Face LLM and Django backend

## Project Setup

```shell
# Clone the repository
git clone <this_repo>
cd BusinessAppsCloudMoveTeamsAssist

python -m venv ~/runtime_data/python_venvs/BusinessAppsCloudMoveTeamsAssist
source ~/runtime_data/python_venvs/BusinessAppsCloudMoveTeamsAssist/bin/activate

# Observe dot in the end of below command
django-admin startproject BusinessAppsCloudMoveTeamsAssist .

python manage.py startapp migration_assistant
mkdir -p migration_assistant/migrations
touch migration_assistant/migrations/__init__.py
touch migration_assistant/serializers.py
touch migration_assistant/services.py
touch migration_assistant/tasks.py

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


```