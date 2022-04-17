from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem

from Window_Classes.UserPage.UserPage import *

from kernel.Quary_Info import Query_UserRank, Query_BookRank


class UserPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(UserPage, self).__init__()
        self.setupUi(self)
        self.User = None
        self.icon = QIcon()
        self.icon.addPixmap(QtGui.QPixmap("images/icon_music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.updateBookRankPage()
        self.updateUserRankPage()

    def SetUser(self, user):
        self.User = user
        self.updatePage()

        # to do 优化1 表格填满窗口
        # #水平方向标签拓展剩下的窗口部分，填满表格
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # #水平方向，表格大小拓展到适当的尺寸
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def updatePage(self) -> None:
        self.updateUserInfoList()
        self.updateRentedBookInfoList()
        pass

    def updateUserInfoList(self) -> None:
        model = QStandardItemModel()
        # name_item = QStandardItem(self.icon, self.User.name)
        model.appendRow(QStandardItem(self.icon, self.User.name))
        model.appendRow(QStandardItem(self.icon, self.User.id))
        self.UserInfoDispList.setModel(model)
        pass

    def updateRentedBookInfoList(self) -> None:
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['id', 'name', 'type', 'Rent Date', 'Return Date'])
            for his in self.User.RentHis:
                row = []
                for detail in his:
                    row.append(QStandardItem(detail))
                model.appendRow(row)
            self.RentedBookTable.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

    def updateBookRankPage(self) -> None:
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['BookId', 'BookName', 'times', 'Stock', 'Price', 'TypeName'])
            for his in Query_BookRank():
                row = []
                for detail in his:
                    if isinstance(detail, int):
                        row.append(QStandardItem(str(detail)))
                    else:
                        row.append(QStandardItem(detail))
                model.appendRow(row)
            self.BookRankTable.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

    def updateUserRankPage(self) -> None:
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['UserName', 'UserId', 'times'])
            for his in Query_UserRank():
                row = []
                for detail in his:
                    if isinstance(detail, int):
                        row.append(QStandardItem(str(detail)))
                    else:
                        row.append(QStandardItem(detail))
                model.appendRow(row)
            self.UserRankTable.setModel(model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.UserRankTable.horizontalHeader().setStretchLastSection(True)
        except Exception as e:
            print(repr(e))
        pass
