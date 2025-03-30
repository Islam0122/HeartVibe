from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ContactrequestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.contactrequest'
    verbose_name = _("Контактные заявки")