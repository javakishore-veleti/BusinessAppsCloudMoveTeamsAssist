# signals.py

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.management import call_command


def create_superuser(sender, **kwargs):
    call_command('createsuperuser')


class MigrationContentPublisherConfig(AppConfig):
    name = 'migration_content_publisher'

    def ready(self):
        post_migrate.connect(create_superuser, sender=self)
