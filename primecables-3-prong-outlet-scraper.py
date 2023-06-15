import requests, subprocess, sys
from bs4 import BeautifulSoup

def sendmail(subject, body):
  subprocess.run(["mail", "-s", subject, "abicelis@gmail.com"], input=body.encode('utf-8'))

URL = "https://www.primecables.ca/p-395617-cab-la-11"
PRICE_TO_BEAT = 3

try:
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find(id="product-price-395617")
  price = float(results.contents[0].strip()[1:])
  if price < PRICE_TO_BEAT:
    out = f"SALE! 'Multi Plug Outlet Extender 3-Prong' is on sale at PrimeCables at {price}"
    sendmail("Primecables scraper!", out)
  #raise Exception("Test")
except Exception as e:
  sendmail("Primecables scraper ERROR!", str(e))
