# Generated by Django 3.2.13 on 2022-04-16 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LongShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.URLField(help_text='Введите оригинальную ссылку', max_length=1024, verbose_name='Длинная ссылка')),
                ('short', models.CharField(help_text='Опционально', max_length=1024, unique=True, verbose_name='Сокращенная ссылка')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('is_public', models.BooleanField(default=False, verbose_name='Публичная ссылка?')),
                ('author', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='urls', to=settings.AUTH_USER_MODEL, verbose_name='Автор ссылки')),
            ],
            options={
                'verbose_name': 'Короткая ссылка',
                'verbose_name_plural': 'Короткие ссылки',
            },
        ),
    ]
