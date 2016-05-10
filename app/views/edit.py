from flask import Blueprint, render_template, jsonify, redirect, url_for
from flask import flash, session, request, g, send_from_directory
from flask.ext.babel import gettext
from ..models import *
from ..models.account import MAccount
from ..utils import passwdHash, requires_admin
import json

mod = Blueprint('edit', __name__, url_prefix='/edit')

import time
from .. import app
from login_form import UserForm


@mod.route('/', methods=['GET'])
@requires_admin
def index():
    roles = get_all_user_image()
    return render_template(
        'user_list.html',
        title='Edit',
        users=roles,
        )


@mod.route('/edit/<string:uin>', methods=['GET', 'post'])
@requires_admin
def edit(uin):
    role = get_user_image_by_uin(uin)
    form = UserForm()
    gids = app.cfg['GROUP_IDS']
    form.group.choices = zip(gids, gids)
    print 'edit uin', uin, form.group.data, form.password.data
    if form.validate_on_submit():
        with sessionScope() as sessionDb:
            _role = sessionDb.query(MAccount).get(form.account.data)
            if _role:
                if _role.passwd != form.password.data:
                    _role.passwd = passwdHash(form.password.data)
                _role.group = unicode(form.group.data)

            return redirect(url_for('edit.index'))
    else:
        form.group.data = role.group

    return render_template(
        'user_edit.html',
        title='Edit',
        op='edit',
        form=form,
        user=role,
    )


@mod.route('/delete/<string:uin>', methods=['GET', 'post'])
@requires_admin
def delete(uin):

    with sessionScope() as sessionDb:
        role = sessionDb.query(MAccount).get(uin)
        if not role:
            flash(gettext('User %(nickname) was not found.', nickname=uin))
        else:
            sessionDb.delete(role)
            sessionDb.commit()
    return redirect(url_for('edit.index'))




@mod.route('/new', methods=['GET', 'post'])
@requires_admin
def new():
    form = UserForm()
    gids = app.cfg['GROUP_IDS']
    form.group.choices = zip(gids, gids)
    if form.validate_on_submit():
        with sessionScope() as sessionDb:
            role = sessionDb.query(MAccount).get(form.account.data)
            if role:
                form.account.errors.append('Repeated account!')
                pass
            else:
                _hash = passwdHash(form.password.data)
                role_root = MAccount(
                    uin=unicode(form.account.data),
                    passwd=_hash,
                    group=unicode(form.group.data),
                    registration_ip=unicode(request.remote_addr),
                )
                sessionDb.add(role_root)
                return redirect(url_for('edit.index'))

    return render_template(
        'user_edit.html',
        title='New',
        op='new',
        form=form,
        user=None,
    )
