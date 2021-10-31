#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Three simple unit tests to check functionality of the sentiment.py feature

Created on Wed Oct 13 22:18:05 2021

@author: sascholle
"""

import unittest
import pandas as pd

from scripts.feature_extraction.sentiment import Sentiment

# class for running a few tests such as the input columns and if the result of the programme is as expected
class SentimentTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.sentiment = Sentiment(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        
    def test_input_columns(self):
        self.assertEqual(self.sentiment._input_columns, [self.INPUT_COLUMN])
        
    # test to see if a really positive tweet that should be scored greater than a 0 sentiment score (neutral)  
    def test_sentiemt_expected_results(self):
        input_text = ["I really enjoy tweeting and hope that this will be the most positive tweet ever!"]
        test_value = 0
        result = self.sentiment._get_values([input_text])
        self.assertGreater(result, test_value)
  
if __name__ == '__main__':
    unittest.main()
