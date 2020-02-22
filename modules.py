from monkeylearn import MonkeyLearn
import web_scraper
 
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
data = web_scraper.cat()
model_id = 'cl_pi3C7JiL'
result = ml.classifiers.classify(model_id, data)
jprint(result.body)
#print(dic)
total_comments=[];
for i in dic.values():
    total_comments.extend(i)
for i in dic.keys():
    print(i,':',round(sum(dic[i])/sum(total_comments)*100,3))
    #print(i,':',round(sum(dic[i])/len(dic[i]),2))