from sqlalchemy import (create_engine, Column, Integer,
    String, DateTime, ForeignKey, event)
from sqlalchemy.orm import sessionmaker, backref, relation, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# from werkzeug import cached_property, http_date

from flask import url_for, Markup, session


from collections import namedtuple
from contextlib import contextmanager
from datetime import datetime, date

from .. import app

__all__ = [
    'Session',
    'sessionScope',
    'Base',
    'dbs',
    'get_current_user',
    'get_current_user_image',
    'get_all_user',
    'get_all_user_image',
    'get_user_by_uin',
    'get_user_image_by_uin',


]


# engine = create_engine(config['DATABASE_URI'],
#                        convert_unicode=True,
#                        **config['DATABASE_CONNECT_OPTIONS'])
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
#

debug = app.cfg.get('debug', False)

dbs = dict()
Database = namedtuple('Database', ('engine', 'session', 'base'))
for key, dbUrl in app.cfg['SQLALCHEMY_DATABASE_URIS'].items():
    # if dbUrl.startswith('mysql://'):
    #   __import__('umysqldb').install_as_MySQLdb()

    _engine = create_engine(dbUrl, echo=debug, encoding='utf-8', pool_recycle=60*60)
    _session = sessionmaker(bind=_engine)
    if key == 'main':
        from account import Base as _base
        # _base.bind = _engine
    else:
        _base = declarative_base(bind=_engine)
    _base.__db__ = dbs[key] = Database(engine=_engine, session=_session, base=_base)
    # _base.metadata.create_all(_engine)


Session = dbs['main'].session
Base = dbs['main'].base


def refresh_sqlalchemy_database_uris():
    for key, dbUrl in app.cfg['SQLALCHEMY_DATABASE_URIS'].items():
        if key == 'main':
            pass
        else:
            _engine = create_engine(dbUrl, echo=debug, encoding='utf-8', pool_recycle=60*60)
            _session = sessionmaker(bind=_engine)
            _base = declarative_base(bind=_engine)
            _base.__db__ = dbs[key] = Database(engine=_engine, session=_session, base=_base)




@contextmanager
def sessionScope(sessionClass=Session):
    session = sessionClass()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()



from account import MAccount, MAccountTuple
def get_current_user():
    uin = session.get('uin', None)
    role = None
    with sessionScope() as sessionDb:
        role = sessionDb.query(MAccount).get(uin)
        yield role

def get_current_user_image():
    uin = session.get('uin', None)
    role = None
    account_tuple = None
    with sessionScope() as sessionDb:
        role = sessionDb.query(MAccount).get(uin)
        account_tuple = MAccountTuple(role.uin, role.passwd, role.group, role.registration_ip, role.registration_date)

    return account_tuple

def get_all_user():
    roles = None
    with sessionScope() as sessionDb:
        roles = sessionDb.query(MAccount).all()
        for role in roles or []:
            yield role

def get_all_user_image():
    roles = None
    role_list = []
    with sessionScope() as sessionDb:
        roles = sessionDb.query(MAccount).all()
        for role in roles or []:
            account_tuple = MAccountTuple(role.uin, role.passwd, role.group, role.registration_ip, role.registration_date)
            role_list.append(account_tuple)

    return role_list

def get_user_by_uin(uin):
    role = None
    with sessionScope() as sessionDb:
        role = sessionDb.query(MAccount).get(uin)
        yield role

def get_user_image_by_uin(uin):
    role = None
    account_tuple = None
    with sessionScope() as sessionDb:
        role = sessionDb.query(MAccount).get(uin)
        account_tuple = MAccountTuple(role.uin, role.passwd, role.group, role.registration_ip, role.registration_date)

    return account_tuple


