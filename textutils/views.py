# I have created this file - tusharpangare ©

import pandas as pd   
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def index(request):
    return render(request, 'index.html')

def analyze(request):
    crop = pd.read_csv("dataset/Crop_recommendation.csv")

    # remove duplicate values
    crop.drop_duplicates()

    # handle null values in dataset
    attr=["N","P","K","temperature","humidity","rainfall","label"]
    if crop.isna().any().sum() !=0:
        for i in range(len(attr)):
            crop[atrr[i]].fillna(0.0, inplace = True)

    #Remove unwanted parts from strings in a column 
    crop.columns = crop.columns.str.replace(' ', '') 

    # we have given 7 features to the algorithm
    features = crop[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]

    # dependent variable is crop
    target = crop['label']

    # our model will contain training and testing data
    x_train, x_test, y_train, y_test = train_test_split(features,target,test_size = 0.2,random_state =2)
    
    # here n_estimators is The number of trees in the forest.
    # random_state is for controlling  the randomness of the bootstrapping
    RF = RandomForestClassifier(n_estimators=20, random_state=0)

    # we'll use rf.fit to build a forest of trees from the training set (X, y).
    RF.fit(x_train,y_train)
    # at this stage our algorithm is trained and ready to use
    
    # take values from user
    N = request.POST.get('nitrogen', 'default')
    P = request.POST.get('phosphorous', 'default')
    K = request.POST.get('potassium', 'default')
    temp = request.POST.get('temperature', 'default')
    humidity = request.POST.get('humidity', 'default')
    ph =request.POST.get('ph', 'default')
    rainfall = request.POST.get('rainfall', 'default')

    # make a list of user input
    userInput = [N, P, K, temp, humidity, ph, rainfall]
    
    # use trained model to predict the data based on user input
    result = RF.predict([userInput])[0]

    # display  result to the user
    params = {'purpose':'Predicted Crop: ', 'analyzed_text': result.upper()}
    return render(request, 'analyze.html', params)    
    
def about_us(request):
    return render(request, 'About_us.html')    