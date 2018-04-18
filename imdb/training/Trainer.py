from helpers import *


class Trainer:
    training_set = []

    @staticmethod
    def train(name, classifier_class):
        print("Training", name.replace('_', ' ').title(), "classifier.")
        classifier = classifier_class.train(Trainer.training_set)
        save(classifier, name)

    @staticmethod
    def run():
        print("Loading features sets.")
        Trainer.training_set = load("features_sets")

        for classifier in Store.classifiers:
            classifier_class = classifier.get('class')
            if not is_pickled(classifier.get('slug')):
                Trainer.train(classifier.get('slug'), classifier_class)
            else:
                print(classifier.get('name'), "has already been trained.")
