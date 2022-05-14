from PyQt5.QtWidgets import QStackedWidget

from Window_Classes.SuperPage.SuperPage import *

from Window_Classes.SuperPage.CheckInfoPage.CheckInfoPageWrapper import CheckInfoPage

from Window_Classes.SuperPage.SuperOptionsPage.SuperOptionsPageWrapper import *

from Window_Classes.SuperPage.UserEditPage.UserEditPageWrapper import *

from Window_Classes.SuperPage.BookEditPage.BookEditPageWrapper import *


class SuperPage(QtWidgets.QWidget, Ui_SuperPage):
    def __init__(self):
        super(SuperPage, self).__init__()
        self.setupUi(self)

        # 设置页面
        self.stackWidget = QStackedWidget(self)
        self.stackWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))

        # 设置选项界面，0
        self.SuperOptionsPage = SuperOptionsPage()
        self.stackWidget.addWidget(self.SuperOptionsPage)
        self.SuperOptionsPage.UserEditButton.clicked.connect(lambda: self.switchPage(1))
        self.SuperOptionsPage.BookEditButton.clicked.connect(lambda: self.switchPage(2))
        self.SuperOptionsPage.CheckInfoButton.clicked.connect(lambda: self.switchPage(3))

        # 设置管理用户界面，1
        self.UserEditPage = UserEditPage()
        self.stackWidget.addWidget(self.UserEditPage)
        self.UserEditPage.GoBackButton.clicked.connect(lambda: self.switchPage(0))

        # 设置管理书籍界面，2
        self.BookEditPage = BookEditPage()
        self.stackWidget.addWidget(self.BookEditPage)
        self.BookEditPage.GoBackButton.clicked.connect(lambda: self.switchPage(0))

        # 设置导出数据界面，3
        self.CheckInfoPage = CheckInfoPage()
        self.stackWidget.addWidget(self.CheckInfoPage)
        self.CheckInfoPage.GoBackButton.clicked.connect(lambda: self.switchPage(0))

        # 将页面置放于窗体中间
        # self.setCentralWidget(self.stackWidget)
        self.switchPage(0)

        pass

    def switchPage(self, index):
        self.stackWidget.setCurrentIndex(index)
