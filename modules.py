from monkeylearn import MonkeyLearn
import json
import 
 

def jprint(obj):
    print(len(obj))
    for i in range(len(obj)):
        temp=obj[i]['classifications'];temp=temp[0]['confidence']
        res=obj[i]['classifications'];res=res[0]['tag_name']
        print("Results show that the product is {} % {}".format(temp*100,res))

ml = MonkeyLearn('7cf596afbe22f32ca0a88479f5731feeba294f30')
data = ['The restaurant was great!', 'The curtains were disgusting']
model_id = 'cl_pi3C7JiL'
result = ml.classifiers.classify(model_id, data)
jprint(result.body)
