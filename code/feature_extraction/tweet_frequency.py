# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:13:59 2021

@author: Beck
"""

import nltk
from code.feature_extraction.feature_extractor import FeatureExtractor
import csv
import numpy as np
import pandas as pd

class TweetFrequency(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_tweet_frequency".format(input_column))
        self.data_f = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

        
        
    def _get_values(self, inputs):

        freq_list = []
        my_dict = dict()
        
        freq_dist = nltk.FreqDist(inputs)

        for user, freq in freq_dist.items():
            my_dict[user] = (freq)
        
        for username in inputs:
            freq_list.append(my_dict.get(username))
        cor_shape = np.array(freq_list)
        cor_shape = cor_shape.reshape(-1, 1)
        print(cor_shape)
        return cor_shape
    
    
    
    
    
        
     
