#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:18:05 2021

@author: sascholle
"""

import unittest
import numpy as np
import pandas as pd

from code.feature_extraction.sentiment import Sentiment
from code.util import COLUMN_TWEET

class SentimentTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.sentiment = Sentiment(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
    
    def test_boolean(self):
        self.assertEqual(True, not False)
        
    def test_input_columns(self):
        self.assertEqual(self.sentiment._input_columns, [self.INPUT_COLUMN])
        
    def test_sentiemt_expected_results(self):
        # a really positive tweet that should be at least greater than a neutral 0 sentiment score
        input_text = ["I really enjoy tweeting and hope that this will be the most positive tweet ever!"]
        self.df[self.INPUT_COLUMN] = [input_text]
        test_value = 0

        result = self.sentiment._get_values(input_text)
        self.assertGreater(result, test_value)
        
  
if __name__ == '__main__':
    unittest.main()
