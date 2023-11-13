import requests, subprocess, sys
from bs4 import BeautifulSoup

def sendmail(subject, body):
  subprocess.run(["mail", "-s", subject, "abicelis@gmail.com"], input=body.encode('utf-8'))

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#URL = "https://fizz.ca/en/plp?default-max-price=1000&sort_by=field_displayorder_value&price__number[min]=0&price__number[max]=30000&field_tag_target_id[5096]=5096"
# Filters: "Google" and "Current offers"
URL = "https://fizz.ca/en/plp?default-max-price=1000&sort_by=field_displayorder_value&price__number[min]=0&price__number[max]=30000&field_devicebrand_target_id[5136]=5136&field_tag_target_id[5096]=5096"
mail_body = ""

try:
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find_all(class_="views-row")
  for result in results:
    product = result.find(class_="product-item")
    out_of_stock = result.find(class_="out-of-stock-tag")
    preloved = result.find(class_="preloved")

    if product != None:
      mail_body += "\n\n"
      mail_body += "Product name:" + product['data-productname'] + ":\n"
      mail_body += " - Preloved:" + ("No" if preloved == None else "Yes") + "\n"
      mail_body += " - Price:" + product['data-price'] + "\n"
      mail_body += " - In stock?:" + ("Yes!!" if out_of_stock == None else "No :(") + "\n"

  # Found something!
  if len(mail_body) > 0:
    mail_body = "Fizz deal scraper FOUND DEALS! Filters: 'Google' and 'Current offers'\n\n" + mail_body
    # print(mail_body)
    sendmail("Fizz deal scraper FOUND DEALS!", mail_body)
except Exception as e:
  # print("ERROR", e)
  sendmail("Fizz scraper ERROR!", str(e))