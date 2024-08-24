from django.apps import AppConfig
from django.core import management


class HomepageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'homepage'


class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        management.call_command('run_speech')
        management.call_command('run_hand')