#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:36:51 2021

@author: Sabine Scholle
"""

from code.feature_extraction.feature_extractor import FeatureExtractor
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np

# class for creating a feature based on a sentiment score that ranges from -1 (extremely negative) to 1 (extremely positive)
class Sentiment(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_sentiment".format(input_column)) 
        
    def _get_values(self, inputs):
        "analyse sentiment of the tweet"
            
        sentiment = SentimentIntensityAnalyzer()
    
        sentiment_score = [] 
        
        # compute the sentiment score (ie compund score) for each of the tweets in the input column
        for tweet in inputs[0]:
            sent_tweet = sentiment.polarity_scores(tweet)
            sentiment_score.append(sent_tweet['compound']) 
        result = np.asarray(sentiment_score)
        result = result.reshape(-1,1)
        return result


#print(sentiment.polarity_scores("This is gonna be epic if it is as amazing as I dream and hope"))

"""
# Miniture Test 

example_sentences = [str('This is gonna be epic if it is as amazing as I dream and hope'), 
str('or this could be terrible'), str('I am so full of hope and anxiety')]

sentiment = SentimentIntensityAnalyzer()
sentiment_score = [] 

def test(example_sentences):
    for text in example_sentences:
        print(text)
        sent_tweet = sentiment.polarity_scores(text)
        sentiment_score.append(sent_tweet['compound'])
        
    result = np.asarray(sentiment_score)
    print(result)
    
    result = result.reshape(-1,1)
    return result

array = test(example_sentences)

print(array)
print(type(array))
(array.shape)
"""
