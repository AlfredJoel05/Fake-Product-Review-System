from bs4 import BeautifulSoup as bs
import requests,json
import pandas as pd
#link="https://www.flipkart.com/samsung-galaxy-s9-midnight-black-64-gb/p/itmf33a69rpszgzn?pid=MOBF2VWVBGCT5QQN&lid=LSTMOBF2VWVBGCT5QQN0ZJFUP&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=9442e503-d85a-467d-a371-0298e93d5120.MOBF2VWVBGCT5QQN.SEARCH&ppt=sp&ppn=sp&ssid=5wpwxh1qv40000001582347298427&qH=fe546279a62683de"
link=input("enter link:")
#print(link)
page = requests.get(link)
soup = bs(page.content,'html.parser')
#print((bs(page.content,'html.parser')))
categories=soup.find_all(class_='qwjRop')
print('\n',categories,'\n')
cat_name=str()
try:
	cat_name=[categories[comments].find(class_='_2t8wE0').get_text() for comments in range(len(categories))]
except:
	cat_name=[categories[comments].find(class_='').get_text() for comments in range(len(categories))]
with open('comments.json','w') as file:
	json.dump(cat_name,file,indent=4)
def cat():
    return cat_name
#DataFrameset=pd.DataFrame(cat_name).to_csv('Test.csv',index=False,encoding='utf-8')