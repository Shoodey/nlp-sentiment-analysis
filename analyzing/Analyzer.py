from analyzing.VoteClassifier import VoteClassifier

from helpers import *


class Analyzer:
    vote_classifier = None

    @staticmethod
    def set_variables(corpus):
        naive_bayes = load_classifier(corpus, "naive_bayes")
        multinomial_naive_bayes = load_classifier(corpus, "multinomial_naive_bayes")
        bernoulli_naive_bayes = load_classifier(corpus, "bernoulli_naive_bayes")
        logistic_regression = load_classifier(corpus, "logistic_regression")
        linear_support_vector = load_classifier(corpus, "linear_support_vector")

        Analyzer.vote_classifier = VoteClassifier(
            naive_bayes,
            multinomial_naive_bayes,
            bernoulli_naive_bayes,
            logistic_regression,
            linear_support_vector,
        )

    @staticmethod
    def get_sentiment(text):
        features = find_features(text)
        return Analyzer.vote_classifier.classify(features)

    @staticmethod
    def run(corpus):
        Analyzer.set_variables(corpus)
        videos = Store.videos
        for video_index, video in enumerate(videos):
            print()
            for comment_index, comment in enumerate(video.comments):
                print("Video", str(video_index + 1) + "/" + str(len(videos)) + " - Comment",
                      str(comment_index + 1) + "/" + str(len(video.comments)))
                comment.sentiments = Analyzer.get_sentiment(comment.text)
        Store.videos = videos
