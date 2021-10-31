# Documentation 

This project aims to predict if a tweet will become viral or not. In order to 
answer this question we have implemented some features that will extract some information from the dataset.
With these features we hope to train a classifier to determine if a tweet will be viral or not.


## Evaluation

### Design Decisions

We used the included accuracy and cohens kappa metrics, otherwise we also used an f1_score metric 
to get a combination of precision (how many positive classified tweets are actaully positive)
and recall (how many true positives were caught).

We used the following baselines:
-majority vote classifier
-label frequency classifier
By comparing ourselves to these very uninformative classifiers we make sure to view
any correct classifications in context.
Which evaluation metrics did you use and why? 

We used the included accuracy and Cohen's kappa metrics, accuracy simply because it is one of the most
common evaluation metrics and incredibly simple, however due to our unbalanced classes doesn't 
actually say very much. Therefore we looked towards Cohen's kappa, which access the agreement
between raters, and therefore takes into account an imbalance in cass distribution, to give
us a more useful judgement of our classifer. And finally we used the F1 score, also good for imbalanced data,
to get a value that is a combination of precision (how many positive classified tweets are actaully positive) 
and recall (how many true positives were caught), which gives us an indictation of both False Negatives and
False Positives - both of which we would want to avoid in viral-tweet classification.

Which baselines did you use and why?
-majority vote classifier: as this Dummy classifier always predicts the most frequent label
in the training set, we used this because we had a majority negative class (about 90% 
of the dataset were non-viral tweets) meaning the accuracy score was rather high (0.908) 
even just for a baseline, which would make analysing our classifier quite easy -
as it would need to have an accuracy above 90% to have made any improvements. 
However the cohens kappa and f1 scores were both 0 so it didn't help much with being used
to compare our other classifiers. There we also made use of the:
-label frequency classifier: this classifier generates predictions by respecting the training set's
class distribution, so here we saw that the cohens kappa and f1 scores were 0.004 and 0.095 for the 
training set and less for the validation set - which at least gave us a figure to work with. 
Also the accuracy was 0.83 for both training and validation, something else to use as a reference
later on with our 'real' classifiers.



### Results
- accuracy results: 
- Cohen's kappa results:
- F1 score results:

As mentioned above, the baseline of 'always false' provides a promising result as 90% of the tweets are classified as non-viral.
Therefore the accuracy is 90%, however the F1 score will all be 0 or NaN. 
'Always true' provides the opposite of course with 10% accuracy and precision, a perfect recall
(all the true positives were caught) however only a 18% f1 score. 

Cohens Kappa provides a universal 0 score because it adjusts the acuracy by the probability of random
Cohen's kappa provides a universal 0 score because it adjusts the acuurcy by the probability of random
agreement - and so as such provides probably the most 'reliable' evaluation of our classifier. 


### Interpretation

Is there anything we can learn from these results?

## Preprocessing


### Design Decisions

- create_labels: this was crucial to implement as to label a tweet as viral or not based on our rewteet
and like numbers. This was used pretty much in every stage of the pipeline
- punctuation_remover: removes the punctuation
Which kind of preprocessing steps did you implement? Why are they necessary
and/or useful down the road?

- create_labels: this was crucial to implement to give the tweet a label which divided it into being
 viral or not (based on our threshold of number of retweets and likes). This was used pretty much in every 
 stage of the pipeline.
- punctuation_remover: removes the punctuation to allow easier processing later e.g. for nltk feature extraction 
where punctuation would just get in the way.
>>>>>>> 5d961665d1d18c0e5ce0986fa209e7f9a4c22da9
- split_data: vital as an evaluation scheme as a way to divide up the data into traning, test and 
validation groups. This way one can check for under and overfitting if the training data has far different 
evaluation metric scores to 'unseen' data in the test data or completely 'virgin' data in the validation
set
- tokenizer: which tokenizes the tweets into individual words, this can be used in feature extraction further
down the pipeline.


### Results

A short example of your preprocessing:

For example a sentence like 'Machine Learning is the best! I love it so much' would be preprocessed as follows: 
1. create labels: if the likes + rewteets > 50 then it is labelled 'true' for being viral. Otherwise not it does not reach
the threshold to be in the positive class and is labelled 'false'. This is saved in a new column in code.util as 'COLUMN_LABEL'.
e.g. let's say our example sentence is viral. It gets the label = TRUE. This is also saved in data/preprocessing/labeled.csv
which gets passed to the next stage:
2. In general preprocessing, the punctuation_remover and tokenizer files are implemented such that any punctuation points are 
replaced with an empty space " ". This is resaved in "COLUMN_TWEET". 
e.g. "Machine Learning is the best I love it so much"
Then in tokenize, the tweet is broken down into the individual words:
So our sentence becomes e.g. "Machine" "Learning" "is" "the" and so forth. 
3. In split_data as a final step, the data gets seperated into training, test and vailidation sets. 


## Feature Extraction

Again, either structure among decision-result-interpretation or based on feature,
up to you.

### Design Decisions

Which features did you implement? What's their motivation and how are they computed?
We implemented 8 features in total: 
- sentiment.py
        As motivation, our group hypothesized that more emotionally saturated tweets would become
        more viral, as people respond more to sentiment extremes e.g. in clickbait thumbnails or 
        sensational articles headlines. Using the nltk package vader sentiment intensity analyser, this feature takes a 
        tweet as input and outputs a set of metrics - positive, negative, neutral and compound. 
        I selected for compound only which is a normalisation between -1 (most extreme positive) 
        and +1 (most extreme positive).
- names_places.py  **This is incredibly processing heavy - runtime warning*
        This aims to count the number of NNPs (Proper Nouns) in each tweet, it implemented using the NER 
        functions which are supplied in the nltk package. We were curious to see if tweets with more
        words that refer to actual people or reference a place (that maybe you relate to) would connect with 
        the audience more and therefore become more viral.
