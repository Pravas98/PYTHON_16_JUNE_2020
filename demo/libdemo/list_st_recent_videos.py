import re
import requests
from bs4 import BeautifulSoup

homepage = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(homepage.text, "lxml-xml")
for itemtag in bs.find_all("item"):
    title = itemtag.find("title").text
    if title.startswith("Video"):
        print(re.sub(r'\s+', ' ', title))
