from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QMessageBox

from Window_Classes.UtilPages.RentingPage.RentingPage import Ui_RentingPage
from PyQt5 import QtWidgets
from kernel.QueryInfoSite.QueryInfo import Query_BookType, Query_Book, Add_RentHis

from kernel.QueryInfoSite.ExceptionClasses_Query import RentRefuse

from Window_Classes.UtilPages.PayMoneyPage.PayMoneyPageWrapper import PayMoneyPage


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
            self.BookTypeCombo.addItem(his[1])

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
        try:
            BookId = self.BooksView.selectionModel().selectedIndexes()[-1].data()
            UserId = self.User.id
            Add_RentHis(UserId, BookId)
        except AttributeError as e:
            self.Echo_Empty_Input("un inited error" + repr(e))
            print("un inited error", repr(e))
        except RentRefuse as e:
            self.Echo_Empty_Input(repr(e) + " you have rent too many books")
        except IndexError as e:
            self.Echo_Empty_Input("select Wrong" + repr(e))
            print("select Wrong", repr(e))
        except Exception as e:
            self.Echo_Empty_Input("unknown " + repr(e))
            print(repr(e))
        # refresh
        self.Query()

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
