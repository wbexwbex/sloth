from gevent import monkey
import gevent

monkey.patch_thread()
monkey.patch_all()
import os
from flask import Flask, session, g, render_template, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.mail import Mail
from flask.ext.babel import Babel, lazy_gettext
# from config import basedir, ADMINS
from momentjs import momentjs
from expireddict import ExpiredDict

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
import config as cfg
app.cfg = cfg.__dict__
# db = SQLAlchemy(app)
mail = Mail(app)
babel = Babel(app)

app.user_dict = ExpiredDict()
# if not app.debug:
#     import logging
#     from logging.handlers import SMTPHandler
#     credentials = None
#     if MAIL_USERNAME or MAIL_PASSWORD:
#         credentials = (MAIL_USERNAME, MAIL_PASSWORD)
#     mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
#     mail_handler.setLevel(logging.ERROR)
#     app.logger.addHandler(mail_handler)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('microblog startup')




@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# @app.before_request
# def load_current_user():
#     g.user = User.query.filter_by(openid=session['openid']).first() \
#         if 'openid' in session else None


# @app.teardown_request
# def remove_db_session(exception):
#     db_session.remove()


# @app.context_processor
# def current_year():
#     return {'current_year': datetime.utcnow().year}


# from app import views, models
from views import login, game, edit

app.register_blueprint(login.mod)
app.register_blueprint(game.mod)
app.register_blueprint(edit.mod)


from analysis_server_list import refresh_server_info
from timer_handler import TimerHandlerDay, TimerHandlerOnce
gevent.spawn(TimerHandlerOnce, refresh_server_info, 0, app)
app.h_timer_server_info = gevent.spawn(TimerHandlerDay, refresh_server_info, 24*3600, app)



from gevent.backdoor import BackdoorServer
import socket
import errno
port = 10415
while True:
    try:
        bds = BackdoorServer(('', port), locals())
        bds.start()
        break
    except socket.error, e:
        if e[0] == errno.EADDRINUSE:
            port += 1
        else:
            raise



