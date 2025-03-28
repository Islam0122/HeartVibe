from django.db import models
from django.utils.timezone import now
from datetime import timedelta

class OTP(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return now() < self.created_at + timedelta(minutes=5)  # Действует 5 минут
