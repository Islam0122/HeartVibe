# Generated by Django 5.1.3 on 2025-04-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(help_text='Имя автора отзыва (на русском)', max_length=100, verbose_name='Автор')),
                ('text', models.TextField(help_text='Введите содержание отзыва (на русском)', verbose_name='Текст отзыва')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1 ⭐'), (2, '2 ⭐'), (3, '3 ⭐'), (4, '4 ⭐'), (5, '5 ⭐')], help_text='Оценка от 1 до 5', verbose_name='Оценка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author_en', models.CharField(blank=True, help_text='Имя автора на английском языке', max_length=100, null=True, verbose_name='Автор (англ.)')),
                ('text_en', models.TextField(blank=True, help_text='Отзыв на английском языке', null=True, verbose_name='Текст отзыва (англ.)')),
                ('author_ky', models.CharField(blank=True, help_text='Имя автора на кыргызском языке', max_length=100, null=True, verbose_name='Автор (кырг.)')),
                ('text_ky', models.TextField(blank=True, help_text='Отзыв на кыргызском языке', null=True, verbose_name='Текст отзыва (кырг.)')),
                ('avatar', models.ImageField(blank=True, help_text='Аватар автора отзыва', null=True, upload_to='avatars/', verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-created_at'],
            },
        ),
    ]
