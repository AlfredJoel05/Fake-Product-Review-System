from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

page = requests.get("https://www.flipkart.com/samsung-galaxy-s9-midnight-black-64-gb/p/itmf33a69rpszgzn?pid=MOBF2VWVBGCT5QQN&lid=LSTMOBF2VWVBGCT5QQN0ZJFUP&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=9442e503-d85a-467d-a371-0298e93d5120.MOBF2VWVBGCT5QQN.SEARCH&ppt=sp&ppn=sp&ssid=5wpwxh1qv40000001582347298427&qH=fe546279a62683de")
soup = bs(page.content,'html.parser')
#print((bs(page.content,'html.parser')))
categories=soup.find_all(class_='qwjRop')
#print(categories)
cat_name=[categories[comments].find(class_='').get_text() for comments in range(len(categories))]
