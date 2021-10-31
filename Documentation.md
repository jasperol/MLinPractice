# Documentation 

This project aims to predict if a tweet will become viral or not. In order to 
answer this question we have implemented some features that will extract information from the dataset.
The dataset consists of ~300 000 tweets containing the phrases "data science", "data analysis" or "data visualisation"
with 38 raw features including metadata like the id, date, place etc.
With these features we hope to train a classifier to determine if a tweet will be viral or not.



## Evaluation

### Design Decisions

Which evaluation metrics did we use and why? 

We used the included accuracy and Cohen's kappa metrics, accuracy because it is one of the most
common evaluation metrics and incredibly simple. However due to our unbalanced data, it didn't 
actually say very much. Therefore we looked towards Cohen's kappa, which accesses the agreement
between raters, and therefore takes into account an imbalance in class distribution. This gave us
a more useful judgement of our classifer.

And finally we added the F1 score, which is also good for imbalanced data. This gave us a value that 
is a combination of precision (how many positive classified tweets are actaully positive) 
and recall (how many true positives were caught). As such it gave us an indictation of both False Negatives and
False Positives - both of which we would want to avoid in viral-tweet classification algorithm.

Which baselines did we use and why?
By comparing ourselves to these very uninformative classifiers we make sure to view
any correct classifications in context.

- Majority Vote classifier: We used this because we had a majority negative class (about 95% non-viral) and 
this Dummy classifier always predicts the most frequent label in the training set. So the accuracy score 
was rather high (0.908). This means it was easy to see if our classifier had made any improvements 
because it would need to be above 90%.
However the majority vote classifer only computes '0' for the Cohen's kappa and F1 scores. 
So didn't set much of a standard to compare our classifiers towards. 
Therefore we also made use of the Label Frequency classifier.

- Label Frequency classifier: this classifier generates predictions by respecting the training set's
class distribution. So here we saw that the Cohen's kappa and F1 scores were 0.004 and 0.095 respectively for the 
training set and less for the validation set - which at least gave us a figure to work with. 
Also the accuracy was 0.83 for both training and validation, something else to use as a reference
later on with our 'real' classifiers.


The results and interpretation thereof are discussed below, within the context of the classification section



## Preprocessing

### Design Decisions

Which kind of preprocessing steps did we implement? Why were they necessary
and/or useful down the road?

- create_labels: this was crucial to implement to give the tweet a 'viral' or 'not viral' label 
  (based on our threshold of number of retweets and likes). This was used pretty much in every 
  stage of the pipeline. We also created a 'viral count' that gave a continuous score of how viral a tweet was,  
  rather than only a discrete boolean class. This was used in the plotting functions. 
- punctuation_remover: removes the punctuation to allow easier processing later where punctuation would just get in the way.
- split_data: was vital to divide up the data into training, test and validation groups. 
  This way one could check for under and overfitting if the training data has vastly different 
  evaluation metric scores between 'unseen' data in the test data or completely 'virgin' data in the validation set
- tokenizer: which tokenized the tweets into individual words, this was used in feature extraction further
  down the pipeline.


### Results

Here is a short example of our preprocessing:

For example a sentence like 'Machine Learning is the best! I love it so much' would be preprocessed as follows: 

1. create labels: 
    If the likes + retweets > 50 then it is labelled 'true' for being viral. Otherwise it is labelled 'false'. 
    This is saved in a novel column in the dataframe in util.py as 'COLUMN_LABEL'.
    e.g. let's say our example sentence is viral. It gets the label = TRUE. This is also stored in data/preprocessing/labeled.csv
    which gets passed to the next stage:
2. In general preprocessing:
    The punctuation_remover any punctuation points are replaced with an empty space " ". This is stored in "COLUMN_PUNCTUATION". 
    e.g. "Machine Learning is the best I love it so much"
    Then in tokenize, the tweet is broken down into the individual words:
    So our sentence becomes e.g. "Machine" "Learning" "is" "the" and so forth. If used, the input gets stored with the suffix
    '_tokenised'
3. In split_data:
    As a final step, the data gets seperated into training, test and vailidation sets. 



## Feature Extraction

### Design Decisions

