from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'dashboard/index.html', context)

def login(request):
    context = {}
    return render(request, 'dashboard/login.html', context)
