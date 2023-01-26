from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.oauth_login, name='login'),
    path('redirect/', views.oauth_redirect, name='redirect'),
]
