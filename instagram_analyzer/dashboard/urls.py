from django.urls import path

from . import views

urlpatterns = [
    path('login', views.index, name='index'),
    path('index', views.index, name='index'),
]
