from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView

from Window_Classes.UtilPages.PayMoneyPage.PayMoneyPageWrapper import PayMoneyPage
from kernel.QueryInfoSite.QueryInfo import Query_UnReturned_Book, Modify_Return

from Window_Classes.UtilPages.ReturnPage.ReturnPage import *


class ReturnPage(QtWidgets.QWidget, Ui_ReturnPage):
    def __init__(self):
        super(ReturnPage, self).__init__()
        self.setupUi(self)
        self.User = None

        self.RefreshButton.clicked.connect(self.updatePage)
        self.ReturnButton.clicked.connect(self.ReturnBook)

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
        print(self.User.id)
        try:
            temp = Query_UnReturned_Book(self.User.id)
            if len(temp) == 0:
                print("find nothing")
            for his in temp:
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

    def ReturnBook(self):
        try:
            tar = []
            for i in [0, 2, 4]:
                tar.append(self.UnreturnedList.selectionModel().selectedRows(i)[0].data())
            PayMoneyPage(self, self.User, tar[1]).exec_()
            # print(self.UnreturnedList.item(index, 0).text())
        except Exception as e:
            print(repr(e))
        self.updatePage()
