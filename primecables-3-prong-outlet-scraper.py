import requests, subprocess, sys
from bs4 import BeautifulSoup

URL = "https://www.primecables.ca/p-395617-cab-la-11"
PRICE_TO_BEAT = 3
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="product-price-395617")

price = float(results.contents[0].strip()[1:])

if price < PRICE_TO_BEAT:
    print(f"SALE! Thing is selling at {price}") 
    
    
result = subprocess.run([sys.executable, "-c", "print('ocean')"])
