from django.urls import path

from . import views

urlpatterns = [
    path('login', views.index, name='login'),
    path('index', views.index, name='index'),
]
