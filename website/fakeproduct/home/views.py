from django.shortcuts import render
from monkeylearn import MonkeyLearn
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Create your views here.
def home(requests):
    if requests.method == 'POST':
        link=requests.POST('link') + '/'
        page = requests.get(link)
        soup = bs(page.content,'html.parser')
        #print((bs(page.content,'html.parser')))
        categories=soup.find_all(class_='qwjRop')
        #print(categories)
        cat_name=[categories[comments].find(class_='').get_text() for comments in range(len(categories))]
        #DataFrameset=pd.DataFrame(cat_name).to_csv('Test.csv')   
        dic={}
        def jprint(obj):
            #print(len(obj))
            for i in range(len(obj)):
                percentage=obj[i]['classifications'];percentage=percentage[0]['confidence']
                comment=obj[i]['classifications'];comment=comment[0]['tag_name']
                print("Results show that the product is {} % {}".format(percentage*100,comment))
                if comment not in dic.keys():
                    dic[comment]=[percentage*100]
                elif comment in dic.keys():
                    dic[comment].append(percentage*100)

        ml = MonkeyLearn('640763d72f139f0d18caadb084a0ad3af213d920')
        model_id = 'cl_pi3C7JiL'
        result = ml.classifiers.classify(model_id, cat_name)
        jprint(result.body)
        #print(dic)
        total_comments=[];
        for i in dic.values():
            total_comments.extend(i)
        for i in dic.keys():
            print(i,':',round(sum(dic[i])/sum(total_comments)*100,3))
            data[i]=round(sum(dic[i])/sum(total_comments)*100,3)
    else:
        data={}
    return render(requests,'index.html',data)


def contact(request):
    return render(request,'contact.html',{})

#def work(requests):
     #link="https://www.flipkart.com/samsung-galaxy-s9-midnight-black-64-gb/p/itmf33a69rpszgzn?pid=MOBF2VWVBGCT5QQN&lid=LSTMOBF2VWVBGCT5QQN0ZJFUP&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=9442e503-d85a-467d-a371-0298e93d5120.MOBF2VWVBGCT5QQN.SEARCH&ppt=sp&ppn=sp&ssid=5wpwxh1qv40000001582347298427&qH=fe546279a62683de"
    
    #print(i,':',round(sum(dic[i])/len(dic[i]),2))
