from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {}
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponse(template.render(context, request))
    return render(request, 'dashboard/index.html', context)
