# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:17:39 2021

@author: Beck
"""

import nltk
import numpy as np
from nltk.tokenize import RegexpTokenizer
from code.feature_extraction.feature_extractor import FeatureExtractor
from code.util import COLUMN_TWEET


class NamesPlacesFeature(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_NNP".format(input_column))
    
    def _get_values(self, inputs):

        nnp_perc = []
        for tweet in inputs[0]:
            tokenizer = RegexpTokenizer(r'\w+')
            words = tokenizer.tokenize(tweet)
            pos_tagged = nltk.pos_tag(words)
            counter = 0
            for i in pos_tagged:
                for j in i:
                    if j == "NNP":
                        counter += 1
            nnp_perc.append(counter/len(pos_tagged))

        cor_shape = np.array(nnp_perc)
        cor_shape = cor_shape.reshape(-1,1)
        print(cor_shape[:10])
        
        return cor_shape