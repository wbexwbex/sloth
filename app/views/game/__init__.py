# vim: fileencoding=utf-8
from flask import Blueprint, render_template, jsonify, redirect, url_for
from flask import flash, session, request, g, send_from_directory
from flask.ext.babel import gettext
from ...models import *
from ...utils import passwdHash, requires_login, pjax, generate_menu
from collections import defaultdict
from menu_data import mod

import user_info
import menu2


@mod.route('/ajax/setdomain', methods=['GET'])
def ajax():

    #Access arguments via request.args
    name = request.args.get('name')
    time = request.args.get('time')


    return render_template('ajax.html',
                           name=name,
                           time=time)
