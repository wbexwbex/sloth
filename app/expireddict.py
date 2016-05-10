# vim: fenc=utf8 ff=unix
# Author: Xiaolan.Lee<chenjiashu@me-game.com>
# Date: 2014-03-03 17:06:23+0800

import time

class ExpiredDict(dict):
    """
    Automatically delete expired keys.
    TODO: Delete expired key even if the key not accessed.
    """
    def __init__(self, expires=3600.):
        if expires <= 0:
            raise ValueError('expires must be positive integer.')
        dict.__init__(self)
        self.expires = expires

    def __getitem__(self, key):
        return dict.__getitem__(self, key)[0]

    def __setitem__(self, key, value):
        expires = self.expires
        return dict.__setitem__(self, key, [value, time.time() + expires])

    def get(self, key, default=None, refresh=False, expire=True):
        expires = self.expires
        try:
            tmp = dict.__getitem__(self, key)
            now = time.time()
            if expire and tmp[1] < now:
                # Delete the key from the underlay dict.
                dict.__delitem__(self, key)
                return None
            if refresh:
                tmp[1] = now + expires
            return tmp[0]
        except KeyError, e:
            return default

