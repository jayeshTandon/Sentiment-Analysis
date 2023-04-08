#%%
# from analysis import analyseSentiment
import pandas as pd
from twitter_data import collectData
import importlib
import csv
import os
analysis = importlib.import_module('analysis')
twitter_data = importlib.import_module('twitter_data')

def setKeyword(key):
    global keyword 
    keyword = key


#%%
def prediction(count):
    global keyword
    global pred

    for i in range(0,count):
        collectData(keyword)

    if os.path.exists('csv_file.csv'):
        df = pd.read_csv('csv_file.csv')
        pred = analysis.analyseSentiment(data=df)

        print("PRED:: ", pred)
        
        total = 0
        for ele in range(0, len(pred)):
            total = total + pred[ele]

        average = total / len(pred)
        average = round(average,2)

        if average<0.45:
            return "Negative ",average
        elif average>=0.45 and average<=0.55:
            return "Neutral ",average
        else:
            return "Positive ",average