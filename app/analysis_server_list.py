from collections import defaultdict
import gevent




def refresh_server_info(app):
    cfg = app.cfg
    uris = cfg['SQLALCHEMY_DATABASE_URIS']
    domainSet = set()
    with open(cfg['server_list_path'], 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\r\n ')
            items = line.split(',')
            if len(items) >= 14:
                domain = items[1]
                server_name = items[5]
                db_host = items[6]
                db_port = items[7]

                db_name = items[8]
                db_user = items[9]
                db_passwd = items[10]

                domainSet.add(domain)

                cfg['domainDict'][domain].append(server_name)
                cfg['serverDict'][server_name] = items
                uris[server_name] = 'mysql://%s:%s@%s:%s/%s' % (db_user, db_passwd, db_host, db_port, db_name)

    cfg['domainList'].extend(list(domainSet))
    import models
    models.refresh_sqlalchemy_database_uris()

    # print cfg['domainList']
    # print cfg['serverDict']
    # print cfg['domainDict']
