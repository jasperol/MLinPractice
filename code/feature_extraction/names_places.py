# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:17:39 2021

@author: Beck
"""

import nltk
import numpy as np
from nltk.tokenize import RegexpTokenizer
from code.feature_extraction.feature_extractor import FeatureExtractor

class NamesPlacesFeature(FeatureExtractor):
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_NNP".format(input_column))
    
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
        cor_shape = np.array(nnp_perc)
        cor_shape = cor_shape.reshape(-1,1)             
        return cor_shape
