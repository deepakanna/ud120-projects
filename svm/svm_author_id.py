#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
#clf=svm.SVC(kernel="linear")
#clf=svm.SVC(kernel="rbf",C=1.0)
clf=svm.SVC(kernel="rbf",C=10000)
#clf=svm.SVC(kernel="rbf")

#########################################################

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''
t0 = time()
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]
clf.fit(features_train,labels_train)
print("Training Time:", round(time()-t0, 3), "s")

t0=time()
pred=clf.predict(features_test)
print("Predicting Time:", round(time()-t0, 3), "s")
acc=accuracy_score(pred,labels_test)
print(acc)
a1=pred[10]
a2=pred[26]
a3=pred[50]
print(a1)
print(a2)
print(a3)
rep=classification_report(labels_test,pred)
print(sum(pred))
#########################################################
