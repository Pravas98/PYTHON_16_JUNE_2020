from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html', {'trainer': 'Srikanth Pragada'})


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    return render(request, 'list_countries.html', {'countries': countries})


def get_country_info(request):
    if 'code' in request.GET:  # Is code present in request parameters
        code = request.GET['code']
        resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
        if resp.status_code == 200:
            country = resp.json()
            return render(request, 'country_info.html', {'country': country, 'code' : code})
        else:
            return render(request, 'country_info.html', {'code' : code,
                                                         'message': 'Country Not Found!'})
    else:
        return render(request, 'country_info.html')
