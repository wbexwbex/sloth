import hashlib
from datetime import datetime, timedelta
from functools import wraps
from flask.ext.babel import gettext
from flask import render_template, g, session, url_for, flash, abort, request, redirect, Markup
from . import app
from collections import defaultdict

def is_admin(uin):
    return uin in app.cfg['ADMINS_UIN']

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        uin = session.get('uin', None)
        token = session.get('token', None)
        if not uin or not token or app.user_dict.get(uin, 'None') != token:
            flash(gettext(u'You need to be signed in for this page.'))
            return redirect(url_for('login.index', next=request.path))
        return f(*args, **kwargs)
    return decorated_function

def requires_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        uin = session.get('uin', None)
        if not uin or not is_admin(uin):
            abort(401)
        return f(*args, **kwargs)
    return requires_login(decorated_function)




def format_datetime(dt):
    return dt.strftime('%Y-%m-%d @ %H:%M')


def format_date(dt):
    return dt.strftime('%Y-%m-%d')


def passwdHash(passwd):
    _salt = u'slothAccount'
    return unicode(hashlib.sha1(_salt + passwd).hexdigest())


# menu_list = {
#     1: {
#         0: ('name10', 'icon10',),
#     },
#     2: {
#         0: ('name20', 'icon20',),
#         1: ('name21', 'icon22',),
#     },
# }
menu_list = defaultdict(lambda: {})
def pjax(template, base_html='game_base.html', **kw):
    """Test whether the request was with PJAX or not."""
    if "X-PJAX" in request.headers:
        return render_template(template)

    return render_template(base_html, template=template, menu_list=menu_list, **kw)
