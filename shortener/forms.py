from django import forms

from shortener.models import LongShortUrl


class URLForm(forms.ModelForm):
    class Meta:
        model = LongShortUrl
        fields = ('long', 'short', 'is_public')
