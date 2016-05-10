#!/usr/local/bin/python
from gevent import monkey
monkey.patch_thread()
monkey.patch_all()

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URIS
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URIS['main']
from config import SQLALCHEMY_MIGRATE_REPO
from app.models import dbs
_base = dbs['main'].base
_engine = dbs['main'].engine
import os.path

_base.metadata.create_all(_engine)

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

