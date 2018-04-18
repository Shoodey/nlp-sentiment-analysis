import nltk
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import LinearSVC


class Store:
    videos = []

    all_words = []

    #  J: Adjective, R: Adverb, V: Verb, ...
    allowed_pos_tags = ["J", "R"]

    documents = []

    word_features = []

    classifiers = [
        {
            'slug': 'naive_bayes',
            'name': 'Naive Bayes',
            'class': nltk.NaiveBayesClassifier
        },
        {
            'slug': 'multinomial_naive_bayes',
            'name': 'Multinomial Naive Bayes',
            'class': nltk.SklearnClassifier(MultinomialNB())
        },
        {
            'slug': 'bernoulli_naive_bayes',
            'name': 'Bernoulli Naive Bayes',
            'class': nltk.SklearnClassifier(BernoulliNB())
        },
        {
            'slug': 'logistic_regression',
            'name': 'Logistic Regression',
            'class': nltk.SklearnClassifier(LogisticRegression())
        },
        {
            'slug': 'linear_support_vector',
            'name': 'Linear Support Vector',
            'class': nltk.SklearnClassifier(LinearSVC())
        }
    ]
