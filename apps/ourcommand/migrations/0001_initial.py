# Generated by Django 5.1.3 on 2025-04-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='team_photos/', verbose_name='Фото')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('bio', models.TextField(blank=True, verbose_name='Описание')),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Контактный номер')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Член команды',
                'verbose_name_plural': 'Члены команды',
            },
        ),
    ]
