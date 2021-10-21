# -*- coding: utf-8 -*-
"""
Feature that extracts the most common hashtags, to be stored in a bag of words.
It will then go through each tweet and check how many of the top used hashtags have been used.

Created on Thu Oct 21 11:23:21 2021

@author: jch
"""

import numpy as np
import nltk
import itertools
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the most common hashtags
class HashtagsMostCommon(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_hashtags_most_common".format(input_column))
        
    def _get_values(self, inputs):
        
        # pre-processing
        hasch = inputs[["hashtags", "label"]]
        viral_tweets = hasch.loc[(hasch.label == True)]
        haschis = viral_tweets["hashtags"]

        hashtags = []
        
        # extract hashtags
        for h in haschis:
            if len(h) > 2:
                tags = h.split("'")
                words = [t for t in tags if t.isalnum()]
                hashtags.append(words)
        
        # combine tags in a flat list
        flat_hasch = list(itertools.chain(*hashtags))
        
        # extract most common tags
        freq = nltk.FreqDist(flat_hasch)
        most_common_tags = freq.most_common(20)
        
        # check for each tweet how many of the most common hashtags are included
        counts = []

        for h in hasch:
            counter = 0
    
            if len(h) > 2:
                tags = h.split("'")
                words = [t for t in tags if t.isalnum()]
        
                for w in words:
                    if any(w in tag for tag in most_common_tags):
                        counter += 1
    
        counts.append(counter)
        
        result = np.array(counts)
        
        return result, most_common_tags
