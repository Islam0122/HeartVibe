from django.db import models

class TeamMember(models.Model):
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True, verbose_name="Фото")
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    bio = models.TextField(blank=True, verbose_name="Описание")
    contact_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Контактный номер")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return f"{self.full_name} - {self.position}"
