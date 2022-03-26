from PyQt5.QtWidgets import QMessageBox

from Window_Classes.LoginPage.LoginPage import *
from DataLoader import sql, data_path, quote
from kernel.Users import UserGet


class LoginPage(QtWidgets.QWidget, Ui_LoginPage):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)

    # 这里要负责绑定登录的逻辑

    def Login(self):
        user = self.UserId_Getter.text()
        password = self.Password_Getter.text()
        print(user, password)
        return self.LoginResult(user, password)

    def LoginResult(self, user_id: str, password: str):
        if user_id == '' or password == '':
            self.Echo_Login_Empty()
            return None
        with sql.connect(data_path) as conn:
            try:
                cursor = conn.execute("""
                    select * from User
                    where UserId = %s
                    and Password = %s
                    """ % (quote(user_id), quote(password)))
            except sql.DatabaseError as e:
                # 先放这个，不能没有显示
                cursor = None
                print(repr(e))
                pass
            if cursor is not None:
                res = cursor.fetchall()
            else:
                self.MultiUserErrorFind()
        print(res)
        if res:
            if len(res) > 1:
                self.MultiUserErrorFind()
            else:
                self.Echo_Login_Success()
                return UserGet(res[0])
        else:
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

    def Echo_Login_Success(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Login!")
        msg.setText("Success!")
        msg.exec_()

    def MultiUserErrorFind(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Error!")
        msg.setText("Find more than 1 user! Contact the OP!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        exit(1)
