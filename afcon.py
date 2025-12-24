import requests
from bs4 import BeautifulSoup
import pandas as pd 

link = "https://www.transfermarkt.com"
afcon_link = f"{link}/africa-cup-of-nations/startseite/pokalwettbewerb/AFCN?saison_id=2024"

# Headers to mimic browser

HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
                "AppleWebKit/537.36 (KHTML, like Gecko) " 
                "Chrome/120.0.0.0 Safari/537.36" 
}

# GET TEAMS 

response = requests.get(afcon_link, headers=HEADERS)
soup = BeautifulSoup(response.text, "lxml")


teams = [] # put the teams in this list 
table = soup.find("table", {"class": "items"})
rows  =  table.find_all("tr")

for x in rows[1:]:
    colomns = x.find_all("td")

    if colomns:
        teamName = colomns[1].get_text(strip=True)
        team_link = link + colomns[1].find("a")["href"]
        
        teams.append({"team": teamName, "link": team_link})


# Scrape players for each team
for team in teams:
    res = requests.get(team["link"], headers=HEADERS)
    team_soup = BeautifulSoup(res.text, "lxml")
    player_table = team_soup.find("table", {"class": "items"})

    players = []
    if player_table:
        for x in player_table.find_all("tr")[1:]:
            colomns = x.find_all("td")
            if len(colomns) >= 6:
                player_name = colomns[1].get_text(strip=True)
                position = colomns[4].get_text(strip=True)
                market_value = colomns[-1].get_text(strip=True)
                players.append({"name": player_name,
                               "position": position,
                               "market_value": market_value
                               })
            else:
                continue
    import time 
    team["players"] = players
    time.sleep(5)


df = pd.DataFrame(teams)
df.to_csv("Afcon_2024_teams.csv", index=False)

print("Scraping complete")