- day_of_the_week
        Here we hoped to see a correlation between the day of the week and viralness - such as more viral tweets 
        seen over the weekend as people have more time away from work where they might be present on
        the app. This feature is extracted from the date column and assigns numerical values for each day of the week. 
- hastags_num
        Again, we hoped to see a correlation between number of hashtags and viralness, as research has shown
        that for example in Instagram posts, making your post easily searchable through widely used hashtags, 
        makes your post more discoverable and hopefully therefore more viral.  And as such, here the overall number of hashtags is 
    	computed in order to check whether for example a high number of hashtags makes a tweet more likely to go viral or not.
- hastags_most_common
        As an extrapolation of the previous feature, we were then curious to check if certain hastags were lent themselves
        to being present in viral tweets. Are there certain topics that are particularly 'hot' in data science related tweets. 
	This features first extracts the most common hashtags over the whole dataset and then checks for each tweet how many
        of the top 50 hashtags were used.
- tweet_frequency
        This feature returns the amount of times that a certain user has posted a tweet, it is implemented by using a 
        predefined function from the nltk package. The motivation was to analyse if more regular tweeters
        have a better chance at posting viral tweets, rather than someone with very few tweets that might
        not have the same following.
- words_most_common
        And finally, we wanted to see if viral tweets had an average lexicon that differed from non-viral 
        tweets, and if so - what these were. This features first extracts the most common words over the whole dataset and 
    	then checks for each tweet how many of the top 50 words were used.
    	
        

- char_length was implemented (a score of the length of the tweet) and bigrams was found to be not strictly necessary for our code. 

### Results

Feature value distributions can be found in the plot_images and feature_plots folder.

Please see corresponding files 'feature plots' and 'plot images' to view the code and .png files respectively. 

The features with the most significant division between viral and non-viral, is the day of the week that 
the tweet was posted. From the plot one can see that posting on weekends makes a tweet much more likely to be viral.

### Interpretation

Can we already guess which features may be more useful than others?
- The number of tweet replies and tweet frequency, day of the week were hypothesized by our group to be most useful.

## Dimensionality Reduction

If you didn't use any because you have only few features, just state that here.
In that case, you can nevertheless apply some dimensionality reduction in order
to analyze how helpful the individual features are during classification

### Design Decisions

Which dimensionality reduction technique(s) did you pick and why?

Due to not having all that many features  - dimensionality reduction techniques in the form
of something like PCA seemed unnecessary. However we found using the mutual information method was useful to 
analyse which features were most useful. As expected, the number of tweet replies and tweet frequency both
had a relatively high statistical dependence to the target variable. 

Also to be noted, in the classification section, we also implemented a random forest classifer
which in its own terms in a method of dimensionality reduction in unto itself. 

### Results

Which features were selected / created? Do you have any scores to report?
Replies_num had a mutual information score of 0.064, tweet frequency of 0.037 and char_length 
was also relatively useful.

### Interpretation

Can we somehow make sense of the dimensionality reduction results?
Which features are the most important ones and why may that be the case?

It would make sense that the number of replies on a tweet indicates how viral a tweet is, by virtue of it
showing user-activity. The higher the number of people are that see your tweet and take the time 
to write a comment, the more likely it is (we hypothesised) that you would have a high number of likes
and retweets. Similarly, we expected that the number of tweets you has posted, the more of a following 
you would have, in comparison to someone who maybe tweeted only randomly rarely. 

## Classification

### Design Decisions

Which classifier(s) did you use? Which hyperparameter(s) (with their respective
candidate values) did you look at? What were your reasons for this?

- We continued using the already implemented K-nearest neighbour classifier, (and as mentioned 
above, the baseline metrics: majority classifier and label frequency classifier). After analysing the 
evaluation metrics from k = 1:10, we found that a k of as low as 2 produced the best results and so set
that as our candidate value.
- As well as we implemented a random forest classifier with a specified number of trees set to 50 as
this was found to produce results evaluation metric scores that leveled out and did not improve the 
classification by enough to necessate the computation required.
- We also implemented the Naive Bayes classifier, but found this had worse metrics than the KNN and 
random forest classifiers, so we opted to use the others instead.


### Results

The big finale begins: What are the evaluation results you obtained with your
classifiers in the different setups? Do you overfit or underfit? For the best
selected setup: How well does it generalize to the test set?

- We are most disappointed to acknowledge that our evaluation metrics showed a less
than stellar classification. The very best scores we managed were around an accuracy of 
0.922 and Cohen_kappa of 0.339 and an f1_score of 0.370 for the validation set and much
the same for the test results. 


### Interpretation

Which hyperparameter settings are how important for the results?
How good are we? Can this be used in practice or are we still too bad?
Anything else we may have learned?

We have learned many skills: foremost being machine learning in practice requires
far more than only coding skills, making a project with so many subfiles and steps 
in the pipeline also requires incredinbly organised version control and diciplined 
branching, coding and merging. As a group we struggled a lot with the set up, some 
members opting for working on windows, some on the VM and we constantly had to 
troubleshoot along the way. All these lessons mean we leave this seminar maybe not
with the best code and the strongest results but we feel a lot more confident 
(or maybe respectful) using Git and Trello to co-ordinate our efforts. But also 
respecting that set-up, trouble-shooting, daily scrum meetings, and figuring out
some-one elses code probably will take up 90% of your time and only a fraction of the 10% 
coding gets spent on implementing super cool, trendy and impressive machine learning algorithms.
So summarised in one sentence: What's the purpose of having the most sophisticated ML classifier
if you can't even get the code to run? In theory it sounds great, in practise - you got to
keep your workspace tidy. 
