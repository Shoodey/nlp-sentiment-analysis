from helpers import *


class Tester:
    testing_set = []

    @staticmethod
    def get_accuracy(classifier):
        accuracy = nltk.classify.accuracy(classifier, Tester.testing_set)

        return str(round(accuracy * 100, 2))

    @staticmethod
    def test(classifier_dict):
        print("Testing", classifier_dict['name'], "classifier.")
        classifier = load_classifier("imdb", classifier_dict['slug'])
        print(classifier_dict['name'], "accuracy:", Tester.get_accuracy(classifier))

    @staticmethod
    def run():
        print("Loading features sets.")
        Tester.testing_set = load("features_sets")

        for classifier_dict in Store.classifiers:
            Tester.test(classifier_dict)
