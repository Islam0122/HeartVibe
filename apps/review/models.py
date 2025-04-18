from django.db import models
from django.utils.translation import gettext_lazy as _

class Review(models.Model):
    author = models.CharField(
        max_length=100,
        verbose_name=_("Автор"),
        help_text=_("Имя автора отзыва (на русском)")
    )
    text = models.TextField(
        verbose_name=_("Текст отзыва"),
        help_text=_("Введите содержание отзыва (на русском)")
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name=_("Оценка"),
        help_text=_("Оценка от 1 до 5"),
        choices=[(i, f"{i} ⭐") for i in range(1, 6)]
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата создания")
    )

    # ENGLISH
    author_en = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Автор (англ.)"),
        help_text=_("Имя автора на английском языке")
    )
    text_en = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Текст отзыва (англ.)"),
        help_text=_("Отзыв на английском языке")
    )

    # KYRGYZ
    author_ky = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Автор (кырг.)"),
        help_text=_("Имя автора на кыргызском языке")
    )
    text_ky = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Текст отзыва (кырг.)"),
        help_text=_("Отзыв на кыргызском языке")
    )

    # Avatar
    avatar = models.ImageField(
        upload_to='avatars/',  # Путь, куда будет сохраняться изображение
        blank=True,
        null=True,
        verbose_name=_("Аватар"),
        help_text=_("Аватар автора отзыва")
    )

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} – {self.rating} ⭐"

    def save(self, *args, **kwargs):
        from googletrans import Translator
        translator = Translator()

        if self.author and not self.author_en:
            self.author_en = translator.translate(self.author, src='ru', dest='en').text
        if self.text and not self.text_en:
            self.text_en = translator.translate(self.text, src='ru', dest='en').text

        if self.author and not self.author_ky:
            self.author_ky = translator.translate(self.author, src='ru', dest='ky').text
        if self.text and not self.text_ky:
            self.text_ky = translator.translate(self.text, src='ru', dest='ky').text

        super().save(*args, **kwargs)
