from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    countries= requests.get('https://api.covid19api.com/countries').json()
    summary= requests.get('https://api.covid19api.com/summary').json()

    # print(summary)

    params = {
        'countries':countries,
        'summary':summary
    }
    return render(request, 'index.html',params)

def sports(request):
    response = requests.get('https://api.the-odds-api.com/v4/sports/?apiKey=e3926b49d9372f6cc79af6d3b1bd2b10')
    data=response.json()
    params={
        'data':data
    }
    return render(request,'sports.html',params)