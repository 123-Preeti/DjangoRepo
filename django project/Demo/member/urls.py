from django.urls import path
from . import views

urlpatterns=[
    path('details', views.displayDetails, name = 'details'),
    path('home', views.home, name='home'),
]