# vim: fileencoding=utf-8


import gevent
import time
import datetime
timeStamp24 = 86400

def GetOffsetSecByTimeSec_day(timeStamp):
    ctime = int(time.time())
    ltime = time.localtime()
    dateC0 = datetime.datetime(ltime.tm_year, ltime.tm_mon, ltime.tm_mday, 0, 0, 0)
    timestamp0 = time.mktime(dateC0.timetuple())
    offset = (timeStamp - ctime + timestamp0) % timeStamp24
    return offset

def GetOffsetSecByTimeSec_hour(timeStamp):
    ctime = int(time.time())
    ltime = time.localtime()
    dateC0 = datetime.datetime(ltime.tm_year, ltime.tm_mon, ltime.tm_mday, ltime.tm_hour, 0, 0)
    timestamp0min = time.mktime(dateC0.timetuple())
    offset = (timestamp0min+3600-time.time() + timeStamp) % 3600
    return offset

def GetOffsetSecByTimeSec_minute(timeStamp):
    ctime = int(time.time())
    ltime = time.localtime()
    dateC0 = datetime.datetime(ltime.tm_year, ltime.tm_mon, ltime.tm_mday, ltime.tm_hour, ltime.tm_min, 0)
    timestamp0sec = time.mktime(dateC0.timetuple())
    offset = (timestamp0sec+60-time.time() + timeStamp) % 60
    return offset


def GetOffsetSecByTimeSec_sec(timeStamp):
    ctime = int(time.time())
    ltime = time.localtime()
    dateC0 = datetime.datetime(ltime.tm_year, ltime.tm_mon, ltime.tm_mday, ltime.tm_hour, ltime.tm_min, ltime.tm_sec)
    timestamp0sec = time.mktime(dateC0.timetuple())
    offset = (timestamp0sec+1-time.time() + timeStamp) % 1
    return offset


# noinspection PyBroadException
def TimerHandlerDay(h, sec, *kw):
    offset = GetOffsetSecByTimeSec_day(sec)
    gevent.sleep(offset)
    while 1:
        try:
            h(*kw)
        except:
            pass
        finally:
            offset = GetOffsetSecByTimeSec_day(sec)
            gevent.sleep(offset or timeStamp24)

# noinspection PyBroadException
def TimerHandlerHour(h, sec, *kw):
    offset = GetOffsetSecByTimeSec_hour(sec)
    gevent.sleep(offset)
    while 1:
        try:
            h(*kw)
        except:
            pass
        finally:
            offset = GetOffsetSecByTimeSec_hour(sec)
            gevent.sleep(offset or 3600)

def TimerHandlerMinute(h, sec, *kw):
    offset = GetOffsetSecByTimeSec_minute(sec)
    gevent.sleep(offset)
    while 1:
        try:
            h(*kw)
        except:
            pass
        finally:
            offset = GetOffsetSecByTimeSec_minute(sec)
            gevent.sleep(offset or 60)




def TimerHandlerOnce(h, offset, *kw):
    gevent.sleep(offset)
    h(*kw)



def main():
    def foo():
        import time
        ltime = time.localtime()
        # gevent.sleep(0.01)
        print ltime

    x = gevent.spawn(TimerHandlerMinute, foo, 0)
    gevent.wait([x])
    pass


if __name__ == "__main__":
    main()
