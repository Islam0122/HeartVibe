from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel


class ContactRequest(BaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Как к вам обращаться?"),
        help_text=_("Введите ваше имя для обращения")
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name=_("Номер телефона"),
        help_text=_("Введите номер в формате +996XXXXXXXXX")
    )
    is_processed = models.BooleanField(
        default=False,
        verbose_name=_("Обработано"),
        help_text=_("Отметьте, если заявка была обработана")
    )

    def __str__(self):
        return f"Заявка от {self.name} ({self.phone_number})"

    class Meta:
        verbose_name = _("Контактная заявка")
        verbose_name_plural = _("Контактные заявки")
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['is_processed']),
        ]