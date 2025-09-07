from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add, name = 'add'),
    path('1', views.home, name='home'),
    path('welcome', views.welcome, name='welcome'),
]