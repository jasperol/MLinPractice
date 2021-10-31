#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple (but effective) feature that counts the number of replies to a tweet

Created on Sat Oct 30 12:23:32 2021

@author: sascholle
"""

import numpy as np
import sys
sys.path.append('./scripts/')
from scripts.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the number of replies
class RepliesCount(FeatureExtractor):

    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_num".format(input_column))
        
    # don't need to fit, so don't overwrite _set_variables()
      
    # return the number of replies 
    def _get_values(self, inputs):
        
      replies = inputs[0]
        
      result = np.array(replies)
      result = result.reshape(-1,1)
        
      return result