#!/bin/bash

# create directory if not yet existing
mkdir -p data/classification/

# run feature extraction on training set (may need to fit extractors)
echo "  training set"
<<<<<<< HEAD
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 1 -s 42 --f1_score --accuracy --kappa
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 2 -s 42 --f1_score --accuracy --kappa
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 3 -s 42 --f1_score --accuracy --kappa
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 4 -s 42 --f1_score --accuracy --kappa
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 5 -s 42 --f1_score --accuracy --kappa
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 6 -s 42 --f1_score --accuracy --kappa
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 7 -s 42 --f1_score --accuracy --kappa
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 8 -s 42 --f1_score --accuracy --kappa
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --knn 9 -s 42 --f1_score --accuracy --kappa
=======
python -m scripts.classification.run_classifier data/dimensionality_reduction/training.pickle -e data/classification/classifier.pickle --random_forest 50 -s 42 --f1_score --accuracy --kappa
>>>>>>> 5d961665d1d18c0e5ce0986fa209e7f9a4c22da9

# run feature extraction on validation set (with pre-fit extractors)
echo "  validation set"
python -m scripts.classification.run_classifier data/dimensionality_reduction/validation.pickle -i data/classification/classifier.pickle --f1_score --accuracy --kappa

# don't touch the test set, yet, because that would ruin the final generalization experiment!
