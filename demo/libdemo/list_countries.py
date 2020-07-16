import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for country in sorted(countries, key=lambda c: c['population'], reverse=True):
    print(f"{country['name']:50}  {country['capital']:30} {country['region']:15} {country['population']:10}")