# vim: fileencoding=utf-8
from menu_data import mod, menu_list
from flask.ext.babel import gettext
from ...utils import passwdHash, requires_login, pjax, generate_menu
from ... import app
from user_form import UserForm
from flask import flash, session, request, g, send_from_directory, render_template

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
    # if form.validate_on_submit():
        print 'validate_on_submit'
        return pjax(menu_list, 'game/user.html',
                    subpage='game/user_detail.html', title='Game',
                    pyDomainDict=app.cfg['domainDict'], userform=form)

    return pjax(menu_list, 'game/user.html', title='Game',
                pyDomainDict=app.cfg['domainDict'], userform=form)

