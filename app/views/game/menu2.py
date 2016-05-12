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



def change_func_name(name):
    def register_handler(handler):
        handler.__name__ = name
        return handler

    return register_handler


for i in xrange(3, 20):
    @mod.route('/login%s' % i, methods=['GET'])
    @requires_login
    @generate_menu(menu_list, mod, gettext(u'登陆详情%s' % i), 'glyphicon-user', 2, i)
    @change_func_name('login%s' % i)
    def loginx():
        return pjax(menu_list, 'game/login.html', title='Game Login%s' % i,)

