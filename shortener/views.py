from django.shortcuts import render

def index(request):
    template = 'index.html'
    context = {
        'text': 'hello world'
    }
    return render(request, template, context)
