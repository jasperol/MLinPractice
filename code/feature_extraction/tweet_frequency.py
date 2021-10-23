# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:13:59 2021

@author: Beck
"""

import nltk
from code.feature_extraction.feature_extractor import FeatureExtractor
import csv
import pandas as pd

class TweetFrequency(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_tweet_frequency".format(input_column))
        self.data_f = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

        
        
    def _get_values(self, inputs):
        
        freq_list = []
        for tweet in inputs:
            self.df = self.data_f["username"]
            self.freq_dist = nltk.FreqDist(self.df)
            freq_list.append = self.freq_dist.get(tweet)
        return freq_list
        
     