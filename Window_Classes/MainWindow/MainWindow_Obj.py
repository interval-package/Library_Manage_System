import sys
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtGui
try:
    from Window_Classes.MainWindow.MainWindow_Login import Ui_MainWindow_Login
except ModuleNotFoundError:
    from MainWindow_Login import Ui_MainWindow_Login


class MainWindow(Ui_MainWindow_Login, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setIcon()
        pass

    def setIcon(self):
        # 由于路径问题需要重新设置一下icon的路径
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon_music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
