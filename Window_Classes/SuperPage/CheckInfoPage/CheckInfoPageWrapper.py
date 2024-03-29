from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox

from Window_Classes.SuperPage.CheckInfoPage.CheckInfoPage import *
from kernel.QueryInfoSite.QueryInfo import Query_Book, Query_BookType, Query_User
from kernel.SaveToExcel import *


class CheckInfoPage(QtWidgets.QWidget, Ui_CheckInfoPage):

    def __init__(self):
        super(CheckInfoPage, self).__init__()
        self.setupUi(self)

        self.BookComboDict = {
            'Ranked Book': [Query_BookRank, self.updateBookRankPage],
            'Query': [self.SaveQuery, self.Query]
        }

        self.UserComboDict = {
            'Ranked User': [Query_UserRank, self.updateUserRankPage],
        }

        self.SetBookType()

        self.SetTypeListDict()

        self.QueryBookButton.clicked.connect(self.Query)
        self.QueryUserButton.clicked.connect(self.Query_User)

        self.SaveBookButton.clicked.connect(self.SaveBookList)
        self.SaveUserButton.clicked.connect(self.SaveUserList)

        self.RefreshButton.clicked.connect(self.RefreshPageInfo)

    def SetTypeListDict(self):
        model = QStandardItemModel()
        for key in self.BookComboDict.keys():
            model.appendRow(QStandardItem(key))
        self.BookCombo.setModel(model)

        model = QStandardItemModel()
        for key in self.UserComboDict.keys():
            model.appendRow(QStandardItem(key))
        self.UserCombo.setModel(model)

    def RefreshPageInfo(self):
        self.RefreshBookList()
        self.RefreshUserList()
        pass

    def RefreshUserList(self):
        tar = self.UserCombo.currentText()
        method = self.UserComboDict[tar][1]
        method()
        pass

    def RefreshBookList(self):
        tar = self.BookCombo.currentText()
        method = self.BookComboDict[tar][1]
        method()
        pass

    BookHeader = ['BookId', 'BookName', 'times', 'Stock', 'Price', 'TypeName']

    def updateBookRankPage(self) -> None:
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.BookHeader)
            for his in Query_BookRank():
                row = []
                for detail in his:
                    if isinstance(detail, int):
                        row.append(QStandardItem(str(detail)))
                    else:
                        row.append(QStandardItem(detail))
                model.appendRow(row)
            self.BookView.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

    def MessageOfGettingPath(self, Filepath=None):
        print(Filepath)
        # 当窗口非继承QtWidgets.QDialog时，self需替换成 None
        FileDir = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件位置", Filepath)
        return FileDir

    def SetBookType(self):
        for his in Query_BookType():
            self.BookTypeCombo.addItem(his[1])

    def SaveQuery(self):
        Type = self.BookTypeCombo.currentText()
        Name = self.BookNameLine.text()

        try:
            his = Query_Book(Type, Name)
        except Exception as e:
            print(repr(e))
            his = []
        return his

    def Query(self):
        Type = self.BookTypeCombo.currentText()
        Name = self.BookNameLine.text()

        try:
            # self.BooksView.clear()
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['name', 'id:Select here'])
            for his in Query_Book(Type, Name):
                row = []
                for detail in his:
                    if isinstance(detail, int):
                        continue
                    else:
                        row.append(QStandardItem(detail))
                model.appendRow(row)
            self.BookView.setModel(model)
            self.BookView.horizontalHeader().setStretchLastSection(True)
        except Exception as e:
            print(repr(e))
        pass

    UserHeader = ['UserName', 'UserId', 'times']

    def Query_User(self):
        UserId = self.UserIdLine.text()
        UserName = self.UserNameLine.text()
        try:
            # self.BooksView.clear()
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['UserName', 'UserId', 'password'])
            for his in Query_User(UserId, UserName):
                row = []
                for detail in his:
                    if isinstance(detail, int):
                        continue
                    else:
                        row.append(QStandardItem(detail))
                model.appendRow(row)
            self.UserView.setModel(model)
            self.UserView.horizontalHeader().setStretchLastSection(True)
        except Exception as e:
            print(repr(e))
        pass



    def updateUserRankPage(self) -> None:
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.UserHeader)
            for his in Query_UserRank():
                row = []
                for detail in his:
                    if isinstance(detail, int):
                        row.append(QStandardItem(str(detail)))
                    else:
                        row.append(QStandardItem(detail))
                model.appendRow(row)
            self.UserView.setModel(model)
            # 水平方向标签拓展剩下的窗口部分，填满表格
            self.UserView.horizontalHeader().setStretchLastSection(True)
        except Exception as e:
            print(repr(e))
        pass

    def SaveBookList(self):
        tar = self.BookCombo.currentText()
        path = self.MessageOfGettingPath()
        SaveToExcel(path, 'Book', self.BookComboDict[tar][0])
        pass

    def SaveUserList(self):
        tar = self.UserCombo.currentText()
        path = self.MessageOfGettingPath()
        SaveToExcel(path, 'Book', self.UserComboDict[tar][0])
        pass

    def Echo_Fail(self, ms):
        msg = QMessageBox(self)
        msg.setWindowTitle("Error!")
        msg.setText(str(ms))
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
