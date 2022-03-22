from Window_Classes.UtilPages.UserPage.UserPage import *


class UserPage(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(UserPage, self).__init__()
        self.setupUi(self)
