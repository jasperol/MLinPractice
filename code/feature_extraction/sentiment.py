#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:36:51 2021

@author: Sabine Scholle
"""

from code.feature_extraction.feature_extractor import FeatureExtractor
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np

# class for creating a feature based on sentiment analysis from -1 (extremely negative) to 1 (extremely positive)
class Sentiment(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_sentiment".format(input_column)) 
        
    def _get_values(self, inputs):
        "analyse sentiment of the tweet"
            
        sentiment = SentimentIntensityAnalyzer()
    
        sentiment_score = [] 
        
        for tweet in inputs[0]:
            sent_tweet = sentiment.polarity_scores(tweet)
            sentiment_score.append(sent_tweet['compound'])
    
        return np.asarray(sentiment_score)
    
# Working miniture scale code as a test for the sentiment analysis class 


#print(sentiment.polarity_scores("This is gonna be epic if it is as amazing as I dream and hope"))

# example_sentences = [str('This is gonna be epic if it is as amazing as I dream and hope'), 
# str('or this could be terrible'), str('I am so full of hope and anxiety')]

# for text in example_sentences:
#     sent_tweet = sentiment.polarity_scores(text)
#     sentiment_score.append(sent_tweet['compound'])

# print(sentiment_score)

    