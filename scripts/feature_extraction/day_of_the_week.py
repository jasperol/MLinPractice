# -*- coding: utf-8 -*-

"""
Feature that translates the date of the tweet into the respective day of the week.

Created on Sun Oct 10 13:43:00 2021

@author: jchburmester
"""

import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import OneHotEncoder
from scripts.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the day of the week as feature
class DayOfTheWeek(FeatureExtractor):
    
    # constructor
    def __init__(self, input_column):
        # access superclass of all features
        super().__init__([input_column], "{0}_day_of_the_week".format(input_column))
    
    def _get_values(self, inputs):
        
        # further pre-processing
        inputs = np.array(inputs).reshape(-1,1)
        dates = pd.DataFrame(inputs)
        dates.rename(columns={ dates.columns[0]: "date" }, inplace = True)
        
        # add columns for weekdays
        # for numerical values
        dates.insert(1, 'weekday_num', value=np.zeros(shape=(len(dates), 1), dtype=int))
        
        # for days as words
        dates.insert(2, 'weekday_alph', value=np.zeros(shape=(len(dates), 1), dtype=int))
                  
        # sort and re-index
        dates_sorted = dates.sort_values(by='date', ascending=False)
        dates_newIdx = dates_sorted.reset_index(drop=True)
               
        # store weekday values in array, extract values, and add to dataframe
        dates_arr = np.array(dates_newIdx['date'])
        dates_list = []

        for date in dates_arr:
            dates_list.append(datetime.strptime(date, '%Y-%m-%d').weekday())

        dates_newIdx['weekday_num'] = dates_list
        
        # assign string to each value
        # pre-processing step for one hot encoder
        weekdays_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

        # store weekday values in array and extract days, and add to dataframe
        week = np.array(dates_newIdx['weekday_num'])
        days = []

        for value in week:
            days.append(weekdays_list[value])

        dates_newIdx['weekday_alph'] = days
        
        # implement one hot encoder
        # pre-processing
        weekdays = np.vstack((dates_list, days)).T
        weekdays_df = pd.DataFrame(weekdays)
        days_new = np.array(weekdays_df[0].astype('category'))
        days_new = days_new.reshape(-1,1)

        # load one hot encoder
        encoder = OneHotEncoder(sparse = False, handle_unknown = 'error')

        # fit and transform encoder on data
        onehot_week = np.array(encoder.fit_transform(days_new))
        
        result = onehot_week
        
        return result    
            