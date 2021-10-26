# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:13:59 2021

@author: Beck
"""

import nltk
from code.feature_extraction.feature_extractor import FeatureExtractor
import numpy as np

class TweetFrequency(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_tweet_frequency".format(input_column))

        
        
    def _get_values(self, inputs):
        
        import pandas as pd
        import csv
        data_f = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")
        inputs = data_f[:100]
        
        freq_list = []
        freq_dist = nltk.FreqDist(inputs[0])
        
        print(inputs[0])
        
        for tweet in inputs[0]:
            freq_list.append(freq_dist.get(tweet))
        cor_shape = np.array(freq_list)
        cor_shape = cor_shape.reshape(-1, 1)
        return cor_shape
    
    
    
    
    
        
     