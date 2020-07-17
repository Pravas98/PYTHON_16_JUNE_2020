
import requests
from bs4 import BeautifulSoup

homepage = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(homepage.text, "html.parser")
for atag in bs.find_all("a"):
    if 'href' in atag.attrs:
        href = atag['href']
        if href != '#':
            if href.startswith("http"):
                 print(href)
            else:
                print("http://www.srikanthtechnologies.com/" + href)


