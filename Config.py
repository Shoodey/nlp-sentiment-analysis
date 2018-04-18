class Config:
    # Number of reviews to test upon, 25.000 being the limit
    # this value will be divided between positive and negative data
    # i.e. training_set_size = 8000 means 4000 positive reviews and 4000 negative ones
    training_set_size = 25000

    # the same applies of the testing_set_size
    testing_set_size = 3000

    # Select which data set to base analysis upon
    # Current ones: twitter, imdb & nltk reviews.
    # You can remove data sets but keep the structure as an array
    corpora = ["twitter", "imdb"]

    # Defaulted to empty as variable should be declared but filled
    # later on with adequate values
    corpus = ""

    # Selected classifiers
    classifiers = []

    # Selected action
    action = ""
