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


@mod.route('/ajax/setdomain/', methods=['GET'])
def set_domain():

    #Access arguments via request.args
    domain = request.args.get('domain')
    server = request.args.get('server')
    ret = {
        "code": 0,
        "domain": domain,
        "server": server,
    }
    print domain, server
    session['_domain'] = domain
    session['_server'] = server

    return jsonify(ret)
