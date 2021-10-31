# -*- coding: utf-8 -*-
"""
Feature that returns the number of times a user has tweeted

Created on Wed Oct 13 21:13:59 2021

@author: joldach
"""

import nltk
import sys
sys.path.append('./scripts/')
from scripts.feature_extraction.feature_extractor import FeatureExtractor
import numpy as np

# Class that returns the number of times a user has tweeted
class TweetFrequency(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_tweet_frequency".format(input_column))

            # don't need to fit, so don't overwrite _set_variables()
        
    def _get_values(self, inputs):

        # create empty list and dictionary
        freq_list = []
        my_dict = dict()
        
        # get frequency distribution of usernames
        freq_dist = nltk.FreqDist(inputs[0])

        # convert array into dictionary
        for user, freq in freq_dist.items():
            my_dict[user] = (freq)
        
        # append frequency values of username to list
        for username in inputs[0]:
            freq_list.append(my_dict.get(username))
            
        # transform shape 
        result = np.array(freq_list)
        result = result.reshape(-1, 1)
        
        return result
    
    
    
    
    
        
     
