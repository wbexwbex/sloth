#!/usr/local/bin/python
from gevent import monkey
monkey.patch_thread()
monkey.patch_all()
import app

def run_flask():
    app.app.debug = True
    app.app.run(host='0.0.0.0')

def run_gevent():
    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('', 5000), app.app)
    http_server.serve_forever()

if __name__ == "__main__":
    run_flask()
    # run_gevent()

