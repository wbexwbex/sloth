# vim: fileencoding=utf-8
from menu_data import mod, menu_list
from flask.ext.babel import gettext
from ...utils import passwdHash, requires_login, pjax, generate_menu
from ... import app
from user_form import UserForm
from flask import flash, session, request, g, send_from_directory, render_template

from ...models import dbs, sessionScope


@generate_menu(menu_list, mod, gettext(u'用户信息'), 'glyphicon-th-large', 1, 0)
def stuff_menu1():
    pass


@mod.route('/', methods=['GET'])
@mod.route('/user/', methods=['GET', 'POST'])
@requires_login
@generate_menu(menu_list, mod, gettext(u'用户查询'), 'glyphicon-th-large', 1, 1)
def index():

    form = UserForm()
    print request
    print request.method, request.form

    if request.method == 'POST':
        print form.roleid.data, session['_domain'], session['_server']
        print dbs[session['_server']]
        with sessionScope(dbs[session['_server']].session) as sessionDb:
            sql='SELECT `role_id`,`name`,`name`,`registration_time`,`runestone`,`gold`,`vip`,`lv` FROM role LIMIT 10;'
            result = sessionDb.execute(sql)
            row = result.fetchall()
            print row

        return pjax(menu_list, 'game/user.html',
                    subpage='game/user_detail.html', title='Game',
                    pyDomainDict=app.cfg['domainDict'], userform=form, users=row)

    return pjax(menu_list, 'game/user.html', title='Game',
                pyDomainDict=app.cfg['domainDict'], userform=form)

