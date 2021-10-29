#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Runs the specified collection of feature extractors.

Created on Wed Sep 29 11:00:24 2021

@author: lbechberger
"""

import argparse, csv, pickle, sys
import pandas as pd
import numpy as np

sys.path.append('./scripts/')
#sys.path.append('./scripts/feature_extraction/names_places')
#sys.path.append('./scripts/feature_extraction/sentiment')
#sys.path.append('./scripts/feature_extraction/tweet_frequency')
#sys.path.append('./scripts/feature_extraction/day_of_the_week')
#sys.path.append('./scripts/feature_extraction/hashtags_most_common')
#sys.path.append('./scripts/feature_extraction/hashtags_num')
#sys.path.append('./scripts/feature_extraction/words_most_common')
#sys.path.append('./scripts/feature_extraction/feature_collector')

from scripts.feature_extraction.character_length import CharacterLength
from scripts.feature_extraction.names_places import NamesPlacesFeature
from scripts.feature_extraction.sentiment import Sentiment
from scripts.feature_extraction.tweet_frequency import TweetFrequency
from scripts.feature_extraction.day_of_the_week import DayOfTheWeek
from scripts.feature_extraction.hashtags_most_common import HashtagsMostCommon
from scripts.feature_extraction.hashtags_num import HashtagsCounts
from scripts.feature_extraction.words_most_common import WordsMostCommon
from scripts.feature_extraction.feature_collector import FeatureCollector
from scripts.util import COLUMN_TWEET, COLUMN_LABEL, COLUMN_DATE, COLUMN_TAGS, COLUMN_USERS
#from util import COLUMN_RETWEETS, COLUMN_LIKES

# setting up CLI
parser = argparse.ArgumentParser(description = "Feature Extraction")
parser.add_argument("input_file", help = "path to the input csv file")
parser.add_argument("output_file", help = "path to the output pickle file")
parser.add_argument("-e", "--export_file", help = "create a pipeline and export to the given location", default = None)
parser.add_argument("-i", "--import_file", help = "import an existing pipeline from the given location", default = None)
parser.add_argument("-c", "--char_length", action = "store_true", help = "compute the number of characters in the tweet")
parser.add_argument("-s", "--sentiment", action = "store_true", help = "compute the sentiment score of the tweet")
parser.add_argument("-n", "--names_places", action = "store_true", help = "count number of names and places per tweet")
parser.add_argument("-f", "--tweet_frequency", action = "store_true", help = "count number of tweets by one user")
parser.add_argument("-w", "--weekday", action = "store_true", help = "extract the day of the week")
parser.add_argument("-h_mc", "--hashtags_most_common", action = "store_true", help = "counts how many of the most common hashtags have been used")
parser.add_argument("-h_n", "--hashtags_num", action = "store_true", help = "counts the number of hashtags")
parser.add_argument("-t", "--words_most_common", action = "store_true", help = "counts how many of the most common words have been used")

args = parser.parse_args()

# load data
df = pd.read_csv(args.input_file, quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

if args.import_file is not None:
    # simply import an exisiting FeatureCollector
    with open(args.import_file, "rb") as f_in:
        feature_collector = pickle.load(f_in)

else:    # need to create FeatureCollector manually

    # collect all feature extractors
    features = []
    
    if args.char_length:
        # character length of original tweet (without any changes)
        features.append(CharacterLength(COLUMN_TWEET))
        
    if args.sentiment:
        # sentiment score of tweet between -1 to 1
        features.append(Sentiment(COLUMN_TWEET))
        
    #if args.names_places:
        # amount of names and places per tweet
        #features.append(NamesPlacesFeature(COLUMN_TWEET))
        
    if args.tweet_frequency:
        # how many tweets posted by one person
        features.append(TweetFrequency(COLUMN_USERS))
        
    if args.weekday:
        # day of the week of the tweet
        features.append(DayOfTheWeek(COLUMN_DATE))
        
    if args.hashtags_most_common:
        # most common words
        features.append(HashtagsMostCommon(COLUMN_TAGS))
        
    if args.hashtags_num:
        # amount of hashtags
        features.append(HashtagsCounts(COLUMN_TAGS))
        
    if args.words_most_common:
        # most common words in the tweets
        features.append(WordsMostCommon(COLUMN_TWEET))
           
    # create overall FeatureCollector
    feature_collector = FeatureCollector(features)
    
    # fit it on the given data set (assumed to be training data)
    feature_collector.fit(df)

# apply the given FeatureCollector on the current data set
# maps the pandas DataFrame to an numpy array
feature_array = feature_collector.transform(df)

# get label array
label_array = np.array(df[COLUMN_LABEL])
label_array = label_array.reshape(-1, 1)

# store the results
results = {"features": feature_array, "labels": label_array, 
           "feature_names": feature_collector.get_feature_names()}

with open(args.output_file, 'wb') as f_out:
    pickle.dump(results, f_out)

# export the FeatureCollector as pickle file if desired by user
if args.export_file is not None:
    with open(args.export_file, 'wb') as f_out:
        pickle.dump(feature_collector, f_out)
