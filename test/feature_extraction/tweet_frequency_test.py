# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:14:23 2021

@author: Beck
"""

import unittest
import pandas as pd
import csv
from code.feature_extraction.tweet_frequency import TweetFrequency

class TweetFrequencyTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.tweet_frequency = TweetFrequency(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        
    def test_input_columns(self):
        self.assertEqual(self.tweet_frequency._input_columns, [self.INPUT_COLUMN])

    def test_tweet_frequency(self):
        expected_value = [1]
        self.data_f = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")
        input_text = self.data_f[:10000]

        result = self.tweet_frequency._get_values(input_text)
        print(max(result[:10000]))
        self.assertEqual(result[0], expected_value)
        
    
if __name__ == "__main__":
    unittest.main()