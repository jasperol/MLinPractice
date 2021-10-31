# -*- coding: utf-8 -*-
"""
Scatter visualisation of 

Created on Sun Oct 31 16:16:18 2021

@author: jch
"""

import csv
import pandas as pd
from matplotlib import pyplot as plt

# load data
data = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

# separate viral and non viral tweets into 2 different dataframes
virals = data.loc[(data.label == True)]
non_virals = data.loc[(data.label == False)]

# set the viralness score
virals['viral_count'] = (virals['likes_count'] + virals['retweets_count'])
non_virals['viral_count'] = (non_virals['likes_count'] + non_virals['retweets_count'])

# select columns
viral_flt = virals[["viral_count","replies_count"]]
non_viral_flt = non_virals[["viral_count","replies_count"]]

# scatter plot of data points
plt.scatter(viral_flt["replies_count"], viral_flt["viral_count"], color='hotpink', label='viral tweets [27.160]',
               alpha=0.3, edgecolors='none')
plt.scatter(non_viral_flt["replies_count"], non_viral_flt["viral_count"], color='darkblue', label='non viral tweets [268.651]',
               alpha=0.3, edgecolors='none')
plt.gcf().set_size_inches((20, 10))
plt.xlim(0, 400)
plt.ylim(0, 2000)
plt.xlabel("replies_count", fontsize=16)
plt.ylabel("viralness", fontsize=16)
plt.figtext(0.05, 0.15, 'threshold = 50', horizontalalignment='left', fontsize=13, color='darkblue') 
plt.legend(loc='upper left', prop={'size': 18})
plt.show
