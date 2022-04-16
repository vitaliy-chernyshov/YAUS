from django import forms

from .models import LongShortUrl


class URLForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['text'].widget.attrs['placeholder'] = (
    #         'Введите какой нибудь текст, ну пожалуйста 😥'
    #     )
    #     self.fields['group'].empty_label = (
    #         'Выберите группу, если желаете 🙂'
    #     )

    class Meta:
        model = LongShortUrl
        fields = ('long', 'short', 'is_public')
