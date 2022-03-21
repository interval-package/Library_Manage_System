import sqlite3 as sql
# import ... other sql libs
import abc
import os
import warnings


class DataBaseAct(object):
    # ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

    data_path = os.path.join(os.getcwd(), 'data', 'library_info_core.db')

    def __init__(self, action: str):
        self.data_path = os.path.join(os.getcwd(), 'data', 'database', 'library_info_core.db')
        self.info = self.getInfo(action)
        pass

    @abc.abstractmethod
    def getInfo(self, action):
        # conn = sqlite3.connect(self.data_path)
        with sql.connect(self.data_path) as conn:
            cur = conn.cursor()
            info = cur.execute(action)
        return info


# 对数据管理进行了尝试，对于数据模型的设计还是用sql语言来进行实现，我们这里只要进行访问就行了
if __name__ == '__main__':
    data_path = os.path.join(os.getcwd(), 'data', 'library_info_core.db')
    print(data_path)

    sqlCommand = 'insert into book (BookId, BookName) values(?, ?)'
    datas = [
        (23, 'book1'),
        (123, 'book2'),
    ]
    # conn = sqlite3.connect(data_path)
    with sql.connect(data_path) as conn:
        try:
            conn.executemany(sqlCommand, datas)
        except Exception as e:
            warnings.warn(repr(e))
            pass
        cursor = conn.execute("select * from User")
        print(cursor)
        for row in cursor:
            for i in row:
                print(i)

