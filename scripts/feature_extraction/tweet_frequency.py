# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:13:59 2021

@author: Beck
"""

import nltk
import sys
sys.path.append('./scripts/')
from scripts.feature_extraction.feature_extractor import FeatureExtractor
import numpy as np

class TweetFrequency(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_tweet_frequency".format(input_column))

        
        
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
        cor_shape = np.array(freq_list)
        cor_shape = cor_shape.reshape(-1, 1)
        print(cor_shape)
        return cor_shape
    
    
    
    
    
        
     
