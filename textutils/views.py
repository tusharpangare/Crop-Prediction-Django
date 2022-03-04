# I have created this file - tusharpangare ©
from __future__ import print_function
import pandas as pd 
import numpy as np   
from sklearn.metrics import classification_report   
from sklearn import metrics    
from sklearn.model_selection import cross_val_score
from django.http import HttpResponse
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def index(request):
    return render(request, 'index.html')

def analyze(request):
    crop = pd.read_csv("E:/Myspace_tushar/Project/Crop Prediction ML/Crop_recommendation.csv")
    crop.columns = crop.columns.str.replace(' ', '') 
    features = crop[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
    target = crop['label']
    acc = []
    model = []
    x_train, x_test, y_train, y_test = train_test_split(features,target,test_size = 0.2,random_state =2)
    RF = RandomForestClassifier(n_estimators=20, random_state=0)
    RF.fit(x_train,y_train)
    predicted_values = RF.predict(x_test)
    x = metrics.accuracy_score(y_test, predicted_values)
    acc.append(x)
    model.append('RF')


    N = request.POST.get('nitrogen', 'default')
    P = request.POST.get('phosphorous', 'default')
    K = request.POST.get('potassium', 'default')
    temp = request.POST.get('temperature', 'default')
    humidity = request.POST.get('humidity', 'default')
    ph =request.POST.get('ph', 'default')
    rainfall = request.POST.get('rainfall', 'default')

    userInput = [N, P, K, temp, humidity, ph, rainfall]
    result = RF.predict([userInput])[0]
    params = {'purpose':'Predicted Crop: ', 'analyzed_text': result.upper()}
    return render(request, 'analyze.html', params)    
