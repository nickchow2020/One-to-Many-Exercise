"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy() 

def connect_db(arr):
    db.app = arr 
    db.init_app(arr)


class User (db.Model):
    """User"""

    __tablename__ = "users"

    def __repr__(self):
        return f"user first name is {self.first_name} and last name is {self.last_name}, id {self.id}"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    first_name = db.Column(db.String(30),
                            nullable=False)

    last_name = db.Column(db.String(20),
                            nullable=False)
    
    image_url = db.Column(db.String,
                            nullable=False)

    def greeting(self):
        return f"Hi,my name is {self.first_name} {self.last_name}!"

class Post(db.Model):
    """Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.Text,nullable=False)

    content = db.Column(db.Text,nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    user = db.relationship('User',backref='posts')