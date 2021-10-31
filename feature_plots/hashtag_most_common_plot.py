# -*- coding: utf-8 -*-
"""
Visualisation of the most common hashtags in all tweets

Created on Thu Oct 21 15:23:47 2021

@author: jch
"""

import pandas as pd
import csv
import nltk
import itertools
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

# store data
hashtags = data["hashtags"]
haschis = []

# extract hashtags
for h in hashtags:
    if len(h) > 2:
        tags = h.split("'")
        words = [t for t in tags if t.isalnum()]
        haschis.append(words)
     
# combine tags in a flat list
flat_hasch = list(itertools.chain(*haschis))

# extract most common tags
freq = nltk.FreqDist(flat_hasch)
most_common_tags = freq.most_common(20)

# plotting the 20 most common tags and their counts
x = most_common_tags[0]
fig,ax = plt.subplots(1,1)
ax.set_xlabel('top 20 tags')
ax.set_ylabel('occurences')
plt.xticks(rotation=90)
plt.plot(x, most_common_tags[1])