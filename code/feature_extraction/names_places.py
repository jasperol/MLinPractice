# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:17:39 2021

@author: Beck
"""

import nltk
from code.feature_extraction.feature_extractor import FeatureExtractor

class NamesPlacesFeature(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_NNP".format(input_column))
    
    def _get_values(self, inputs):
        
        inputs = "James Cameron is the person and London is a place but George also lives in Australia"
        sentences = nltk.sent_tokenize(inputs)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            pos_tagged = nltk.pos_tag(words)
        counter = 0
        for i in pos_tagged:
            for j in i:
                if j == "NNP":
                    counter += 1