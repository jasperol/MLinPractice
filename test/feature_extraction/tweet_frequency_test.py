# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:14:23 2021

@author: Beck
"""

import unittest
import pandas as pd
from code.feature_extraction.tweet_frequency import TweetFrequency
import nltk

class TweetFrequencyTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.tweet_frequency = TweetFrequency(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        
    def test_input_columns(self):
        self.assertEqual(self.tweet_frequency._input_columns, [self.INPUT_COLUMN])

    def test_names_places(self):
        input_text = "John"
        self.df[self.INPUT_COLUMN] = [input_text]
        expected_value = 1 

        result = self.names_places_feature._get_values(input_text)
        self.assertEqual(result, expected_value)
        
    
if __name__ == "__main__":
    unittest.main()