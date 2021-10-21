# -*- coding: utf-8 -*-
"""
Visualisation of the most common hashtags in all tweets

Created on Thu Oct 21 15:23:47 2021

@author: jch
"""

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns

# load the data
df = pd.read_csv("data/preprocessing/preprocessed.csv", quoting = csv.QUOTE_NONNUMERIC, lineterminator = "\n")

# store data
tags_and_labels = df[["hashtags", "label"]]

# virals only
virals = df.loc[(tags_and_labels.label == True)]
non_virals = df.loc[(tags_and_labels.label == False)]

v_tags = virals["hashtags"]
non_v_tags = non_virals["hashtags"]

# count hashtags

# for viral tweets
v_counts = []

for v in v_tags:
    if len(v) > 2:
        tags = v.split("'")
        words = [t for t in tags if t.isalnum()]
        v_counts.append(len(words))
    else:
        v_counts.append(0)
        
non_v_counts = []

# for non viral tweets
for n in non_v_tags:
    if len(n) > 2:
        n_tags = n.split("'")
        n_words = [nt for nt in n_tags if nt.isalnum()]
        non_v_counts.append(len(n_words))
    else:
        non_v_counts.append(0)

# compute means 
means = [np.mean(v_counts), np.mean(non_v_counts)]

# plotting means
bars = ('viral tweets', 'non-viral tweets')
x_pos = np.arange(len(bars))
plt.bar(x_pos, means)
plt.xticks(x_pos, bars)
plt.show()

# plotting distribution
df_virals = pd.DataFrame(v_counts)
df_non_virals = pd.DataFrame(non_v_counts)

ax = sns.violinplot(y=df_virals, color="skyblue")
sns.violinplot(y=df_non_virals, color="orange")
sns.set(style="darkgrid")
ax.set_title("distribution of occurences")
ax.set_ylabel("number of tags")
plt.show()


