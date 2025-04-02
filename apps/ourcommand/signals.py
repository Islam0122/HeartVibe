from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from .models import TeamMember

@receiver(post_migrate)
def load_news_data(sender, **kwargs):
    if not TeamMember.objects.exists():
        call_command('loaddata', 'apps/ourcommand/fixtures/initial_team_data.json')