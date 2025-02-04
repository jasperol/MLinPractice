# -*- coding: utf-8 -*-
"""
Feature that extracts the number of mentions.

Created on Sun Oct 31 12:05:48 2021

@author: jch
"""

import numpy as np
import sys
sys.path.append('./scripts/')
from scripts.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the number of mentions
class MentionsCounts(FeatureExtractor):

    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_num".format(input_column))
        
        # don't need to fit, so don't overwrite _set_variables()
        
    def _get_values(self, inputs):
        
        # pre-processing
        mentions = inputs[0]
        
        # count the occurences of 'id' which is equal to the number of mentions of another user
        counts = [m.count('id') for m in mentions]
        
        result = np.array(counts)
        result = result.reshape(-1,1)
        
        return result
