from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import LongShortUrl, User

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'urls_count')

    @admin.display(description='Кол-во ссылок у юзера')
    def urls_count(self, obj):
        return obj.urls.count()


@admin.register(LongShortUrl)
class URLAdmin(admin.ModelAdmin):
    list_display = ('pk', 'long', 'short', 'added_date', 'is_public', 'author')
    date_hierarchy = 'added_date'
    list_editable = ('author', 'is_public')
    search_fields = ('long',)
    list_filter = ('added_date', 'author', 'is_public')
    empty_value_display = '-пусто-'
