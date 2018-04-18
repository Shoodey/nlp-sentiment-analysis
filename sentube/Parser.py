import json
import os

from Store import Store
from helpers import get_videos_path
from sentube.entities.Comment import Comment
from sentube.entities.Video import Video


class Parser:

    @staticmethod
    def load_videos(directory):
        videos = []
        path = get_videos_path(directory)
        for filename in os.listdir(path):
            # Skip non json files (such as .gitignore)
            if ".json" not in filename:
                continue

            video_data = json.load(open(path + "/" + filename, "r", encoding="utf8"))

            video = Video(
                video_data['video_id'],
                video_data['video_type'],
                video_data['category'],
                video_data['uploader'],
                video_data['title'],
                video_data['view_count'],
                video_data['video_description'],
                video_data['duration'],
                video_data['published'],
            )

            comments = []
            for comment_data in video_data['comments']:
                if comment_data['text']:
                    comments.append(Comment(
                        comment_data['id'],
                        comment_data['author'],
                        comment_data['text'],
                        comment_data['published'],
                    ))
            video.set_comments(comments)
            videos.append(video)

        return videos

    @staticmethod
    def run():
        print("Loading videos data.")
        automobile_videos = Parser.load_videos("automobiles")
        tablet_videos = Parser.load_videos("tablets")

        Store.videos = automobile_videos + tablet_videos
