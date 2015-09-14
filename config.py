__author__ = 'Alexey'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'go-kill-yourself'
OPENID_PROVIDERS=[
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
    {'name': 'Google2', 'url': 'https://accounts.google.com/o/oauth2/auth'}
]
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
