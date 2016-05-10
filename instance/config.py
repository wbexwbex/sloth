# -*- coding: utf-8 -*-

import os
from config import basedir

SQLALCHEMY_ECHO = True
DEBUG = True

SECRET_KEY = 'you-will-never-guess'
BCRYPT_LEVEL = 12  # Configuration for the Flask-Bcrypt extension



# mail server settings
MAIL_SERVER = 'localhost'
# MAIL_SERVER = 'submail.cn'
MAIL_PORT = 1025
# MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# ...

# administrator list
ADMINS = ['987978874@qq.com']

# microsoft translation service
MS_TRANSLATOR_CLIENT_ID = 'myWebApp01' # enter your MS translator app id here
MS_TRANSLATOR_CLIENT_SECRET = 'SbgFB1wwrtckcuQC8kqzDhG8IIbKL4x42C0tUrGDOaQ=' # enter your MS translator app secret here




