from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Window_Classes.UtilPages.PayMoneyPage.PayMoneyPage import *
from kernel.QueryInfoSite.QueryInfo_sqlite import Query_BookRank, Query_Price_Remain, Add_RentHis, Modify_Return


class PayMoneyPage(Ui_PayMoneyPage, QtWidgets.QDialog):
    def __init__(self, parent, user, BookId=None, RentDate=None):
        super(PayMoneyPage, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Pay money for books")

        self.NopeButton.clicked.connect(self.done)
        self.PayButon.clicked.connect(self.Return)

        self.user = user
        self.BookId = BookId
        self.RentDate = RentDate
        self.Res = Query_Price_Remain(self.user.id, self.BookId, RentDate)

        self.UpdatePricePage()

    def UpdatePricePage(self):
        self.InitPriceView()
        self.InitLabel()
        pass

    Header = ['Book Name', 'Price', 'RentDate']

    def InitPriceView(self):
        try:
            model = QStandardItemModel()
            model.setHorizontalHeaderLabels(self.Header)
            for his in self.Res:
                row = []
                for detail in his[2:-1]:
                    if isinstance(detail, int):
                        row.append(QStandardItem(str(detail)))
                    else:
                        row.append(QStandardItem(detail))
                model.appendRow(row)
            self.PriceView.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

    def InitLabel(self):
        self.InfoLabel.setText("you need to pay {}".format(self.CalcPrice()))
        pass

    def CalcPrice(self):
        tarPrice = 0
        if self.Res is not None:
            for i in self.Res:
                tarPrice += int(i[3])
        return tarPrice

    def Return(self):
        if self.BookId is not None:
            Modify_Return([self.user.id, self.BookId, self.RentDate])
        else:
            self.done(1)
