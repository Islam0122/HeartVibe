# Generated by Django 5.1.3 on 2025-04-06 21:19

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
                ('full_name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name (English)')),
                ('position_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Position (English)')),
                ('bio_en', models.TextField(blank=True, null=True, verbose_name='Bio (English)')),
                ('full_name_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Name (Kyrgyz)')),
                ('position_ky', models.CharField(blank=True, max_length=100, null=True, verbose_name='Position (Kyrgyz)')),
                ('bio_ky', models.TextField(blank=True, null=True, verbose_name='Bio (Kyrgyz)')),
            ],
            options={
                'verbose_name': 'Член команды',
                'verbose_name_plural': 'Члены команды',
            },
        ),
    ]
