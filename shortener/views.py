from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView
from django.views.generic.list import ListView

from shortener.forms import URLForm
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


class ProfileView(LoginRequiredMixin, ListView):
    http_method_names = ('get',)
    paginate_by = 5
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['form'] = URLForm()
        return context

    def get_queryset(self):
        author = self.request.user
        return author.urls.all()


class UpdateURL(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = URLForm
    model = LongShortUrl
    success_url = reverse_lazy('shortener:profile')

    def post(self, request, *args, **kwargs):
        print(args, kwargs)
        if 'confirm_delete' in self.request.POST:
            url = get_object_or_404(LongShortUrl, pk=kwargs.get('pk'))
            url.delete()
            messages.warning(request, 'ссылка удалена')

            return redirect(self.success_url)
        return super(UpdateURL, self).post(request, *args, **kwargs)
