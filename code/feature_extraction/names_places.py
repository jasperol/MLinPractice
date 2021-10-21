# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:17:39 2021

@author: Beck
"""

""" this feature returns how many NNP (proper nouns/ names or places) a 
tweet contains """

import nltk
from code.feature_extraction.feature_extractor import FeatureExtractor
from nltk.tokenize import RegexpTokenizer


class NamesPlacesFeature(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_NNP".format(input_column))
    
    def _get_values(self, inputs):
                
        
        tokenizer = RegexpTokenizer(r'\w+')
        words = tokenizer.tokenize(inputs)
        pos_tagged = nltk.pos_tag(words)
        counter = 0
        for i in pos_tagged:
            for j in i:
                if j == "NNP":
                    counter += 1
        print(counter)
        nnp_perc = counter/len(pos_tagged)
        return nnp_perc 