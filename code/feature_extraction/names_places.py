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

        import pandas as pd
        import csv
        import numpy as np

        df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")
        input_text = df["tweet"][:1000]      
        
        nnp_perc = []
        tokenizer = RegexpTokenizer(r'\w+')

        for tweet in input_text:
            words = tokenizer.tokenize(tweet)
            pos_tagged = nltk.pos_tag(words)
            my_dict = dict(pos_tagged)
            nnp_perc.append(sum(value == "NNP" for value in my_dict.values())/len(pos_tagged))
            
        cor_shape = np.array(nnp_perc)
        cor_shape = cor_shape.reshape(-1,1)     
        
        return cor_shape
