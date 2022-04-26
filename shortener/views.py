from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, RedirectView
from django.views.generic.list import MultipleObjectMixin

from shortener.models import LongShortUrl


class IndexView(SuccessMessageMixin, CreateView):
    http_method_names = ('get', 'post')
    template_name = 'index.html'
    model = LongShortUrl
    fields = ('long', 'short', 'is_public')
    success_url = reverse_lazy('shortener:index')
    success_message = '%(short_url)s'

    def form_valid(self, form):
        """Сохраняет автора для ссылки если пользователь авторизован"""
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            short_url=f'{self.object.short}',)


class CustomRedirectView(RedirectView):
    http_method_names = ('get',)

    def get_redirect_url(self, *args, **kwargs):
        url = LongShortUrl.objects.filter(short=kwargs['url']).first()
        if url:
            return url.long
        messages.warning(self.request, 'Такой ссылки нет в базе данных')
        return reverse('shortener:index')


class ProfileView(MultipleObjectMixin, LoginRequiredMixin, CreateView):
    http_method_names = ('get', 'post')
    paginate_by = 5
    model = LongShortUrl
    fields = ('long', 'short', 'is_public',)
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        author_urls = LongShortUrl.objects.filter(author=self.request.user.id)
        return super().get_context_data(object_list=author_urls, **kwargs)
