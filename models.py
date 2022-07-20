"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://icon-library.com/images/default-user-icon/default-user-icon-13.jpg"

def connect_db(app):

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User Model"""
    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    first_name = db.Column(db.Text, nullable  = False)

    last_name = db.Column(db.Text, nullable  = False)

    image_url = db.Column(db.Text, nullable = False, default = DEFAULT_IMG_URL)

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"