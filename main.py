import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from DataLoader import DataBaseAct, sql


if __name__ == '__main__':
    # 连接数据库

    conn = sql.connect(DataBaseAct.data_path)

