#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 22:18:05 2021

@author: sascholle
"""

import unittest
import numpy as np

from code.feature_extraction.sentiment import Sentiment
from code.util import COLUMN_TWEET

class SentimentTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.sentiment = Sentiment(self.INPUT_COLUMN)
    
    def test_boolean(self):
        self.assertEqual(True, not False)
        
    def test_input_columns(self):
        self.assertEqual(self.sentiment._input_columns, [self.INPUT_COLUMN])
     
    def test_sentiment_score(self):
        result = self.sentiment._get_values(COLUMN_TWEET)
        print(result)
        #self.assertEqual(result, expected_value)
    
  



        
if __name__ == '__main__':
    unittest.main()
