#this is my view.py file
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.

def home(request):
    import json
    import requests

    if request.method == "POST":
        city = request.POST['city']
        api_request = requests.get( "http://api.airvisual.com/v2/city?city=" +city+ "&state=Maharashtra&country=India&key=495e4d8a-45b8-4f23-880e-da49142c9fbe")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})
    else:
        api_request = requests.get("http://api.airvisual.com/v2/city?city=Pune&state=Maharashtra&country=India&key=495e4d8a-45b8-4f23-880e-da49142c9fbe")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})
    # return HttpResponse('Hello World')

def about(request):
    return render(request, 'about.html')
