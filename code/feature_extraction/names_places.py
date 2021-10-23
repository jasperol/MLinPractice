# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:17:39 2021

@author: Beck
"""

import nltk
from nltk.tokenize import RegexpTokenizer
from code.feature_extraction.feature_extractor import FeatureExtractor

class NamesPlacesFeature(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "{0}_NNP".format(input_column))
    
    def _get_values(self, inputs):

        
        import numpy as np
        import csv
        import pandas as pd
                
        df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")
        inputs = df["tweet"][:100]
        nnp_perc = []
        for tweet in inputs:
            tokenizer = RegexpTokenizer(r'\w+')
            words = tokenizer.tokenize(tweet)
            pos_tagged = nltk.pos_tag(words)
            counter = 0
            for i in pos_tagged:
                for j in i:
                    if j == "NNP":
                        counter += 1
            nnp_perc.append(counter/len(pos_tagged))

        print(np.array(nnp_perc))

        return nnp_perc 