__author__ = 'Alexey'

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120),index = True, unique=True)
    hashed_password = db.Column(db.String(120), index = False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(120), index = True, unique = False)
    last_name = db.Column(db.String(120),index = True, unique=False)
    books = db.relationship('Book', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return '<Author %r %f>' % (self.first_name,self.last_name)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64), index = True, unique = True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return '<Book %r>' % (self.title)