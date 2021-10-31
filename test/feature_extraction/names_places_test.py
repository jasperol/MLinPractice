# -*- coding: utf-8 -*-
"""
Unit test for name_places.py

Created on Wed Oct 13 13:15:45 2021

@author: Beck
"""


import unittest
import pandas as pd
import csv
from scripts.feature_extraction.names_places import NamesPlacesFeature

class NamesPlacesFeatureTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.names_places_feature = NamesPlacesFeature(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        
    def test_input_columns(self):
        self.assertEqual(self.names_places_feature._input_columns, [self.INPUT_COLUMN])

    def test_names_places(self):
        df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")
        input_text = df["tweet"]
        self.df[self.INPUT_COLUMN] = [input_text]
        expected_value = 0.5

        result = self.names_places_feature._get_values(input_text)
        print(result[:10])
        self.assertEqual(result[2], expected_value)
        
    
if __name__ == "__main__":
    unittest.main()
