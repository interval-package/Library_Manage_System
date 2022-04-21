import pymssql as sql


class SqlServer(object):
    def __init__(self):
        self.connect = sql.connect('(local)')
        if self.connect:
            print("valid!")
            self.cur = self.connect.cursor()
        else:
            self.cur = None
        pass
