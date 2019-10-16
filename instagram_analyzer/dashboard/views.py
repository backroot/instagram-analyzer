from django.shortcuts import render
from django.http import HttpResponse

import json
import instagram_explore as ie

def index(request):
    res = ie.user('kirin_brewery')    
    context = { 'data': json.dumps(res.data, indent=2, ensure_ascii=False)}
    return render(request, 'dashboard/index.html', context)

def login(request):
    context = {}
    return render(request, 'dashboard/login.html', context)
