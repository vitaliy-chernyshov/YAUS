from django.contrib.auth.views import (LoginView, LogoutView)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(
        template_name='login.html'), name='login'),

]
