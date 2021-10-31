# -*- coding: utf-8 -*-
"""
Feature that counts the number of NNPs (Proper Nouns) in each tweet.

Created on Wed Oct 13 13:17:39 2021

@author: joldach
"""

import nltk
import numpy as np
from nltk.tokenize import RegexpTokenizer
import sys
sys.path.append('./scripts/')
from scripts.feature_extraction.feature_extractor import FeatureExtractor

class NamesPlacesFeature(FeatureExtractor):
    
    #constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_NNP".format(input_column))
    
    # don't need to fit, so don't overwrite _set_variables()
    
    def _get_values(self, inputs):

        # create empty list
        nnp_perc = []
        tokenizer = RegexpTokenizer(r'\w+')

        # Use NER package on each tweet in column and return the number of NNPs in each tweet
        for tweet in inputs[0]:
            words = tokenizer.tokenize(tweet)
            pos_tagged = nltk.pos_tag(words)
            my_dict = dict(pos_tagged)
            nnp_perc.append(sum(value == "NNP" for value in my_dict.values())/len(pos_tagged))
            
        # changes the shape of the list into a column
        result = np.array(nnp_perc)
        result = result.reshape(-1,1) 
            
        return result
