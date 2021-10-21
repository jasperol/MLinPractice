#!/bin/bash

# create directory if not yet existing
mkdir -p data/feature_extraction/

# run feature extraction on training set (may need to fit extractors)
echo "  training set"
<<<<<<< HEAD
python -m code.feature_extraction.extract_features data/preprocessing/split/training.csv data/feature_extraction/training.pickle -e data/feature_extraction/pipeline.pickle --char_length --sentiment
=======
python -m code.feature_extraction.extract_features data/preprocessing/split/training.csv data/feature_extraction/training.pickle -e data/feature_extraction/pipeline.pickle --char_length --weekday --hashtags_most_common --hashtags_num --words_most_common
>>>>>>> 9b6307233c0e0adf36c399c93b74cae9f13dc65f

# run feature extraction on validation set and test set (with pre-fit extractors)
echo "  validation set"
python -m code.feature_extraction.extract_features data/preprocessing/split/validation.csv data/feature_extraction/validation.pickle -i data/feature_extraction/pipeline.pickle
echo "  test set"
python -m code.feature_extraction.extract_features data/preprocessing/split/test.csv data/feature_extraction/test.pickle -i data/feature_extraction/pipeline.pickle
