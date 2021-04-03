import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 


headers = {'User-Agent':Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36}
url = 'https://www.ebay.ca/b/Nike-Mens-T-Shirts/15687/bn_701356' 
results = requests.get(url,headers=headers)

#instantiate to the beautifulsoup library
soup = BeautifulSoup(results.text,'html.parser')

#create empty lists for data storage
item_title= []
Price = []
Trending_Price = []
Shipping = []
Hotness = []

shirt_div = soup.find_all('div',class_='s-item__info clearfix')

#create a loop to iterate through the container that represents the entire page
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
    
#create a datafrane called nike_df and store all the items within the container.        
nike_df = pd.DataFrame({
'Item name':item_title,
'Price': Price,
'Trending_Price':Trending_Price,
'Shipping': Shipping,
'Hotness': Hotness})

print(nike_df)
