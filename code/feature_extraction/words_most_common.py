# -*- coding: utf-8 -*-
"""
Feature that extracts the most common words in all tweets, to be stored in a bag of words.
It will then go through each tweet and check how many of the top used words have been used.

Created on Thu Oct 21 11:23:21 2021

@author: jch
"""

import numpy as np
import nltk
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the most common hashtags
class WordsMostCommon(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_tweet_words_most_common".format(input_column))
        
    def _get_values(self, inputs):
        
        # function to drop special characters
        def join_char(word):
            new = ''.join(char for char in word if char.isalnum())
            return new
        
        # pre-processing
        tweets_and_labels = inputs[["tweet_tokenized", "label"]]
        viral_tweets = inputs.loc[(tweets_and_labels.label == True)]
        tweets_column = viral_tweets["tweet_tokenized"]
        
        # concatenate all tweets into one text
        text = ' '.join(tweet for tweet in tweets_column)
        
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
        most_common_words = freq.most_common(50)
        
        # check for each tweet how many of the most common words are included
        tweets = inputs["tweet_tokenized"]
        counts = []

        for t in tweets:
            counter = 0
    
            words = t.split("'")
            tokens = [w for w in words if w.isalnum()]
        
            for token in tokens:
                if any(token in mcw for mcw in most_common_words):
                    counter += 1
        
            counts.append(counter)
        
        result = np.array(counts)
        
        return result
        
        
        