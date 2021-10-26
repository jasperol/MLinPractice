#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 21:33:57 2021

@author: sascholle
"""

# plotting with matplotlib
import pickle
from matplotlib import pyplot as plt
import numpy as np

with open("data/feature_extraction/training.pickle", "rb") as f_in:
    data = pickle.load(f_in)

# ensure the feature.extraction.sh file runs the training set using only the --sentiment command and no other features
features = data["features"]
labels = data["labels"]

# creating viral and non-viral tweet labels
pos = features[labels]
neg_index = np.array([not x for x in labels])
neg = features[neg_index]

# plotting the histrogram with normalised tweet numbers by defining density=True
plt.hist(pos, alpha = 0.5, label = 'viral', density = True) 
plt.hist(neg, alpha = 0.5, label = 'non-viral', density = True)
plt.title('Tweet Sentiment Score Distribution')
plt.xlabel('Sentiment Polarity Score')
plt.ylabel('Normalised Number of Tweets')
plt.legend(loc = 'upper right')
