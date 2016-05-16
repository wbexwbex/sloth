# vim: fileencoding=utf-8
from menu_data import mod, menu_list
from flask.ext.babel import gettext
from ...utils import passwdHash, requires_login, pjax, generate_menu
from ... import app



@mod.route('/', methods=['GET'])
@mod.route('/user/', methods=['GET'])
@requires_login
@generate_menu(menu_list, mod, gettext(u'用户信息'), 'glyphicon-th-large', 1, 0)
def index():

    print app.cfg['domainDict']
    return pjax(menu_list, 'game/user.html', title='Game', pyDomainDict=app.cfg['domainDict'])

