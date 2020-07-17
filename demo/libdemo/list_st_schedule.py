
import requests
from bs4 import BeautifulSoup

homepage = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(homepage.text, "html.parser")
table = bs.find("table", id="ctl00_ContentPlaceHolder1_GridView2")
for row in table.find_all('tr')[1:]:
    cols = row.find_all("td")
    print(f"{cols[0].text:20}  {cols[1].text:15}  {cols[2].text:10} {cols[5].text:3}")

