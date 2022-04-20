from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Window_Classes.SuperPage.CheckInfoPage.CheckInfoPage import *
from kernel.Quary_Info import FetchAllBooks


class CheckInfoPage(QtWidgets.QWidget, Ui_CheckInfoPage):
    def __init__(self):
        super(CheckInfoPage, self).__init__()
        self.setupUi(self)

        self.QueryBookButton.clicked.connect(self.Query_Book)
        self.QueryUserButton.clicked.connect(self.Query_User)

        self.SaveBookButton.clicked.connect(self.SaveBookList)
        self.SaveUserButton.clicked.connect(self.SaveUserList)

    def RefreshPageInfo(self):
        self.RefreshBookList()
        self.RefreshUserList()
        self.BookView.clear()
        pass

    def RefreshUserList(self):
        pass

    def RefreshBookList(self):
        try:
            model = QStandardItemModel()
            # model.setHorizontalHeaderLabels([])
            for his in FetchAllBooks():
                row = []
                for detail in his:
                    row.append(QStandardItem(detail))
                model.appendRow(row)
            self.BookView.setModel(model)
        except Exception as e:
            print(repr(e))
        pass

    def Query_Book(self):
        pass

    def Query_User(self):
        pass

    def UserReaction_GetDir(self, Filepath=None):
        directory = QtWidgets.QFileDialog. \
            getExistingDirectory(None, "Choose the folder", "C:/")  # 起始路径
        return directory

    def SaveBookList(self):
        pass

    def SaveUserList(self):
        pass

    @staticmethod
    def BindOptionsDict():
        return
