#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility file for collecting frequently used constants and helper functions.

Created on Wed Sep 29 10:50:36 2021

@author: lbechberger
"""

# column names for the original data frame
COLUMN_TWEET = "tweet"
COLUMN_LIKES = "likes_count"
COLUMN_RETWEETS = "retweets_count"
COLUMN_DATE = "date"
COLUMN_TAGS = "hashtags"
COLUMN_USERS = "username"
COLUMN_REPLIES = "replies_count"
COLUMN_MENTIONS = "mentions"

# column names of novel columns for preprocessing
COLUMN_LABEL = "label"
COLUMN_PUNCTUATION = "tweet_no_punctuation"
COLUMN_VIRAL_COUNT = "viralness"

SUFFIX_TOKENIZED = "_tokenized"
