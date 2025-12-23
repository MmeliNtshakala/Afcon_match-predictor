import requests
from bs4 import BeautifulSoup

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

print(soup)