#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AN NLTK Sentiment analysis feature that rates a tweet from -1 (most negative) to 1 (most postive) through 0 (neutral). 

Created on Sun Oct 10 20:36:51 2021

@author: sascholle 
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import sys
sys.path.append('./scripts/')
from scripts.feature_extraction.feature_extractor import FeatureExtractor

# class for creating a feature based on a sentiment score
class Sentiment(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_sentiment".format(input_column)) 
    
    # don't need to fit, so don't overwrite _set_variables()
    
    # compute the normalised sentiment score (so called compund score) for each tweet
    def _get_values(self, inputs):        
        sentiment = SentimentIntensityAnalyzer()
        sentiment_score = [] 
        
        for tweet in inputs[0]:
            sent_tweet = sentiment.polarity_scores(tweet)
            sentiment_score.append(sent_tweet['compound']) 
            
        result = np.asarray(sentiment_score)
        result = result.reshape(-1,1)
        
        return result
