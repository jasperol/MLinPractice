# -*- coding: utf-8 -*-
"""
Visualisation of the most common hashtags in all tweets

Created on Thu Oct 21 15:23:47 2021

@author: jch
"""

import pandas as pd
import csv
import matplotlib.pyplot as plt
from scripts.feature_extraction.hashtags_most_common import HashtagsMostCommon

# load the data
df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

top_20 = HashtagsMostCommon(df)[1]

top_tags = pd.DataFrame(top_20)

# visualisation
x = top_tags[0]

fig,ax = plt.subplots(1,1)
ax.set_xlabel('top 20 tags')
ax.set_ylabel('occurences')
plt.xticks(rotation=90)
plt.plot(x, top_tags[1])