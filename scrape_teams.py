import requests
from bs4 import BeautifulSoup
import pandas as pd

link = "https://en.wikipedia.org/wiki/2025_Africa_Cup_of_Nations"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
}

res = requests.get(link, headers=HEADERS)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

teams = []
tables = soup.find_all("table", class_= "wikitable")[:6]

for x, table in enumerate(tables):
    group = chr(65 +x)
    rows = table.find_all("tr")[1:]

    for z in rows:
        colomns = z.find_all("td")
        if len(colomns) >= 2:
            teams.append({
                "team": colomns[1].get_text(strip=True),
                "group" : group            
                })
dataframe = pd.DataFrame(teams)
dataframe.to_csv("afcon_teams.csv", index=False)

print("DONE")