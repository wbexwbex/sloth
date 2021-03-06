#!/usr/local/bin/python
from gevent import monkey
monkey.patch_thread()
monkey.patch_all()
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URIS
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URIS['main']
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
