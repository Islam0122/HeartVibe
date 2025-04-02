from django.apps import AppConfig


class OurcommandConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ourcommand'
    verbose_name = 'Наша команда'

    def ready(self):
        import apps.ourcommand.signals
