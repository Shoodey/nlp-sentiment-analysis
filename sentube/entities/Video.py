from helpers import to_timestamp


class Video:

    def __init__(self, id, type, category, uploader, title, view_count, description, duration, published):
        self.id = id
        self.type = type
        self.category = category
        self.uploader = uploader
        self.title = title
        self.view_count = view_count
        self.description = description
        self.duration = duration
        self.comments = []
        self.published = to_timestamp(published)

    def set_comments(self, comments):
        self.comments = comments
