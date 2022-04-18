from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, RedirectView

from shortener.models import LongShortUrl


class IndexView(SuccessMessageMixin, CreateView):
    http_method_names = ('get', 'post')
    template_name = 'index.html'
    model = LongShortUrl
    fields = ('long', 'short', 'is_public')
    success_url = reverse_lazy('shortener:index')
    success_message = '%(short_url)s'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            short_url=self.object.short,)


class CustomRedirectView(RedirectView):
    http_method_names = ('get',)

    def get_redirect_url(self, *args, **kwargs):
        url = LongShortUrl.objects.filter(short=kwargs['url']).first()
        if url:
            return url.long
        messages.warning(self.request, 'Такой ссылки нет в базе данных')
        return reverse('shortener:index')
