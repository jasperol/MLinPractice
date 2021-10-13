# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:15:45 2021

@author: Beck
"""


import unittest
import pandas as pd
from code.feature_extraction.names_places import NamesPlacesFeature
import nltk

class NamesPlacesFeatureTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.names_places_feature = NamesPlacesFeature(self.INPUT_COLUMN)
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = ["This is a string with names, John is a person who lived in madagascar and Tom was from london"]
        
    def test_input_columns(self):
        self.assertEqual(self.names_places_feature._input_columns, [self.INPUT_COLUMN])

    def test_feature_name(self):
        self.assertEqual(self.names_places_feature.get_feature_name(), self.INPUT_COLUMN + "_names_places")

    def test_names_places(self):
         
        input_text = "This is a string with names, John is a person who lived in madagascar and Tom was from london"
        df[self.INPUT_COLUMN] = [input_text]
        counted_NNP = self.names_places.fit_transform(df)
        
        self.names_places_feature.fit(self.df)
        expected_value = 2
        
        self.assertEqual(freq_list[0][0], EXPECTED_BIGRAM)

        self.assertEqual(counted_NNP[self.OUTPUT_COLUMN[0]], output_val)
    
if __name__ == "__main__":
    unittest.main()