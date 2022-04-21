QueryMethod = 'sqlite'

if QueryMethod == 'sqlite':
    from kernel.QueryInfoSite.QueryInfo_sqlite import *
elif QueryMethod == 'sql_server':
    from kernel.QueryInfoSite.QueryInfo_MsSql import *

if __name__ == '__main__':
    pass
