# -*- coding: utf-8 -*-
"""
Feature that extracts the number of hashtags.

Created on Thu Oct 21 11:23:21 2021

@author: jch
"""

import numpy as np
import sys
sys.path.append('./scripts/')
from scripts.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the number of hashtags
class HashtagsCounts(FeatureExtractor):

    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_num".format(input_column))
        
    def _get_values(self, inputs):
        
        # pre-processing
        hasch = inputs[0]
        counts = []
        hashtags = []
        
        # extracting the number of hashtags from the length of the hashtag list
        for h in hasch:
            
            # if string contains hashtags
            if len(h) > 2:
                tags = h.split("'")
                words = [t for t in tags if t.isalnum()]
                counts.append(len(words))
                hashtags.append(words)
            
            # else is empty string
            else:
                counts.append(0)
        
        result = np.array(counts)
        result = result.reshape(-1,1)
        
        return result