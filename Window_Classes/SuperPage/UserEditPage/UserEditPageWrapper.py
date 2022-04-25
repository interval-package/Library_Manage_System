from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox

from Window_Classes.SuperPage.UserEditPage.UserEditPage import *
from kernel.QueryInfoSite.QueryInfo import FetchAllRoleTypes, FetchAllUser, Add_User
from kernel.QueryInfoSite.QueryInfo import Update_UserInfo


class UserEditPage(QtWidgets.QWidget, Ui_UserEditPage):
    UserInfoHeader = ['id', 'name', 'role', 'password']

    def __init__(self):
        super(UserEditPage, self).__init__()
        self.setupUi(self)
        self.RefreshViews()

        self.RoleDict = dict()

        for role in FetchAllRoleTypes():
            self.RoleDict[role[1]] = role[0]

        self.SetBookType()

        self.ChangeUserButton.clicked.connect(self.ChangeUserInfoAction)
        self.RefreshButton.clicked.connect(self.RefreshViews)
        self.AddUserButton.clicked.connect(self.AddUserAction)

        pass

    def RefreshViews(self):
        self.UpdateRoleView()
        self.UpdateUserView()

        self.UserIdLine.clear()
        self.UserNameLine.clear()
        self.PassWordLine.clear()

        self.SuperCommandEdit.clear()

        pass

    def UpdateRoleView(self):
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.UserInfoHeader)
            for his in FetchAllUser():
                row = []
                for detail in his:
                    row.append(QStandardItem(str(detail)))
                model.appendRow(row)
            self.UserView.setModel(model)
        except Exception as e:
            self.Echo_Fail(repr(e))
        pass

    def ChangeUserInfoAction(self):
        try:
            pack = dict()
            for i, title in zip(self.UserView.selectionModel().selectedIndexes(), self.UserInfoHeader):
                pack[title] = i.data()
            Update_UserInfo(pack)
        except Exception as e:
            self.Echo_Fail(repr(e))
            return
        self.Echo_Success()
        pass

    def AddUserAction(self):
        UserName = self.UserNameLine.text()
        UserId = self.UserIdLine.text()
        Password = self.PassWordLine.text()
        Role = self.RoleOfTypeCombo.currentText()
        Role = self.RoleDict[Role]
        if UserName == '' or UserId == '' or Password == '':
            self.Echo_Empty_Input()
        else:
            try:
                Add_User(UserId, UserId, Role, Password)
                self.Echo_Success()
                self.RefreshViews()
            except Exception as e:
                self.Echo_Empty_Input(repr(e))
        pass

    def UpdateUserView(self):
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['id', 'name', 'duration', 'times'])
            for his in FetchAllRoleTypes():
                row = []
                for detail in his:
                    row.append(QStandardItem(str(detail)))
                model.appendRow(row)
            self.RoleView.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

    def SetBookType(self):
        for his in FetchAllRoleTypes():
            self.RoleOfTypeCombo.addItem(his[1])
            self.RoleOfUserCombo.addItem(his[1])

    def Echo_Empty_Input(self, ms=None):
        msg = QMessageBox(self)
        msg.setWindowTitle("Error!")
        if ms is not None:
            msg.setText(str(ms))
        else:
            msg.setText("Wrong Input")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        pass

    def Echo_Fail(self, ms):
        msg = QMessageBox(self)
        msg.setWindowTitle("Error!")
        msg.setText(str(ms))
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def Echo_Success(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("success")
        msg.setText("success")
        msg.exec_()
        pass
