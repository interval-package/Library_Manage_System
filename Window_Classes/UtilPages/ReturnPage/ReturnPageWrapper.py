from PyQt5 import QtWidgets
from Window_Classes.UtilPages.ReturnPage.ReturnPage import *


class ReturnPage(QtWidgets.QWidget,Ui_ReturnPage):
    def __init__(self):
        super(ReturnPage, self).__init__()
        self.setupUi(self)
