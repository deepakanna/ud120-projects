#!/usr/bin/python3"""     Starter code for exploring the Enron dataset (emails + finances);    loads up the dataset (pickled dict of dicts).    The dataset has the form:    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }    {features_dict} is a dictionary of features associated with that person.    You should explore features_dict as part of the mini-project,    but here's an example to get you started:    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000    """import pickleenron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))f1=open("../final_project/poi_names.txt","r")#import joblib#enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))#file_path = "../final_project/final_project_dataset_modified.pkl"#enron_data = pickle.load((open(file_path, "rb")), fix_imports=True)l=len(enron_data)print("The number of data points is ",len(enron_data))c=0for i in enron_data:    c=len(enron_data[i])print("The number of features for each person is ",c)count=0for i in enron_data:    if(enron_data[i]["poi"]==1):        count+=1print("The no. of POI in the dataset",count)for i in f1:    x=f1.readlines()[1:]print(x)print("The number of POIs were ",len(x))print("The total stock value of JAMES Prentice is ",enron_data["PRENTICE JAMES"]["total_stock_value"])print(enron_data)print("The no. of messages from wesley colwell to POI's is ",enron_data['COLWELL WESLEY']['from_this_person_to_poi'])print("The value of stock_optionsexercised by Jeffrey K Skilling is ",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])#print(len(f1.readlines())-1)s=0e=0t=0tp=0for i in enron_data:    if(enron_data[i]['salary']!='NaN'):        s+=1    if(enron_data[i]['email_address']!='NaN'):        e+=1    if(enron_data[i]['total_payments']=='NaN'):        t+=1print("The employees who have quantified salary are",s)print("The employees who have an email address are ",e)print(t)per=t/l*100print("The percentage of people in the dataset who have NaN for the total_payments is ", round(per))for i in enron_data:    if (enron_data[i]['poi'] == 1):        if (enron_data[i]['total_payments'] == 'NaN'):            tp += 1print("The % of the number of poi who have the total_payments NaN is ",tp,"%")