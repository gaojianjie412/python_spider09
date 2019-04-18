
from mongoengine import *


class Comic(Document):
    comic_id = StringField(max_length=32)
    name = StringField(max_length=256)
    cover = StringField(max_length=1024)
    line2 = StringField(max_length=512)


class ComicChapter(Document):
    comic_id = StringField(max_length=32)
    chapter_id = StringField(max_length=32)
    chapter_url = StringField(max_length=1024)
    title = StringField(max_length=128)