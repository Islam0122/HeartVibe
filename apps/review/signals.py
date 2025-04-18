from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from .models import Review

@receiver(post_migrate)
def load_review_data(sender, **kwargs):
    if not Review.objects.exists():
        call_command('loaddata', 'apps/review/fixtures/initial_review_data.json')