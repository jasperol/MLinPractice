# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:40:18 2021

@author: Beck
"""

import csv
import pandas as pd
import nltk
import matplotlib.pyplot as plt


df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

# for the frequency of users I have to put the different frequencies in the x axis 
# and the amount of users with these amounts in the y axis

#bool_val = False
#viral_tweets = df.loc[df["label"] == bool_val]


freq_dist = nltk.FreqDist(df["username"])
freq_dist.items()


different_values = []
different_users = []
value_list = []
for x in range(1, 1000):
    key_list = [key for (key, value) in freq_dist.items() if value == x]
    value_list = [value for (key, value) in freq_dist.items()]
    # the amount of tweets
    different_values.append(x)
    # the amount of users that had that amount of tweets
    different_users.append(len(key_list))
    #list of numbers of tweets by users to determine average tweet frequency

#print("{0} average tweet count of {1} virals".format(sum(value_list)/len(value_list), bool_val))

plt.plot(different_values, different_users)
plt.ylabel("number of users")
plt.xlabel("number of tweets")
plt.yscale('log')
