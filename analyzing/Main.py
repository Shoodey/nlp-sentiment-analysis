import json

from Config import Config
from Store import Store
from analyzing.Analyzer import Analyzer
from sentube.Parser import Parser

Parser.run()

for corpus in Config.corpora:
    print("Using " + corpus.upper())
    print("Analyzing...")
    Config.corpus = corpus
    Analyzer.run(corpus)
    print("Saving...")

    videos = []
    for video_data in Store.videos:
        video = {
            'id': video_data.id,
            'type': video_data.type,
            'category': video_data.category,
            'uploader': video_data.uploader,
            'title': video_data.title,
            'view_count': video_data.view_count,
            'description': video_data.description,
            'duration': video_data.duration,
            'published': video_data.published,
            'comments': []
        }
        for comment_data in video_data.comments:
            video['comments'].append({
                'id': comment_data.id,
                'author': comment_data.author,
                'text': comment_data.text,
                'published': comment_data.published,
                'sentiments': comment_data.sentiments,
            })

        videos.append(video)

    with open('output/' + corpus + '/videos.json', 'w') as output:
        json.dump(videos, output)
