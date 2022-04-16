from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from shortener.models import LongShortUrl


def index(request):
    template = 'index.html'
    context = {
        'text': 'hello world'
    }
    return render(request, template, context)


class IndexView(CreateView):
    template_name = 'index.html'
    model = LongShortUrl
    fields = ('long', 'short', 'is_public')
    success_url = reverse_lazy('shortener:index')
