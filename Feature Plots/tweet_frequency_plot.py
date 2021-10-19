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

freq_dist = nltk.FreqDist(df["username"])

different_values = []
different_users = []
for x in range(1, 300):
    key_list = [key for (key, value) in freq_dist.items() if value == x]
    # the amount of tweets
    different_values.append(x)
    # the amount of users that had that amount of tweets
    different_users.append(len(key_list))


plt.plot(different_values, different_users)
plt.ylabel("number of users")
plt.xlabel("number of tweets")
plt.yscale('log')
