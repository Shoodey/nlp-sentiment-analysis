from helpers import to_timestamp


class Comment:

    def __init__(self, id, author, text, published):
        self.id = id
        self.author = author
        self.text = text.replace('\ufeff', '')
        self.published = to_timestamp(published)
        self.sentiments = []
