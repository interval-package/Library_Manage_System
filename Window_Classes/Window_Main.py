from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from PyQt5 import QtGui

from Window_Classes.MainWindow.MainWindow import Ui_MainWindow

from Window_Classes.LoginPage.LoginPageWrapper import LoginPage
# except ModuleNotFoundError:
#     from MainWindow_Login import Ui_MainWindow_Login

from Window_Classes.UtilPages.UserPage.UserPageWrapper import UserPage


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # 先设置User为空
        self.User = None

        self.setupUi(self)
        # 设置页面
        self.stackWidget = QStackedWidget()

        # 设置登录界面,0
        self.LoginPage = LoginPage()
        self.stackWidget.addWidget(self.LoginPage)

        # 设置信号与槽的连接-登录界面
        self.LoginPage.LoginButton.clicked.connect(self.LoginPage_Login)

        # 设置用户界面,1
        self.UserPage = UserPage()
        self.stackWidget.addWidget(self.UserPage)

        # 收尾设置
        self.Pages = self.LoginPage, self.UserPage

        # 设置图标
        self.setIcon()

        # 将页面置放于窗体中间
        self.setCentralWidget(self.stackWidget)
        self.switchPage(0)
        pass

    def setIcon(self):
        # 由于路径问题需要重新设置一下icon的路径
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def switchPage(self, index):
        self.stackWidget.setCurrentIndex(index)

    def LoginPage_Login(self):
        User = self.LoginPage.Login()
        if User is not None:
            self.UserPage.SetUser(User)
            self.switchPage(1)
            pass

