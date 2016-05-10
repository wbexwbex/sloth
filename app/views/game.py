# vim: fileencoding=utf-8
from flask import Blueprint, render_template, jsonify, redirect, url_for
from flask import flash, session, request, g, send_from_directory
from flask.ext.babel import gettext
from ..models import *
from ..models.account import MAccount
from ..utils import passwdHash, requires_login, pjax, menu_list
from collections import defaultdict
from collections import namedtuple

mod = Blueprint('game', __name__, url_prefix='/game')

import time
from functools import wraps

MenuInfo = namedtuple('MenuInfo', ('title', 'icon', 'endpoint',))
def generate_menu(name, icon, level, row=1):
    def register_handler(handler):
        menu_list[level][row] = MenuInfo(name, icon, '%s.%s' % (mod.name, handler.func_name,))
        print icon, level, row, handler.func_name
        print menu_list
        return handler

    return register_handler



@mod.route('/', methods=['GET'])
@mod.route('/user/', methods=['GET'])
@requires_login
@generate_menu(gettext(u'用户信息'), 'glyphicon-th-large', 1, 0)
def index():

    return pjax('game/user.html', title='Game',)

    # return render_template(
    #     'game/user.html',
    #     title='Game',
    #     )


@generate_menu(gettext(u'查询功能'), 'glyphicon-cog', 2, 0)
def stuff_menu2():
    pass


@mod.route('/login', methods=['GET'])
@requires_login
@generate_menu(gettext(u'登陆详情'), 'glyphicon-user', 2, 1)
def login():

    return pjax('game/login.html', title='Game Login',)

    # return render_template(
    #     'game/login.html',
    #     title='Game Login',
    # )


@mod.route('/login1', methods=['GET'])
@requires_login
@generate_menu(gettext(u'登陆详情1'), 'glyphicon-user', 2, 2)
def login1():

    return pjax('game/login.html', title='Game Login1',)

    # return render_template(
    #     'game/login.html',
    #     title='Game Login',
    # )
