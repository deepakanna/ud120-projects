#!/usr/bin/python3
import os
import joblib
import sys
import matplotlib.pyplot
sys.path.append(os.path.abspath("../tools/"))
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
print(data_dict)
### your code below
for i in data:
    salary=i[0]
    bonus=i[1]
    matplotlib.pyplot.scatter(salary,bonus)

matplotlib.pyplot.xlabel("Salary")
matplotlib.pyplot.ylabel("Bonus")
matplotlib.pyplot.show()
#print(o)
b=1
print("length is",len(data_dict))
for i in data_dict:
#    if(data_dict[i]['salary']>250000):
     #if(data_dict[i]['bonus']!='NaN' and data_dict[i]['bonus']>100000):
   if(data_dict[i]['bonus']!='NaN' and int(data_dict[i]['bonus'])>b):
        b=int(data_dict[i]['bonus'])
        ind=i
print(b)
print(ind)
data_dict.pop(ind,0)
print("length is",len(data_dict))

data = featureFormat(data_dict, features)
for i in data:
    salary=i[0]
    bonus=i[1]
    matplotlib.pyplot.scatter(salary,bonus)

matplotlib.pyplot.xlabel("Salary")
matplotlib.pyplot.ylabel("Bonus")
matplotlib.pyplot.show()

names=[]
for i in data_dict:
#    if(data_dict[i]['salary']>250000):
     #if(data_dict[i]['bonus']!='NaN' and data_dict[i]['bonus']>100000):
   if(data_dict[i]['bonus']!='NaN' and int(data_dict[i]['bonus'])>5000000) and (data_dict[i]['salary']!='NaN' and int(data_dict[i]['salary'])>1000000):
        names.append(i)
print(names)
mm=0
import math
mn=math.inf
for i in data_dict:
    if(data_dict[i]["exercised_stock_options"]!='NaN'):
        if(data_dict[i]["exercised_stock_options"]>mm):
            mm=data_dict[i]["exercised_stock_options"]
        if (data_dict[i]["exercised_stock_options"] < mn):
            mn = data_dict[i]["exercised_stock_options"]

print(mm,"  ",mn)

mm=0
import math
mn=math.inf
for i in data_dict:
    if(data_dict[i]["salary"]!='NaN'):
        if(data_dict[i]["salary"]>mm):
            mm=data_dict[i]["salary"]
        if (data_dict[i]["salary"] < mn):
            mn = data_dict[i]["salary"]

print(mm,"  ",mn)