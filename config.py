# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# CSRF_ENABLED = True
SQLALCHEMY_ECHO = False
DEBUG = False

WHOOSH_BASE = os.path.join(basedir, 'search.db')

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

# available languages
LANGUAGES = {
    'en': u'English',
    'es': u'Español',
    'zh': u'中文',
}


# pagination
POSTS_PER_PAGE = 50
MAX_SEARCH_RESULTS = 50

ADMINS_UIN = frozenset(['root'])
GROUP_IDS = ('root', 'xn')



# SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/xndb'
SQLALCHEMY_DATABASE_URIS = {
    'main': 'mysql://root:@localhost:3306/xndb',
}
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True


