from Window_Classes.UtilPages.RentingPage.RentingPage import Ui_RentingPage
from PyQt5 import QtWidgets


class RentingPage(QtWidgets.QWidget, Ui_RentingPage):
    def __init__(self):
        super(RentingPage, self).__init__()
        self.setupUi(self)