Which features did you implement? What's their motivation and how are they computed?
We created 9 features in total: 
- sentiment.py
        Our group hypothesized that more emotionally saturated tweets would become
        more viral, as people respond more to sentiment extremes. For example in clickbait thumbnails or 
        sensational articles headlines. Inspiration: https://www.wired.com/2015/12/psychology-of-clickbait/
        Using the nltk package vader sentiment intensity analyser, this feature 
        outputs a set of metrics - positive, negative, neutral and compound. 
        I selected for compound only which is a normalisation between -1 (most extreme positive) 
        and +1 (most extreme positive).
- day_of_the_week
        Here we hoped to see a correlation between the day of the week and viralnes. Namely, more viral tweets 
        are over the weekend when people aren't working and might be present on the app.
        This feature is extracted from the date column and assigns numerical values for each day of the week. 
- hastags_num
        Again, we hoped to see a correlation between number of hashtags and viralness. Research has shown
        that for example in Instagram posts, contrary to belief, less hashtags is correlated to more popular posts. 
        (https://mention.com/en/reports/instagram/hashtags/#3).  Since hashtags are so popular,
        a post will most likely be obscured by the competition. So here the overall number of hashtags is computed 
        in order to check if an indirectly proportional relationship exists. 
- hastags_most_common
        As an follow-on of the previous feature, we were curious if certain hastags were more present in viral tweets. 
        Are there certain topics that are particularly 'hot' in data science related tweets?
    	This feature first extracts the most common hashtags over the whole dataset and then checks for each tweet how many
        of the top 50 hashtags were used.
- tweet_frequency
        This feature returns the amount of times that a certain user has posted a tweet, it is implemented by using a 
        predefined function from the nltk package. The motivation was to analyse if more regular tweeters
        have a better chance at posting viral tweets, rather than someone with very few tweets that might
        not have the same following.
- words_most_common
        We wanted to see if viral tweets had an average lexicon that differed from non-viral 
        tweets, and if so - what these were. This features first extracts the most common words over the whole dataset and 
    	then checks for each tweet how many of the top 50 words were used.
- replies_num.py
        This feature takes the tweet replies count column of the dataframe as a marker of interest. 
        We predicted that a higher number of replies will correlate to a chance of viralness.
- mention_num.py
        Upon reading some literature on tweet viralness, we saw that the number of mentions in a tweet 
        (a reference to another twitter account) could have a relationship to viralness. So like in hastags.num the 
        number of mentions were computed as a predictor. 
        (Inspiration: https://www.researchgate.net/publication/262166912_Analyzing_and_predicting_viral_tweets)
- names_places.py  
        This aims to count the number of NNPs (Proper Nouns) in each tweet, it implemented using the NER 
        functions which are supplied in the nltk package. We were curious to see if tweets with more
        words that refer to actual people or reference a place (that maybe you relate to) would connect with 
        the audience more and therefore become more viral.
        This feature was incredibly processing heavy - so we opted to leave it out.
- char_length.py
        was already implemented (a score of the length of the tweet) and was a simple, although quite useful 
        feature and so was kept in our project.

### Results

Please see corresponding files 'feature_plots' and 'plot_images' to view the code and .png files respectively, 
that visualise how the features divided the viral/non-viral tweets and their spread.


### Interpretation

We guessed that the number of tweet replies, tweet frequency, and the hashtags count may be more useful than others. 
This was partly confirmed below.



## Dimensionality Reduction

### Design Decisions

Which dimensionality reduction technique(s) did we pick and why?

Due to not having all that many features, dimensionality reduction techniques like PCA seemed unnecessary. 
However we found using the mutual information method was noteworthy to analyse which features were most useful. 

### Results

Which features were selected / created? Do we have any scores to report?

The three most useful features were as expected, replies_num with a mutual information score of 0.064, 
tweet frequency of 0.037 and unexpectantly char_length with a score of 0.012.
We decided to implement all of our features (except names_places), as they were not terribly computationally heavy and 
did improve the metrics slightly, so we decided there was no harm in keeping them despite their relatively
low mutual information.

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

Which classifier(s) did we use? Which hyperparameter(s) (with their respective
candidate values) did we look at? What were our reasons for this?

- We continued using the already implemented K-nearest neighbour classifier. After analysing the 
hyperparamters from K = 1:10, we found that a K neighbours of as low as 2 produced reasonable results 
in the training data, but K = 5 had the best Cohen's kappa and F1 scores and so set that as our candidate value.
- We also implemented a random forest classifier with a specified number of trees set to 50 as
this was found to produce evaluation metric scores that leveled out and did not improve the 
classification by enough to necessate the computation required.
- We also implemented the Naive Bayes classifier, but found this had worse metrics than the KNN and 
random forest classifiers, so we opted to use the others instead.

### Results

The big finale begins: What are the evaluation results we obtained with our
classifiers in the different setups? Do they overfit or underfit?

The very best scores we obtained for the training data were from the random forest classifier (50 trees):
accuracy: 0.9544020373437905
cohen_kappa: 0.6699552036549987
f1_score: 0.6931098555231126

Below a print out where you can see the improvement/worsening of the metrics as the hyperparameters were adjusted:

scripts/classification.sh
  training set
    2 nearest neighbor classifier
    accuracy: 0.9332172678408438
    cohen_kappa: 0.44166829225114657
    f1_score: 0.4694032857334706
    
    5 nearest neighbor classifier
    accuracy: 0.9302367510676899
    cohen_kappa: 0.46881711827834527
    f1_score: 0.5024911603985857
    
    7 nearest neighbor classifier
    accuracy: 0.9288056522767993
    cohen_kappa: 0.4444170698348935
    f1_score: 0.47772174919401506
    
    10 nearest neighbor classifier
    accuracy: 0.9276337288574874
    cohen_kappa: 0.39445197680675737
    f1_score: 0.42444882595447214
    
    30 random forest classifier
    accuracy: 0.9540020057920061
    cohen_kappa: 0.6676240672543705
    f1_score: 0.691015063204905
    
    50 random forest classifier
    accuracy: 0.9544471113214563
    cohen_kappa: 0.6704789276896022
    f1_score: 0.6936223426427679
    
    100 random forest classifier
    accuracy: 0.954683749704202
    cohen_kappa: 0.6714254435739221
    f1_score: 0.6944032827994984
    
    guassian naive bayes classifier
    accuracy: 0.9219938474020486
    cohen_kappa: 0.3078018159984025
    f1_score: 0.3354931605471562 
  
Unfortunately the random forest seems to be overfitting, as the metrics are somewhat worse in 
the validation set
  validation set
    accuracy: 0.9223826104594165
    cohen_kappa: 0.30896697118777483
    f1_score: 0.3362243422954611

For the best selected setup: How well does it generalize to the test set?


### Interpretation

Is there anything we learned from these results?

We are excited to report that our training and validation results are an improvement on our baselines
 
They are unfortuately not substantial results, with only moderate agreement for Cohen's kappa for example on our 
training set, and fair results on the validation set. However, with more time and metadata 
(like number of followers we anticipate would have been INCREDIBLY telling), we are convinced that 
we could improve on this score and could easily be used in practice. At this point in time probably not. 

Which hyperparameter settings are important for the results?

- the number of trees in the random forest classifier and the number of neighbours for the KNN
classifier had highly variable results when altered. This is good to know for the future. 


Anything else we may have learned?

We have learned many skills: foremost being machine learning in practice requires
far more than only coding skills, making a project with so many subfiles and steps 
in the pipeline also requires organised version control and diciplined 
branching, coding and merging. As a group we struggled a lot with the set up, some 
members opting for working on windows, some on the VM and we constantly had to 
troubleshoot along the way. All these lessons mean we leave this seminar maybe not
with the best code and the strongest results but we feel a lot more confident 
using Git and Trello to co-ordinate our efforts. But also 
respecting that set-up, trouble-shooting, daily scrum meetings, and figuring out another
persons codebase probably will take up 90% of your time and only a fraction of the 10% 
coding gets spent on implementing super cool, trendy and impressive machine learning algorithms.
So summarised in one sentence: What's the purpose of having the most sophisticated ML classifier
if you can't even get the code to run? In theory it sounds great, in practise - you got to
keep your workspace tidy. 
