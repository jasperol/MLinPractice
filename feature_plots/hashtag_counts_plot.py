# -*- coding: utf-8 -*-
"""
Visualisation of the most common hashtags in all tweets

Created on Thu Oct 21 15:23:47 2021

@author: jch
"""

import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# load the data
with open("data/feature_extraction/training.pickle", "rb") as f_in:
    data = pickle.load(f_in)

# store data
tags_and_labels = data[["hashtags", "label"]]

# virals only
virals = data.loc[(tags_and_labels.label == True)]
non_virals = data.loc[(tags_and_labels.label == False)]

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

# plotting distribution
df_virals = pd.DataFrame(v_counts)
df_non_virals = pd.DataFrame(non_v_counts)

ax = sns.violinplot(y=df_virals, color="skyblue")
sns.violinplot(y=df_non_virals, color="orange")
sns.set(style="darkgrid")
ax.set_title("distribution of occurences")
ax.set_ylabel("number of tags")
plt.show()


