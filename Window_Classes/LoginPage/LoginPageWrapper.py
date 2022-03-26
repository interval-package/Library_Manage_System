from PyQt5.QtWidgets import QMessageBox

from Window_Classes.LoginPage.LoginPage import *
from kernel.Actions.user_login import *


class LoginPage(QtWidgets.QWidget, Ui_LoginPage):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)

    # 这里要负责绑定登录的逻辑

    def Login(self):
        user = self.UserId_Getter.text()
        password = self.Password_Getter.text()
        print(type(user), type(password))
        print(user == '')
        if user == '' or password == '':
            self.Echo_Login_Empty()
            return None
        print(user, password)
        self.Echo_Login_Failed()
        return None

    def Echo_Login_Failed(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Login Error!")
        msg.setText("Please try your id and Password again")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def Echo_Login_Empty(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Login Error!")
        msg.setText("Check your input! It's empty!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
