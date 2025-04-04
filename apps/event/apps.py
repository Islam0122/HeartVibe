from django.apps import AppConfig


class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.event'
    verbose_name = 'Управление мероприятиями'

    def ready(self):
        import apps.event.signals
