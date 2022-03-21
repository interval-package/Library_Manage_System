import sys

from PyQt5 import QtCore, QtWidgets


class Disco(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.artista = QtWidgets.QLineEdit()
        self.titolo = QtWidgets.QLineEdit()
        layout = QtWidgets.QFormLayout(self)
        layout.addRow('Artista', self.artista)
        layout.addRow('Titolo', self.titolo)

    def setData(self, data):
        self.artista.setText(data.get('artista', ''))
        self.titolo.setText(data.get('titolo', ''))

    def getData(self):
        return {'artista': self.artista.text(), 'titolo': self.titolo.text()}


class Canzoni(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        self.table = QtWidgets.QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(('Titolo', 'Durata'))
        layout.addWidget(self.table)
        self.addButton = QtWidgets.QPushButton('Aggiungi')
        layout.addWidget(self.addButton)
        self.addButton.clicked.connect(lambda:
            self.table.insertRow(self.table.rowCount()))

    def setData(self, data):
        self.table.clearContents()
        canzoni = data.get('canzoni', [])
        self.table.setRowCount(len(canzoni))
        for row, (titolo, durata) in enumerate(canzoni):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(titolo))
            durataItem = QtWidgets.QTableWidgetItem()
            durataItem.setData(QtCore.Qt.DisplayRole, int(durata))
            self.table.setItem(row, 1, durataItem)

    def getData(self):
        canzoni = []
        for row in range(self.table.rowCount()):
            canzoni.append([
                self.table.item(row, 0).text(),
                self.table.item(row, 1).data(QtCore.Qt.DisplayRole),
            ])
        return {'canzoni': canzoni}


class Strumenti(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        self.table = QtWidgets.QTableWidget(0, 2)
        layout.addWidget(self.table)
        self.table.setHorizontalHeaderLabels(('Artista', 'Strumenti'))
        self.table.verticalHeader().hide()
        self.addButton = QtWidgets.QPushButton('Aggiungi')
        layout.addWidget(self.addButton)
        self.addButton.clicked.connect(lambda:
            self.table.insertRow(self.table.rowCount()))

    def setData(self, data):
        self.table.clearContents()
        strumenti = data.get('strumenti', [])
        self.table.setRowCount(len(strumenti))
        for row, (artista, strumento) in enumerate(strumenti):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(artista))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(strumento))

    def getData(self):
        strumenti = []
        for row in range(self.table.rowCount()):
            strumenti.append([
                self.table.item(row, 0).text(),
                self.table.item(row, 1).text(),
            ])
        return {'strumenti': strumenti}


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stackWidget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stackWidget)

        self.disco = Disco()
        self.stackWidget.addWidget(self.disco)

        self.canzoni = Canzoni()
        self.stackWidget.addWidget(self.canzoni)

        self.strumenti = Strumenti()
        self.stackWidget.addWidget(self.strumenti)

        self.pages = self.disco, self.canzoni, self.strumenti

        self.loadAction = self.menuBar().addAction('Load')
        self.loadAction.triggered.connect(self.loadData)
        self.saveAction = self.menuBar().addAction('Save')
        self.saveAction.triggered.connect(self.saveData)

        for i, actionName in enumerate(('Disco', 'Canzoni', 'Strumenti')):
            action = self.menuBar().addAction(actionName)
            action.setData(i)

        self.menuBar().triggered.connect(self.switchPageAction)

        self.setStyleSheet('''
            Disco {
                background: red;
            }
            Canzoni {
                background: green;
            }
            Strumenti {
                background: yellow;
            }
        ''')
        self.switchPage(0)

    def loadData(self):
        data = {
            'artista': 'Elio e le Storie Tese',
            'titolo': 'Elio Samaga Hukapan Kariyana Turu',
            'canzoni': [
                ['John Holmes', 206],
                ['Nubi di ieri sul nostro domani odierno', 253],
            ],
            'strumenti': [
                ['Elio', 'Voci'],
                ['Rocco', 'Tastiere'],
            ]
        }
        for page in self.pages:
            page.setData(data)

    def saveData(self):
        data = {}
        for page in self.pages:
            data.update(page.getData())
        print(data)

    def switchPageAction(self, action):
        index = action.data()
        if index is not None:
            self.switchPage(index)

    def switchPage(self, index):
        self.stackWidget.setCurrentIndex(index)
        for action in self.menuBar().actions():
            action.setEnabled(action.data() != index)

if __name__ == '__main__':
    # 初始化软件，这是必要操作
    app = QtWidgets.QApplication(sys.argv)

    # 创建窗体对象
    win = MainWindow()
    win.show()

    # 结束所有逻辑，之前所有循环的逻辑结束
    sys.exit(app.exec_())