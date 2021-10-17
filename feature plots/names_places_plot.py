# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:05:29 2021

@author: Beck
"""


import csv
import pandas as pd
import nltk
import matplotlib.pyplot as plt


df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

df["tweet_tokenized"]

NNP_list = []
print(df["tweet_tokenized"])

for tweet in df["tweet_tokenized"]:
    pos_tagged = nltk.pos_tag(df["tweet_tokenized"])
    counter = 0
    for word in pos_tagged:
        if word == "NNP":
            counter += 1
    NNP_list.append(counter)
    
print(pos_tagged)
#####################does not work yet printing of different NNP is still difficult

plt.plot(x = NNP_list)
plt.ylabel("number of tweets")
plt.xlabel("percentage of NNP")

###########################################################

print(df["tweet_tokenized"])

for tweet in df["tweet_tokenized"]:
    counter = 0
    for word in tweet:
        if word == "NNP":
            counter += 1
    NNP_list.append(counter/len(tweet))
    
print(NNP_list)
    
    
