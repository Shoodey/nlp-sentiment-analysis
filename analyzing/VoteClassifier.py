from nltk import ClassifierI
from statistics import mode
from collections import Counter


class VoteClassifier(ClassifierI):

    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for classifier in self._classifiers:
            vote = classifier.classify(features)
            votes.append(vote)

        grouped_votes = [[k, ] * v for k, v in Counter(votes).most_common()]
        sentiments = []
        for vote in grouped_votes:
            sentiments.append({
                'sentiment': vote[0],
                'confidence': len(vote) / len(votes)
            })

        return sentiments

    def labels(self):
        pass
