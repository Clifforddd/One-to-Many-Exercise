"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://icon-library.com/images/default-user-icon/default-user-icon-13.jpg"

def connect_db(app):

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User Model"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    first_name = db.Column(db.Text, nullable  = False)

    last_name = db.Column(db.Text, nullable  = False)

    image_url = db.Column(db.Text, nullable = False, default = DEFAULT_IMG_URL)

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    """Post Model"""

    __tablename__ = "Post"

    id = db.Column(db.Integer, primary_key = True)

    content = db.Column(db.Text, nullable  = False)

    created_at = db.Column(db.DateTime, nullable  = False, default = datetime.datetime.now)

    user_table = db.Column(db.Integer, db,ForeignKey("user.id"), nullable  = False)

    @property
    def friendly_date(self):
        """Return time."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")


def connect_db(app):

    db.app = app
    db.init_app(app)

