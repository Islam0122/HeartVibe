from django.db import models
from django.utils.translation import gettext_lazy as _


class TeamMember(models.Model):
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True, verbose_name="Фото")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    bio = models.TextField(blank=True, verbose_name="Описание")
    contact_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Контактный номер")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    # Многоязычные поля
    full_name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Full Name (English)"))
    position_en = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Position (English)"))
    bio_en = models.TextField(blank=True, null=True, verbose_name=_("Bio (English)"))

    full_name_ky = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Full Name (Kyrgyz)"))
    position_ky = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Position (Kyrgyz)"))
    bio_ky = models.TextField(blank=True, null=True, verbose_name=_("Bio (Kyrgyz)"))

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return f"{self.full_name} - {self.position}"

    def save(self, *args, **kwargs):
        from googletrans import Translator

        translator = Translator()

        if self.full_name and not self.full_name_en:
            self.full_name_en = translator.translate(self.full_name, src='ru', dest='en').text
        if self.position and not self.position_en:
            self.position_en = translator.translate(self.position, src='ru', dest='en').text
        if self.bio and not self.bio_en:
            self.bio_en = translator.translate(self.bio, src='ru', dest='en').text

        if self.full_name and not self.full_name_ky:
            self.full_name_ky = translator.translate(self.full_name, src='ru', dest='ky').text
        if self.position and not self.position_ky:
            self.position_ky = translator.translate(self.position, src='ru', dest='ky').text
        if self.bio and not self.bio_ky:
            self.bio_ky = translator.translate(self.bio, src='ru', dest='ky').text

        super().save(*args, **kwargs)
