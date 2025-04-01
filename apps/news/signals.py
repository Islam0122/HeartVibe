from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from .models import News

@receiver(post_migrate)
def load_news_data(sender, **kwargs):
    if not News.objects.exists():
        call_command('loaddata', 'apps/news/fixtures/initial_news_data.json')