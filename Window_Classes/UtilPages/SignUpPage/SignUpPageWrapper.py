from PyQt5.QtWidgets import QMessageBox

from Window_Classes.UtilPages.SignUpPage.SignUpPage import *

from kernel.QueryInfoSite.QueryInfo import Add_User, sql


class SignUpPage(QtWidgets.QWidget, Ui_SignUpPage):
    def __init__(self):
        super(SignUpPage, self).__init__()
        self.setupUi(self)

    def SignUp_Action(self) -> bool:
        UserName = self.UserNameLine.text()
        UserId = self.UserIdLine.text()
        Password = self.PassWordLine.text()
        Role = self.RoleCombo.currentText()
        if Role == 'Student':
            Role = 2
        else:
            Role = 1
        if UserName == '' or UserId == '' or Password == '':
            self.Echo_Empty_Input()
            return False
        try:
            Add_User(UserId, UserId, Role, Password)
        except sql.DatabaseError as e:
            print(repr(e))
            self.Echo_Empty_Input()
            return False
        msg = QMessageBox(self)
        msg.setText("Success!")
        msg.exec_()
        return True

    def Echo_Empty_Input(self):
        msg = QMessageBox(self)
        msg.setText("Check your input!")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
