# -*- coding: utf-8 -*-
"""

Created on Sun Oct 17 13:40:18 2021

@author: joldach
"""

import matplotlib.pyplot as plt
import pickle
import numpy as np


with open("data/feature_extraction/training.pickle", "rb") as f_in:
    data = pickle.load(f_in)

# ensure the feature.extraction.sh file runs the training set using only the --tweet_frequency command and no other features
features = data["features"]
labels = data["labels"]

# creating viral and non-viral tweet labels
pos = features[labels]
neg_index = np.array([not x for x in labels])
neg = features[neg_index]

# plotting the histogram with normalised tweet numbers by defining density=True
plt.hist(pos, alpha = 0.5, label = 'viral', density = True) 
plt.hist(neg, alpha = 0.5, label = 'non-viral', density = True)
plt.title('Tweet Frequency distribution')
plt.xlabel('Number of tweets')
plt.ylabel('Percentage of users')
plt.legend(loc = 'upper right')

