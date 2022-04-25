import pymssql as sql


class SqlServer(object):
    db = "LibraryManageSystem"

    def __init__(self, host="(local)"):
        self.host = host
        with sql.connect(host=host, database=self.db) as conn:
            if conn is None:
                raise ValueError("invalid host")
        pass

    def CallBase(self):
        conn = sql.connect(host=self.host, database=self.db)
        if not conn:
            raise ValueError("invalid host")
        return conn


tar = SqlServer()


def connGetter():
    return tar.CallBase().cursor()


def connAction(conn, command):
    conn.execute(command)
    return conn


if __name__ == '__main__':
    conn = sql.connect(host='(local)', database='LibraryManageSystem')
    if conn:
        print("valid")
    else:
        exit(-1)
    cur = conn.cursor()
    tar = cur.execute("select * from UserInfo")
    res = cur.fetchall()
    print(res)
    pass
