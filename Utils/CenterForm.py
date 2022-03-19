from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()

        self.setWindowTitle("centering!")
        pass

    def Center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        left = (screen.width()-size.width())/2
        top = (screen.height()-size.height())/2
        self.move(left,top)
        pass
