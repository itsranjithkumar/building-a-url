import string

from.extensions import db

from datatime import datetime # type: ignore
from random import choices

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)
    visits = db.Column(db.Integer, default=0)
    data_create = db.Column(db.DateTime,default=datetime.now)

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.short_url = 'something'

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=3))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            self.generate_short_link()

        return short_url