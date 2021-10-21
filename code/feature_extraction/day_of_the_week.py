# -*- coding: utf-8 -*-

"""
Simple feature that translates the date of the tweet into the respective day of the week.

Created on Sun Oct 10 13:43:00 2021

@author: jchburmester
"""

import numpy as np
import daytime
from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the day of the week as feature
class DayOfTheWeek(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{1}_day_of_the_week".format(input_column))
        
        # don't need to fit, so don't overwrite _set_variables()
        
    # translate the input into day of the week format as integers
    # '0' for Monday, '6' for Sunday
    def _get_values(self, inputs):
        result = np.array(inputs[0])
        print(type(inputs[0]))
        return result        
            