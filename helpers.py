import datetime
import os
import pickle
import nltk
import time

from Config import Config
from Store import Store

project_path = os.path.abspath(os.path.dirname(__file__))


def save(data, filename, corpus=None):
    if corpus:
        path = corpus + "/training/pickle/"
        path = os.path.join(project_path, path)

    else:
        path = "pickle/"

    file = open(path + filename + ".pickle", "wb")
    pickle.dump(data, file)
    file.close()


def load(filename, corpus=None):
    if corpus:
        path = corpus + "/training/pickle/"
        path = os.path.join(project_path, path)

    else:
        path = "pickle/"

    file = open(path + filename + ".pickle", "rb")
    data = pickle.load(file)
    file.close()
    return data


def load_classifier(base, filename):
    file_path = os.path.join(project_path, base + "/training/pickle/" + filename + ".pickle")
    file = open(file_path, "rb")
    data = pickle.load(file)
    file.close()
    return data


def is_pickled(filename):
    return os.path.isfile("pickle/" + filename + ".pickle") and os.path.getsize("pickle/" + filename + ".pickle") > 0


def find_features(text, text_number=-1):
    if text_number != -1:
        print("Extracting features for document " + str(text_number + 1) + "/" + str(len(Store.documents)))

    words = nltk.word_tokenize(text)
    features = {}

    if not len(Store.word_features):
        Store.word_features = load("word_features", Config.corpus)

    for word in Store.word_features:
        features[word] = (word in words)

    return features


def load_reviews(directory, category, size):
    """
    Loads data from files in given directory and stores it onto documents data set.
    :param directory: Directory containing the training data
    :param category: The category of the data (positive/negative)
    :param size: Size of the set to read (either for training or testing=
    """
    # reviews_limit is half of the set value since it deals with both positive & negative reviews
    reviews_limit = size
    reviews = []

    for filename in os.listdir(directory):
        # Skip non txt files (such as .gitignore)
        if ".txt" not in filename:
            continue

        # Only load files within set limit
        if reviews_limit == 0:
            break

        print("Reading", category, "file", filename,
              str(size - reviews_limit + 1) + "/" + str(size))

        # Open given file and store its content
        file = open(directory + filename, "r", encoding="utf8")
        review = file.read()
        # Append the review to the reviews list set as tuple (line, positive/negative)
        reviews.append((review, category))
        # Tokenize file's words
        words = nltk.word_tokenize(review)
        # Map each word to its part of speech tag
        pos = nltk.pos_tag(words)
        # Go through each (word, pos) element
        for word in pos:
            # Only accept POS tags starting with a letter in allowed_pos_tags
            # Example: JJ, JJR, JJS are all adjectives (starting with J)
            if word[1][0] in Store.allowed_pos_tags:
                # Append allowed words to the all_words set
                Store.all_words.append(word[0].lower())
        file.close()
        reviews_limit -= 1

    return reviews


def get_videos_path(directory):
    return os.path.join(project_path, "sentube/data/" + directory)


def to_timestamp(iso_datetime):
    return int(time.mktime(datetime.datetime.strptime(iso_datetime, "%Y-%m-%dT%H:%M:%S.%fZ").timetuple()))
