from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from .models import EventCategory , Event

@receiver(post_migrate)
def load_event_data(sender, **kwargs):
    if not  Event.objects.exists() and not EventCategory.objects.exists() :
        call_command('loaddata', 'apps/event/fixtures/initial_events_data.json')