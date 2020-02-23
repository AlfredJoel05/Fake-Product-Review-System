from monkeylearn import MonkeyLearn
import web_scraper,json
import pandas as pd
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
with open('comment_percentage.json','w') as file:
	temp={};obj=result.body
	for i in range(len(obj)):
		percentage=obj[i]['classifications'];percentage=percentage[0]['confidence']
		comment=obj[i]['text'];temp[comment]=percentage
	json.dump(temp,file,indent=4)
	pd.DataFrame({'comment':list(temp.keys()),'percentage':list(temp.values())}).to_csv('Test.csv',index=False,encoding='utf-8')
with open('sentimental_analysis_result.json','w') as file:
	json.dump(result.body,file,indent=4)
jprint(result.body)
with open('comment_type.json','w') as file:
	json.dump(dic,file,indent=4)
total_comments=[];
for i in dic.values():
    total_comments.extend(i)
for i in dic.keys():
    print(i,':',round(sum(dic[i])/sum(total_comments)*100,3))
    #print(i,':',round(sum(dic[i])/len(dic[i]),2))