
from init import *


if __name__ == '__main__':

    # 连接数据库，还是不要那么跳进行with操作了
    print(DataBaseAct.data_path)
    # conn = sql.connect(DataBaseAct.data_path)

    # 修正，对于数据库操作应当是每次使用的时候进行一次连接

    # 初始化软件，这是必要操作
    app = QApplication(sys.argv)

    # 创建窗体对象
    win = MainWindow()
    win.show()

    # 结束所有逻辑，之前所有循环的逻辑结束
    # conn.close()
    sys.exit(app.exec_())
