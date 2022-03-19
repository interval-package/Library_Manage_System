import sqlite3
import abc
import os


class DataBaseAct(object):
    # ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, action: str):
        self.data_path = os.path.join(os.getcwd(), 'Data', 'info.bd', )

        self.info = self.getInfo(action)
        pass

    @abc.abstractmethod
    def getInfo(self, action):
        conn = sqlite3.connect(self.data_path)
        cur = conn.cursor()
        info = cur.execute(action)
        return info


if __name__ == '__main__':
    DataBaseAct('create table stu')
