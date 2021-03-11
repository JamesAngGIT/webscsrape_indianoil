print("hello world")
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

#import os
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# set URLs
#url = "https://www.alibaba.com/catalog/barite_cid90801?spm=a2700.details.debelsubf.5.7c2c2515lKlJtS"
url = "https://www.alibaba.com/product-detail/Low-Density-Polyethylene-LDPE-Resin-pellets_1600131873797.html?spm=a2700.gallery_search_cps.normalList.18.500d64d2d9tcf0"
driver.get(url)

# Initialisation
grade = []              # Film------DONE
competitor = []         # Company name
country = []            # China-------DONE
data_source = []        # alibaba-------
price_type = []         # Offer price
competitor_price = []   # Pull > 50 MT-------DONE
currency = []           # USD-----------DONE
UOM = []                # MT
packaging = []          # 25 kg--------DONE
products = []
date = []               # Date of request

#
content = driver.page_source
print(content)
soup = BeautifulSoup(content,features="html.parser
print(soup.prettify())

# Scraping
soup.title.string

competitor_price = soup.find_all(class_="pre-inquiry-price")[-1].get_text()
print(c)

currency = soup.find_all('label',class_= "ellipsis")[-1].get_text().split(" - ")[-1]
print(currency)

country = soup.find_all('div',class_ = "text-ellipsis")[0].get_text().split(", ")[-1]
print(country)

grade = soup.find_all('div',class_ = "text-ellipsis")[2].get_text().replace(' grade','')
print(grade)

for item in soup.find_all('dl',class_ = "do-entry-item"):
    #print(item.get_text())

    if 'Place of Origin:' in item.get_text():
        country = item.get_text().split(':')[-1].split(", ")[-1]
        print(country)

    elif 'Model Number:' in item.get_text():
        grade = item.get_text().split(':')[-1].replace(' grade','')
        print(grade)

    elif 'Package:' in item.get_text():
        package = item.get_text().split(':')[-1].split('/')[0]
        print(package)

    elif 'Payment term:' in item.get_text():
        payment_term = item.get_text().split(':')[-1]
        print(payment_term)
