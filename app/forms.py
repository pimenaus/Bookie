__author__ = 'Alexey'

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, validators
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    try:
        openid = StringField( 'openid', [Length(min=4, max=250)])
        remember_me = BooleanField('remember_me', default = False)
    except Exception as e:
                raise

