from flask import Blueprint, render_template, jsonify, redirect, url_for
from flask import flash, session, request, g, send_from_directory
from flask.ext.babel import gettext
from ..models import *
from ..models.account import MAccount
from ..utils import passwdHash
from .. import app
import os

mod = Blueprint('login', __name__, url_prefix='/login')

from login_form import LoginForm
import time




def get_login_cd(_session, ctime):
    if 'login_cd' not in _session:
        _session['login_cd'] = 0
        _session['login_times'] = 0
        _session['login_cd_second'] = 0
    elif _session['login_cd'] != 0:
        _session['login_cd_second'] = max(0, _session['login_cd']-ctime)
    else:
        pass

def set_login_cd(_session, ctime, succ=False):
    if succ:
        _session['login_cd'] = 0
        _session['login_cd_second'] = 0
        _session['login_times'] = 0
    else:
        _session['login_times'] += 1
        cd = max(3, 2 ** _session['login_times'])
        _session['login_cd'] = ctime+cd
        _session['login_cd_second'] = cd

def check_login_cd(_session, ctime):
    if ctime <= _session['login_cd']:
        return False
    else:
        return True


def userLogin(uin, _session):
    token = os.urandom(10)
    _session['token'] = token
    _session['uin'] = uin
    app.user_dict[uin] = token

@mod.route('/init-root', methods=['GET', 'POST'])
def init_root():
    print 'login uin',session.get('uin',None)
    ctime = time.time()
    form = LoginForm()
    get_login_cd(session, ctime)

    if form.validate_on_submit():
        if not check_login_cd(session, ctime):
            return redirect(url_for('login.index'))
        if form.account.data != u'root':
            return render_template('404.html')
        else:
            pass

        with sessionScope() as sessionDb:
            role = sessionDb.query(MAccount).get(form.account.data)
            _hash = passwdHash(form.password.data)
            if not role:
                role_root = MAccount(
                    uin=u'root',
                    passwd=_hash,
                    group=u'root',
                    registration_ip=unicode(request.remote_addr),
                )
                sessionDb.add(role_root)
                userLogin(role_root.uin, session)
                return redirect(url_for('edit.index'))
            else:
                if role.passwd == _hash:
                    set_login_cd(session, ctime, succ=True)
                    userLogin(role.uin, session)
                    return redirect(url_for('edit.index'))
                else:
                    set_login_cd(session, ctime, succ=False)
                    return redirect(url_for('login.init_root'))

        return render_template('404.html')
    else:
        pass

    return render_template(
        'login.html',
        title='InitRoot',
        form=form)

@mod.route('/', methods=['GET', 'POST'])
def index():
    ctime = time.time()
    form = LoginForm()
    get_login_cd(session, ctime)
    if form.validate_on_submit():
        if not check_login_cd(session, ctime):
            return redirect(url_for('login.index'))

        login_succ = False
        with sessionScope() as sessionDb:
            role = sessionDb.query(MAccount).get(form.account.data)
            _hash = passwdHash(form.password.data)
            if role and role.passwd == _hash:
                userLogin(role.uin, session)
                login_succ = True

        if login_succ:
            set_login_cd(session, ctime, succ=True)
            return redirect(url_for('game.index'))
        else:
            set_login_cd(session, ctime, succ=False)
            return redirect(url_for('login.index'))
    else:
        pass

    return render_template(
        'login.html',
        title='Login',
        form=form)
