from Window_Classes.SuperPage.CheckInfoPage.CheckInfoPage import *


class CheckInfoPage(QtWidgets.QWidget, Ui_CheckInfoPage):
    def __init__(self):
        super(CheckInfoPage, self).__init__()
        self.setupUi(self)
        # self.UserReaction_GetDir()

    def RefreshUserList(self):
        pass

    def RefreshBookList(self):
        pass

    def RefreshPageInfo(self):
        pass

    def SaveBookList(self):
        pass

    def SaveUserList(self):
        pass

    def UserReaction_GetDir(self, Filepath=None):
        directory = QtWidgets.QFileDialog. \
            getExistingDirectory(None, "Choose the folder", "C:/")  # 起始路径
        return directory

    @staticmethod
    def BindOptionsDict():
        return