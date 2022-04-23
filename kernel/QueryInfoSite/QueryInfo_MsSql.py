import pymssql as sql


class SqlServer(object):
    db = "LibraryManageSystem"

    def __init__(self, host="(local)"):
        self.host = host
        with sql.connect(host=host, database=self.db) as conn:
            if ~conn:
                raise ValueError("invalid host")
        pass

    def CallBase(self):
        conn = sql.connect(host=self.host, database=self.db)
        if ~conn:
            raise ValueError("invalid host")
        return conn


if __name__ == '__main__':
    conn = sql.connect(host='(local)', database='LibraryManageSystem')
    if conn:
        print("valid")
    else:
        exit(-1)
    cur = conn.cursor()
    cur.execute("select * from UserInfo")
    res = cur.fetchall()
    print(res)
    pass
