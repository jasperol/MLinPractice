# Documentation Example

Some introductory sentence(s). Data set and task are relatively fixed, so 
probably you don't have much to say about them (unless you modifed them).
If you haven't changed the application much, there's also not much to say about
that.
The following structure thus only covers preprocessing, feature extraction,
dimensionality reduction, classification, and evaluation.

## Evaluation

### Design Decisions

Which evaluation metrics did you use and why? 
We used the included accuracy and cohens kappa metrics, otherwise we also used an f1_score metric 
to get a combination of precision (how many positive classified tweets are actaully positive)
and recall (how many true positives were caught).

Which baselines did you use and why?
-Always true
-Always false



### Results

How do the baselines perform with respect to the evaluation metrics?
The baseline of 'always false' provides a promising result as 90% of the tweets are classified as non-viral.
Therefore the accuracy is 90% (what percentage did I get right?), however the precision, recall and 
f1 score will all be 0 or NaN. 
'Always true' provides the opposite of course with 10% accuracy and precision, a perfect recall
(all the true positives were caught) however only a 18% f1 score. 

Cohens Kappa provides a universal 0 score because it adjusts the acuurcy by the probability of random
agreement - and so as such provides probably the most 'reliable' evaluation of our classifier. 



### Interpretation

Is there anything we can learn from these results?

## Preprocessing

I'm following the "Design Decisions - Results - Interpretation" structure here,
but you can also just use one subheading per preprocessing step to organize
things (depending on what you do, that may be better structured).

### Design Decisions

Which kind of preprocessing steps did you implement? Why are they necessary
and/or useful down the road?

- create_labels: this was crucial to implement as to label a tweet as viral or not based on our rewteet
and like numbers. This was used pretty much in every stage of the pipeline
- punctuation_remover
- split_data: vital as an evaluation scheme as a way to divide up the data into traning, test and 
validation groups. This way one can check for under and overfitting if the training data has far different 
evaluation metric scores to 'unseen' data in the test data or completely 'virgin' data in the validation
set
- tokenizer: this was used in the names_places feature extraction and others



### Results

Maybe show a short example what your preprocessing does.

For example a sentence like 'Machine Learning is the best! I love it so much' would be preprocessed as follows: 
1. create labels: if the likes + rewteets > 50 then it is labelled 'true' for being viral. Otherwise not it does not reach
the threshold to be in the positive class and is labelled 'false'. This is saved in a new column in code.util as 'COLUMN_LABEL'.
e.g. let's say our example sentence is viral. It gets the label = TRUE.
2. In general preprocessing, punctuation_remover and tokenizer files are implemented such that any punctuation points are 
replaced with an empty space " ". This is resaved at "COLUMN_TWEET". 


Then in tokenize, the tweet is borken down into the individual words:
So our sentence becomes 

### Interpretation

Probably, no real interpretation possible, so feel free to leave this section out.

## Feature Extraction

Again, either structure among decision-result-interpretation or based on feature,
up to you.

### Design Decisions

Which features did you implement? What's their motivation and how are they computed?

### Results

Can you say something about how the feature values are distributed? Maybe show some plots?

### Interpretation

Can we already guess which features may be more useful than others?

## Dimensionality Reduction

If you didn't use any because you have only few features, just state that here.
In that case, you can nevertheless apply some dimensionality reduction in order
to analyze how helpful the individual features are during classification

### Design Decisions

Which dimensionality reduction technique(s) did you pick and why?

### Results

Which features were selected / created? Do you have any scores to report?

### Interpretation

Can we somehow make sense of the dimensionality reduction results?
Which features are the most important ones and why may that be the case?

## Classification

### Design Decisions

Which classifier(s) did you use? Which hyperparameter(s) (with their respective
candidate values) did you look at? What were your reasons for this?

### Results

The big finale begins: What are the evaluation results you obtained with your
classifiers in the different setups? Do you overfit or underfit? For the best
selected setup: How well does it generalize to the test set?

### Interpretation

Which hyperparameter settings are how important for the results?
How good are we? Can this be used in practice or are we still too bad?
Anything else we may have learned?