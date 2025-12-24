import requests
from bs4 import BeautifulSoup

link = "https://en.wikipedia.org/wiki/2025_Africa_Cup_of_Nations"

res = requests.get(link)
soup = BeautifulSoup(res.text, "html")

teams = []
tables = soup.find_all("table", class_= "wikitable")[:6]

for x, y in enumerate(tables):
    group = chr(65 +x)
    rows = y.find_all("tr")[1:]

    for z in rows:
        colomns = x.find_all("td")
        if len(colomns) >= 2:
            teams.append({
                "team": colomns[1].get_text(strip=True),
                "group" : group            
                })