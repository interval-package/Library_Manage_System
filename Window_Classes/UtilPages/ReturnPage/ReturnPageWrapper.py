from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView

from kernel.Quary_Info import Query_UnReturned_Book

from Window_Classes.UtilPages.ReturnPage.ReturnPage import *


class ReturnPage(QtWidgets.QWidget, Ui_ReturnPage):
    def __init__(self):
        super(ReturnPage, self).__init__()
        self.setupUi(self)
        self.User = None

        self.RefreshButton.clicked.connect(self.updatePage)

        self.UnreturnedList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def SetUser(self, User):
        self.User = User
        self.updatePage()

    def updatePage(self) -> None:
        self.updateRentedBookInfoList()
        pass

    def updateRentedBookInfoList(self) -> None:
        self.User.updateRentHis()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['id', 'name', 'Book Id', 'Book name', 'RentDay'])
        try:
            for his in Query_UnReturned_Book(self.User.id):
                row = []
                for detail in his:
                    if isinstance(detail, int):
                        continue
                    else:
                        row.append(QStandardItem(detail))
                model.appendRow(row)
        except AttributeError as e:
            print("init error", repr(e))
        except Exception as e:
            print(repr(e))
        self.UnreturnedList.setModel(model)
        pass
