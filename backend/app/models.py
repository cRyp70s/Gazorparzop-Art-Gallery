from datetime import datetime

# import flask_whooshalchemy3
# from whoosh.analysis import StemmingAnalyzer

from . import db


class GalleryEntry(db.Model):
    __tablename__ = "galleries"
    __searchable__ = ["title", "collection", "description"]  # indexed fields
    # __analyzer__ = StemmingAnalyzer()
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    artist = db.Column(db.String(255))
    sample_img_url = db.Column(db.String(255))
    description = db.Column(db.Text)
    collection = db.Column(db.String(20))
    created = db.Column(db.DateTime, default=datetime.utcnow)
