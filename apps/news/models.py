from django.db import models
from googletrans import Translator
from core.models import BaseModel


class News(BaseModel):
    image = models.ImageField(
        upload_to='news/',
        verbose_name="Изображение",
        help_text="Выберите изображение для новости"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок (RU)",
        help_text="Введите заголовок новости на русском языке (до 255 символов)"
    )
    content = models.TextField(
        verbose_name="Содержимое (RU)",
        help_text="Введите текст новости на русском языке"
    )

    title_en = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Заголовок (EN)",
        help_text="Автоматически переводится с русского на английский"
    )
    content_en = models.TextField(
        blank=True,
        null=True,
        verbose_name="Содержимое (EN)",
        help_text="Автоматически переводится с русского на английский"
    )
    title_ky = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Заголовок (Kyrgyz)",
        help_text="Автоматически переводится с русского на кыргызский"
    )
    content_ky = models.TextField(
        blank=True,
        null=True,
        verbose_name="Содержимое (Kyrgyz)",
        help_text="Автоматически переводится с русского на кыргызский"
    )

    def save(self, *args, **kwargs):
        translator = Translator()
        if self.title and not self.title_en:
            self.title_en = translator.translate(self.title, src='ru', dest='en').text
        if self.content and not self.content_en:
            self.content_en = translator.translate(self.content, src='ru', dest='en').text
        if self.title and not self.title_ky:
            self.title_ky = translator.translate(self.title, src='ru', dest='ky').text
        if self.content and not self.content_ky:
            self.content_ky = translator.translate(self.content, src='ru', dest='ky').text

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'news'
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
