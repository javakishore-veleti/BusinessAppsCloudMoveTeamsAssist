from django.apps import AppConfig


class MigrationContentPublisherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'migration_content_publisher'

    def ready(self):
        pass

