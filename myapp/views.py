from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    response= requests.get('https://api.covid19api.com/countries').json()

    params = {
        'response':response
    }
    return render(request, 'index.html',params)
# def data(request):
   

#     return render(request, 'index.html',params)