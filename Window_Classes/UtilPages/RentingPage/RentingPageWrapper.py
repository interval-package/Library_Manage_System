from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QMessageBox

from Window_Classes.UtilPages.RentingPage.RentingPage import Ui_RentingPage
from PyQt5 import QtWidgets
from kernel.Quary_Info import Query_BookType, Query_Book, Add_RentHis, RentHis_Certification


class RentingPage(QtWidgets.QWidget, Ui_RentingPage):
    def __init__(self):
        super(RentingPage, self).__init__()
        self.setupUi(self)
        self.User = None

        self.SetBookType()

        self.QueryButton.clicked.connect(self.Query)

        self.RentButton.clicked.connect(self.Rent)

        self.BooksView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setUser(self, User):
        self.User = User
        self.Query()

    def SetBookType(self):
        for his in Query_BookType():
            for i in his:
                self.BookTypeCombo.addItem(i)

    def updateRentedBookInfoList(self) -> None:
        self.User.updateRentHis()
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['id', 'name', 'type', 'Rent Date', 'Return Date'])
            for his in self.User.RentHis:
                row = []
                for detail in his:
                    row.append(QStandardItem(detail))
                model.appendRow(row)
            self.RentedBookView.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

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
            self.BooksView.setModel(model)
        except Exception as e:
            print(repr(e))
        pass
        self.updateRentedBookInfoList()

    def Rent(self):
        flag = True
        try:
            BookId = self.BooksView.selectionModel().selectedIndexes()[-1].data()
            UserId = self.User.id
            if RentHis_Certification(UserId):
                print(UserId, BookId)
                Add_RentHis(UserId, BookId)
            else:
                self.Echo_Fail_To_Rent()
                return
        except AttributeError as e:
            print("un inited error", repr(e))
            flag = False
        except IndexError as e:
            print("select Wrong", repr(e))
            flag = False
        except Exception as e:
            print(repr(e))
            flag = False
        self.Echo_Success_Not(flag)
        # refresh
        self.Query()

    def Echo_Success_Not(self, flag):
        msg = QMessageBox(self)
        if flag:
            msg.setText("success")
        else:
            msg.setText("Check your input!")
            msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        pass

    def Echo_Fail_To_Rent(self):
        msg = QMessageBox(self)
        msg.setText("you could no more rent, please return books first.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        pass
