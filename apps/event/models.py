from django.db import models
from django.core.validators import URLValidator
from core.models import BaseModel

class EventCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории мероприятия"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория мероприятий"
        verbose_name_plural = "Категории мероприятий"
        ordering = ['name']


class Event(BaseModel):
    image = models.ImageField(
        upload_to='events/',
        verbose_name="Изображение",
        help_text="Загрузите изображение для мероприятия",
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=200,
        verbose_name="Название",
        help_text="Введите название мероприятия"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Подробное описание мероприятия"
    )
    date = models.DateTimeField(
        verbose_name="Дата и время",
        help_text="Укажите дату и время проведения мероприятия"
    )
    location = models.CharField(
        max_length=200,
        verbose_name="Место проведения",
        help_text="Физическое место проведения (адрес или название места)"
    )
    location_url = models.URLField(
        max_length=255,
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name="Ссылка на место проведения",
        help_text="Ссылка на карту или страницу места проведения (необязательно)"
    )
    category = models.ForeignKey(
        EventCategory,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='events',
        verbose_name="Категория",
        help_text="Выберите категорию мероприятия"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активно",
        help_text="Отметьте, если мероприятие активно и должно отображаться"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date']),
            models.Index(fields=['category']),
            models.Index(fields=['is_active']),
            models.Index(fields=['is_active', '-date']),
        ]
