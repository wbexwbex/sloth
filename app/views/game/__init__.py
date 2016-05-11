# vim: fileencoding=utf-8
from flask import Blueprint, render_template, jsonify, redirect, url_for
from flask import flash, session, request, g, send_from_directory
from flask.ext.babel import gettext
from ...models import *
from ...utils import passwdHash, requires_login, pjax, generate_menu
from collections import defaultdict

mod = Blueprint('game', __name__, url_prefix='/game')
menu_list = defaultdict(lambda: {})

import time


@mod.route('/', methods=['GET'])
@mod.route('/user/', methods=['GET'])
@requires_login
@generate_menu(menu_list, mod, gettext(u'用户信息'), 'glyphicon-th-large', 1, 0)
def index():

    return pjax(menu_list, 'game/user.html', title='Game',)

    # return render_template(
    #     'game/user.html',
    #     title='Game',
    #     )


@generate_menu(menu_list, mod, gettext(u'查询功能'), 'glyphicon-cog', 2, 0)
def stuff_menu2():
    pass


@mod.route('/login', methods=['GET'])
@requires_login
@generate_menu(menu_list, mod, gettext(u'登陆详情'), 'glyphicon-user', 2, 1)
def login():

    return pjax(menu_list, 'game/login.html', title='Game Login',)

    # return render_template(
    #     'game/login.html',
    #     title='Game Login',
    # )


@mod.route('/login1', methods=['GET'])
@requires_login
@generate_menu(menu_list, mod, gettext(u'登陆详情1'), 'glyphicon-user', 2, 2)
def login1():

    return pjax(menu_list, 'game/login.html', title='Game Login1',)

    # return render_template(
    #     'game/login.html',
    #     title='Game Login',
    # )