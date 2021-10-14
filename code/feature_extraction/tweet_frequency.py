# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:13:59 2021

@author: Beck
"""

import nltk
from code.feature_extraction.feature_extractor import FeatureExtractor

class TweetFrequency(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_tweet_frequency".format(input_column))
    
    #def _set_variables(self, inputs):
        
        #df = pd.read_csv('data_analysis.csv', quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")
        
        
    def _get_values(self, inputs):
        
        self.df = ['a','b','a','a','c','c','b','a','d','a']
        self.freq_dist = nltk.FreqDist(self.df)
        print(self.freq_dist.items())
        
        return self.freq_dist.get(inputs)/len(self.df)
        
     