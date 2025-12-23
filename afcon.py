import requests
from bs4 import BeautifulSoup

link = "https://www.transfermarkt.com"
afcon_link = f"{BASE_URL}/africa-cup-of-nations/startseite/pokalwettbewerb/AFCN?saison_id=2024"

HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
                "AppleWebKit/537.36 (KHTML, like Gecko) " 
                "Chrome/120.0.0.0 Safari/537.36" 
}

response = requests.get(afcon_link, headers=HEADERS)