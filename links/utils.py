import requests
import lxml
from bs4 import BeautifulSoup

def get_link_data(url):
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Acceot-Language":"en",
    }
    
    response = requests.get(url,headers = headers)

    soup = BeautifulSoup(response.text,'lxml')

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector=".a-price-whole").getText()
    price = float(price.replace(',',''))

    return name,price