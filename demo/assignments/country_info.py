import requests
import sys

def get_country(countries, code):
    for c in countries:
        if c['alpha3Code'] == code:
            return c
    else:
        return None


def get_country_name(countries, code):
    c = get_country(countries, code)
    if c is not None:
        return c['name']
    else:
        return None


resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()
print("Size of countries :", sys.getsizeof(countries), sys.getsizeof(countries[0]))
while True:
    code = input("Enter country code [exit to stop]:")
    if code == 'exit':
        break
    country = get_country(countries,code)
    if country is None:
        print("Sorry! Invalid country code!")
        continue

    # display info
    print(f"Name        : {country['name']}")
    print(f"Capital     : {country['capital']}")
    print(f"Region      : {country['region']}")
    print(f"Population  : {country['population']}")
    print("Sharing Border With:")
    for code in country["borders"]:
        print(get_country_name(countries,code))





