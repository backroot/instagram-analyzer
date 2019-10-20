from django.urls import path

from . import views

urlpatterns = [
    path('index',       views.index,       name='index'),
    path('add_account', views.add_account, name='add_account'),
]
