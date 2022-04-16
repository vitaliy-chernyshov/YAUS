import string
from secrets import choice

ALLOWED_SYMBOLS = string.ascii_letters + string.digits


def gen_random_string(length=6):
    """Генерирует рандомную строку из букв и цифр. По умолчанию длина = 6"""
    return ''.join([choice(ALLOWED_SYMBOLS) for _ in range(length)])
