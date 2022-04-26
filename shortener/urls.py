from django.urls import path

from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('me/', views.ProfileView.as_view(), name='profile'),
    path('<str:url>/', views.CustomRedirectView.as_view(), name='redirect'),

]
