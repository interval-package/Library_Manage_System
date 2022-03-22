from PyQt5.QtWidgets import QMainWindow, QStackedWidget
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

        # 设置登录界面
        self.LoginPage = LoginPage()
        self.stackWidget.addWidget(self.LoginPage)

        # 设置用户界面
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
        for action in self.menuBar().actions():
            action.setEnabled(action.data() != index)

    def switchPageAction(self, action):
        index = action.data()
        if index is not None:
            self.switchPage(index)
