import random

from Config import Config
from helpers import *


class Pickler:

    @staticmethod
    def run():
        # Save or load positive reviews
        if not is_pickled("positive_reviews"):
            print("Reading positive reviews.")
            positive_reviews = load_reviews('data/positive/', "positive", int(Config.testing_set_size / 2))
            print("Saving positive reviews.")
            save(positive_reviews, "positive_reviews")
        else:
            print("Loading positive reviews.")
            positive_reviews = load("positive_reviews")

        # Save or load negative reviews
        if not is_pickled("negative_reviews"):
            print("Reading negative reviews.")
            negative_reviews = load_reviews('data/negative/', "negative", int(Config.testing_set_size / 2))
            print("Saving negative reviews.")
            save(negative_reviews, "negative_reviews")
        else:
            print("Loading negative reviews.")
            negative_reviews = load("negative_reviews")

        # Save or load documents
        if not is_pickled("documents"):
            Store.documents = positive_reviews + negative_reviews
            print("Saving documents.")
            save(Store.documents, "documents")
        else:
            print("Loading documents.")
            Store.documents = load("documents")

        # Save or load word features
        if not is_pickled("word_features"):
            # Only pick the 5000 most frequent words according to the frequency distribution
            Store.word_features = list(nltk.FreqDist(Store.all_words).keys())[:5000]
            print("Saving word_features.")
            save(Store.word_features, "word_features")
        else:
            print("Loading word features.")
            Store.word_features = load("word_features")

        # Save or load features set
        if not is_pickled("features_sets"):
            features_sets = [(find_features(review, index), category) for index, (review, category) in
                             enumerate(Store.documents)]
            random.shuffle(features_sets)
            print("Saving features set.")
            save(features_sets, "features_sets")
            # Nothing to do after otherwise
