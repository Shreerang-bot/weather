#this is my view.py file
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Shreerang'})
    # return HttpResponse('Hello World')

def about(request):
    return render(request, 'about.html')
