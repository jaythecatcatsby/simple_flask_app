from app import db
from urllib.parse import urlparse
class videos(db.Model):
    Id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    tags = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Integer(), nullable=False)
    stars = db.Column(db.String(30), nullable=True)
    thumbnail = db.Column(db.String(200), nullable=False)
 
    #username = db.Column(db.String(64), index=True, unique=True)
    #email = db.Column(db.String(120), index=True, unique=True)
    #password_hash = db.Column(db.String(128))

    def __repr__(self):
       return f"videos('{self.title}','{self.url}')"
