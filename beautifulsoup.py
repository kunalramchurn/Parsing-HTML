import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 

url = 'https://www.ebay.ca/b/Nike-Mens-T-Shirts/15687/bn_701356' 
results = requests.get(url)

soup = BeautifulSoup(results.text,'html.parser')

#create empty lists for storage
item_title= []
Price = []
Trending_Price = []
Shipping = []
Hotness = []

#use find all function
shirt_div = soup.find_all('div',class_='s-item__info clearfix')

for container in shirt_div:
    title = container.h3.text
    item_title.append(title)

    price = container.find('span',class_='ITALIC')
    Price.append(price)

    trending_price= container.find('span',class_='STRIKETHROUGH')
    Trending_Price.append(trending_price)

    shipping = container.find('span',class_= 's-item__shipping s-item__logisticsCost')
    Shipping.append(shipping)

    hotness = container.find('span',class_= 's-item__hotness s-item__itemHotness')    
    Hotness.append(hotness)

nike_df = pd.DataFrame({
'Item name':item_title,
'Price': Price,
'Trending_Price':Trending_Price,
'Shipping': Shipping,
'Hotness': Hotness})

print(nike_df)