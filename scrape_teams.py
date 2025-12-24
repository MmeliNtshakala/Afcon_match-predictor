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

for header in soup.find_all(["h2", "h3"]):
    if "Qualified teams" in header.get_text():
        table = header.find_next("table", class_="wikitable")
        break


rows = table.find("tbody").find_all("tr")

for z in rows:
    colomns = z.find_all("td")
    if len(colomns) < 8:
        continue

    teams.append({
        "team": colomns[0].get_text(strip=True),
        "qualification" : colomns[1].get_text(strip=True),
        "appearances" : colomns[3].get_text(strip=True),
        "best_perfomance" : colomns[-2].get_text(strip=True),
        "fifa_Rank": colomns[1].get_text(strip=True)           
        })
        
dataframe = pd.DataFrame(teams)
dataframe.to_csv("afcon_teams.csv", index=False)

print(f"DONE {len(dataframe)} qualified")