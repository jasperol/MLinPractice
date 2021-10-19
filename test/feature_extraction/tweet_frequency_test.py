# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:14:23 2021

@author: Beck
"""

""" Tests the tweet frequency feature by passing a user and checking to see if
the feature returns the correct tweet_frequency for that user """

import unittest
import pandas as pd
from code.feature_extraction.tweet_frequency import TweetFrequency

class TweetFrequencyTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.tweet_frequency = TweetFrequency(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        
    def test_input_columns(self):
        self.assertEqual(self.tweet_frequency._input_columns, [self.INPUT_COLUMN])

    def test_tweet_frequency(self):
        self.tweet_frequency._set_variables()
        expected_value = 1
        input_text = 'iampinglacson'

        result = self.tweet_frequency._get_values(input_text)
        self.assertEqual(result, expected_value)
        
    
if __name__ == "__main__":
    unittest.main()