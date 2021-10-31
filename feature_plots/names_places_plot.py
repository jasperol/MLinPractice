# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:05:29 2021

@author: joldac
"""

import csv
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer

df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

viral_tweets = df.loc[df["label"] == True]
non_viral_tweets = df.loc[df["label"] == False]

# Function that emulates the feature aswell as sorts the returned data for plotting
def NNP_function(input):
    NNP_list = []
    # use a sample amount of 2000 tweets to display the distribution of high frequency NNP use
    for text in input["tweet"][:1000]:
        tokenizer = RegexpTokenizer(r'\w+')
        words = tokenizer.tokenize(text)
        pos_tagged = nltk.pos_tag(words)
        counter = 0
        for i in pos_tagged:
            for j in i:
                if j == "NNP":
                    counter += 1
            NNP_list.append(counter)

    # count how many tweets have a certain number of NNP words 
    number_NNP = []
    for x in NNP_list:
        number_NNP.append((x, NNP_list.count(x)))
    
    
    # splits the list into two lists, one containing the NNP count,
    #and the other the amount of tweets with the respective NNP counts
    NNP_count = []
    amount = []

    for NNP_percentage, count in number_NNP:
        NNP_count.append(NNP_percentage)
        amount.append(count)
    
    return NNP_count, amount

x1, y1 = NNP_function(viral_tweets)
x2, y2 = NNP_function(non_viral_tweets)

plt.bar(x1, y1, label = 'viral') 
plt.bar(x2, y2, label = 'non-viral')
plt.ylabel("Number of tweets")
plt.xlabel("NNP word count per tweet")
plt.title('NNP amount distribution')
plt.legend(loc = 'upper right')




    
