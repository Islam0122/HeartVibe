from django.db import models
from core.models import BaseModel


class News(BaseModel):
    image = models.ImageField(
        upload_to='news/',
        verbose_name="Изображение",
        help_text="Выберите изображение для новости"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Введите заголовок новости (до 255 символов)"
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите текст новости"
    )

    class Meta:
        db_table = 'news'
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
