from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from PyQt5 import QtGui

from Window_Classes.MainWindow.MainWindow import Ui_MainWindow

from Window_Classes.LoginPage.LoginPageWrapper import LoginPage

from Window_Classes.UserPage.UserPageWrapper import UserPage

from Window_Classes.UtilPages.SignUpPage.SignUpPageWrapper import SignUpPage

from Window_Classes.UtilPages.RentingPage.RentingPageWrapper import RentingPage

from Window_Classes.UtilPages.ReturnPage.ReturnPageWrapper import ReturnPage


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
        self.LoginPage.SignUpButton.clicked.connect(lambda: self.switchPage(2))

        # 设置用户界面,1
        self.UserPage = UserPage()
        self.stackWidget.addWidget(self.UserPage)

        # 设置注册界面,2
        self.SignUpPage = SignUpPage()
        self.stackWidget.addWidget(self.SignUpPage)

        # 注册逻辑
        self.SignUpPage.SignUpButton.clicked.connect(self.SignUpPage_SignUpAction_Bind)
        self.SignUpPage.GoBackButton.clicked.connect(lambda: self.switchPage(0))

        # 设置借书界面,3
        self.RentingPage = RentingPage()
        self.stackWidget.addWidget(self.RentingPage)

        # 借阅逻辑
        self.UserPage.RentButton.clicked.connect(lambda: self.switchPage(3))

        # 设置归还界面,4
        self.ReturnPage = ReturnPage()
        self.stackWidget.addWidget(self.ReturnPage)

        # 归还逻辑
        self.UserPage.RentButton.clicked.connect(lambda: self.switchPage(4))

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

    # login page actions

    def LoginPage_Login(self):
        User = self.LoginPage.Login()
        if User is not None:
            self.UserPage.SetUser(User)
            self.switchPage(1)
            pass

    # rent and return

    # action for sign up page

    def SignUpPage_SignUpAction_Bind(self):
        flag = self.SignUpPage.SignUp_Action()
        if flag:
            self.switchPage(0)
        pass


# def clicked_1(self):
#     self.right_widget1.hide() # 隐藏界面1
#     self.right_widget2.show() # 显示界面2

