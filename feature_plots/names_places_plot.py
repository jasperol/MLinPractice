# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:05:29 2021

@author: Beck
"""


import csv
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer



df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

#viral_tweets = df.loc[df["label"] == False]

NNP_list = []
# use a sample amount of 1000 tweets to display the distribution of high frequency NNP use
for text in df["tweet"][:5000]:
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)
    pos_tagged = nltk.pos_tag(words)
    counter = 0
    for i in pos_tagged:
        for j in i:
            if j == "NNP":
                counter += 1
    NNP_list.append(counter)
print(sum(NNP_list)/len(NNP_list))



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
    

plt.bar(NNP_count, amount)
plt.ylabel("amount of tweets")
plt.xlabel("NNP word count per tweet")




    
