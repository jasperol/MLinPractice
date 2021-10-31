# -*- coding: utf-8 -*-
"""
Visualisation of the most common words in all tweets

Created on Thu Oct 21 15:23:47 2021

@author: jch
"""

import pandas as pd
import csv
import nltk
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# load the data
data = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

# store tweet column
tweets = data["tweet"]

# function to drop special characters
def join_char(word):
    new = ''.join(char for char in word if char.isalnum())
    return new

# concatenate all tweets into one text
text = ' '.join(tweet for tweet in tweets)

# tokenize text
token_list = list(text.split(","))

# drop special characters
tokens = [join_char(token) for token in token_list]

# filter for empty strings and remove stopwords
tokens_final = list(filter(lambda x: x != "", tokens))
tokens_noStopWords = [word for word in tokens_final if word.lower() not in ENGLISH_STOP_WORDS]

# filter for 's' & 'll'
tokens_fixed = list(filter(lambda x: x != "s", tokens_noStopWords))
tokens_clear = list(filter(lambda x: x != "ll", tokens_fixed))

# extract most common words
freq = nltk.FreqDist(tokens_clear)
most_common_words = freq.most_common(20)

# plotting the 20 most common words and their counts
x = most_common_words[0]
fig,ax = plt.subplots(1,1)
ax.set_xlabel('top 20 words')
ax.set_ylabel('occurences')
plt.xticks(rotation=90)
plt.plot(x, most_common_words[1])