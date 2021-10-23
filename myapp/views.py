from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    countries= requests.get('https://api.covid19api.com/countries').json()
    results= requests.get('https://api.covid19api.com/summary').json()['Global']
    response= requests.get('https://api.covid19api.com/').json()


    # print(results)

    params = {
        'countries':countries,
        'results':results,
        'response':response
    }
    return render(request, 'index.html',params)

def sports(request):
    response = requests.get('https://api.the-odds-api.com/v4/sports/?apiKey=e3926b49d9372f6cc79af6d3b1bd2b10')
    data=response.json()
    params={
        'data':data
    }
    return render(request,'sports.html',params)