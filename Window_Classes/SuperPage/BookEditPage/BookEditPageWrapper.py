from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox

from Window_Classes.SuperPage.BookEditPage.BookEditPage import *
from kernel.QueryInfoSite.QueryInfo import Add_Book, FetchAllBooks, FetchAllBookType, Query_BookType
from kernel.QueryInfoSite.QueryInfo import Add_BookType, Update_BookInfo


class BookEditPage(QtWidgets.QWidget, Ui_BookEditPage):
    def __init__(self):
        super(BookEditPage, self).__init__()
        self.setupUi(self)
        self.RefreshViews()

        self.TypeDict = self.BindTypeDict()

        self.ChangeBookButton.clicked.connect(self.ChangeBookAction)
        self.AddBookButton.clicked.connect(self.AddBookAction)

        self.RefreshButton.clicked.connect(self.RefreshViews)

        self.AddTypeButton.clicked.connect(self.AddBookType)

        self.DeleteTypeButton.clicked.connect(lambda: self.Echo_Fail("have reference, could not delete"))

        self.DeleteButton.clicked.connect(lambda: self.Echo_Fail("have reference, could not delete"))

        pass

    def RefreshViews(self):
        self.SetUpBookView()
        self.SetUpBookTypeView()
        self.SetBookType()

        self.BookIdLine.clear()
        self.BookNameLine.clear()
        self.StockLine.clear()
        self.PriceLine.clear()

        self.BookIdLine.clear()
        self.BookNameLine.clear()

        pass

    def AddBookType(self):
        TypeId = self.TypeIdLine.text()
        TypeName = self.TypeNameLine.text()
        if TypeId != '' and TypeName != '':
            try:
                Add_BookType(TypeId, TypeName)
                pass
            except Exception as e:
                self.Echo_Empty_Input(repr(e))
            pass
        pass

    def ChangeBookAction(self):
        try:
            pack = dict()
            for i, title in zip(self.BookView.selectionModel().selectedIndexes(), self.BookHeader):
                pack[title] = i.data()
            Update_BookInfo(pack)
        except Exception as e:
            self.Echo_Fail(repr(e))
            return
        self.Echo_Success()
        pass

    def AddBookAction(self):
        Type = self.BookTypeComboBox.currentText()
        Name = self.BookNameLine.text()
        BookId = self.BookIdLine.text()
        Stock = self.StockLine.text()
        Price = self.PriceLine.text()
        if BookId is None or Name is None or Stock is None or Price is None:
            self.Echo_Empty_Input()
            pass
        else:
            try:
                Add_Book(BookId, Name, Stock, Price, self.TypeDict[Type])
                self.Echo_Success()
                self.RefreshViews()
            except Exception as e:
                self.Echo_Empty_Input(repr(e))
        pass

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

    def SetBookType(self):
        self.BookTypeComboBox.clear()
        self.TypeDict = self.BindTypeDict()
        for his in self.TypeDict.keys():
            self.BookTypeComboBox.addItem(his)

    BookHeader = ['id', 'name', 'stock', 'price', 'type id']

    def SetUpBookView(self):
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.BookHeader)
            for his in FetchAllBooks():
                row = []
                for detail in his:
                    row.append(QStandardItem(str(detail)))
                model.appendRow(row)
            self.BookView.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

    def SetUpBookTypeView(self):
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(['id', 'name'])
            for his in FetchAllBookType():
                row = []
                for detail in his:
                    row.append(QStandardItem(detail))
                model.appendRow(row)
            self.BookTypeView.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

    @staticmethod
    def BindTypeDict():
        names = Query_BookType()
        container = dict()
        for name in names:
            container[name[1]] = name[0]
        return container
