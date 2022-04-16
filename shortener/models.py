from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from shortener.utils import gen_random_string

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
        blank=True,
        validators=(RegexValidator(
            r'^[a-zA-Z0-9]+$',
            'Короткая ссылка должна содержать только'
            'буквы латинского алфавита и/или цифры'),),
        error_messages={'unique': 'Такая короткая ссылка уже существует'}
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
        related_name='urls',
        default=User.get_anonymous_pk(),
    )

    class Meta:
        verbose_name = 'Короткая ссылка'
        verbose_name_plural = 'Короткие ссылки'

    def __str__(self):
        return f'{self.long[:10]} - {self.short}'

    def save(self, *args, **kwargs):
        if not self.short:
            # Generate ID once, then check the db. If exists, keep trying.
            self.short = gen_random_string()
            while LongShortUrl.objects.filter(short=self.short).exists():
                self.short = gen_random_string()
        super().save(*args, **kwargs)
