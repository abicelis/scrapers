import requests, subprocess, sys
from bs4 import BeautifulSoup

def sendmail(subject, body):
  #print(subject, body)
  subprocess.run(["mail", "-s", subject, "abicelis@gmail.com"], input=body.encode('utf-8'))

URL = "https://www.newegg.ca/synology-ds423/p/N82E16822108830"
PRICE_TO_BEAT = 605
OUT_BODY = "SALE! 'Synology DS423' is on sale at Newegg.ca at {price}"
OUT_SUBJECT = "Newegg scraper!"

try:
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find("li", class_="price-current")

  price = float(results.get_text().strip()[1:])
  if price < PRICE_TO_BEAT:
    out = OUT_BODY.format(price = price)
    sendmail(OUT_SUBJECT, out)
  #raise Exception("Test")
except Exception as e:
  sendmail(OUT_SUBJECT + " - ERROR!", str(e))
