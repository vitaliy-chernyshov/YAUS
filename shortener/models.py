from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class LongShortUrl(models.Model):
    """Модель для сопоставления длинной и короткой ссылки"""

    long = models.URLField(
        max_length=1024,
        verbose_name='Длинная ссылка',
        help_text='Введите оригинальную ссылку'
    )
    short = models.CharField(
        max_length=1024,
        verbose_name='Сокращенная ссылка',
        help_text='Опционально',
        unique=True,
    )
    added_date = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True)
    is_public = models.BooleanField(
        verbose_name='Публичная ссылка?',
        default=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор ссылки',
        related_name='urls'
    )

    class Meta:
        verbose_name = 'Короткая ссылка'
        verbose_name_plural = 'Короткие ссылки'

    def __str__(self):
        return f'{self.long[:10]} - {self.short}'

