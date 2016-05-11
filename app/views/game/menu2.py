# vim: fileencoding=utf-8
from menu_data import mod, menu_list
from flask.ext.babel import gettext
from ...utils import passwdHash, requires_login, pjax, generate_menu


@generate_menu(menu_list, mod, gettext(u'查询功能'), 'glyphicon-cog', 2, 0)
def stuff_menu2():
    pass


@mod.route('/login', methods=['GET'])
@requires_login
@generate_menu(menu_list, mod, gettext(u'登陆详情'), 'glyphicon-user', 2, 1)
def login():

    return pjax(menu_list, 'game/login.html', title='Game Login',)


@mod.route('/login1', methods=['GET'])
@requires_login
@generate_menu(menu_list, mod, gettext(u'登陆详情1'), 'glyphicon-user', 2, 2)
def login1():

    return pjax(menu_list, 'game/login.html', title='Game Login1',)

