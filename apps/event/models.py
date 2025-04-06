from django.core.validators import URLValidator
from django.db import models
from googletrans import Translator
from core.models import BaseModel


class EventCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории мероприятия"
    )
    name_en = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Название категории (англ.)",
        help_text="Название категории на английском"
    )
    name_ky = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Название категории (кырг.)",
        help_text="Название категории на кыргызском"
    )

    def save(self, *args, **kwargs):
        translator = Translator()
        if self.name:
            if not self.name_en:
                self.name_en = translator.translate(self.name, src='ru', dest='en').text
            if not self.name_ky:
                self.name_ky = translator.translate(self.name, src='ru', dest='ky').text
        super().save(*args, **kwargs)

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
    title_en = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Название (англ.)",
        help_text="Название мероприятия на английском"
    )
    title_ky = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Название (кырг.)",
        help_text="Название мероприятия на кыргызском"
    )

    description = models.TextField(
        verbose_name="Описание",
        help_text="Подробное описание мероприятия"
    )
    description_en = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание (англ.)",
        help_text="Описание мероприятия на английском"
    )
    description_ky = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание (кырг.)",
        help_text="Описание мероприятия на кыргызском"
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

    def save(self, *args, **kwargs):
        translator = Translator()
        if self.title:
            if not self.title_en:
                self.title_en = translator.translate(self.title, src='ru', dest='en').text
            if not self.title_ky:
                self.title_ky = translator.translate(self.title, src='ru', dest='ky').text
        if self.description:
            if not self.description_en:
                self.description_en = translator.translate(self.description, src='ru', dest='en').text
            if not self.description_ky:
                self.description_ky = translator.translate(self.description, src='ru', dest='ky').text
        super().save(*args, **kwargs)

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
