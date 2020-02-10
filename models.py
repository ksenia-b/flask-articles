from app import db
from datetime import datetime
from sqlalchemy import DateTime
from flask_security import UserMixin, RoleMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    user_name = db.Column(db.String(255))
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    register_day = db.Column(db.String(255))
    # active = db.Column(db.Boolean())
    # roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    def __init__(self, *args, **kwargs):
        # * =list
        # ** = dict Key Word args = named paramether
        super(User, self).__init__(*args, **kwargs)
    #     self.generate_slug()
    #
    # def generate_slug(self):
    #     if self.title:
    #         self.slug = slugify(self.title)


class Article(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    slug = db.Column(db.String(140), unique=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    created = db.Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        # * =list
        # ** = dict Key Word args = named paramether
        super(Article, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
