# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookEditPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookEditPage(object):
    def setupUi(self, BookEditPage):
        BookEditPage.setObjectName("BookEditPage")
        BookEditPage.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(BookEditPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 2)
        self.tableView_2 = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout.addWidget(self.tableView_2, 1, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.gridLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 2)
        self.GoBackButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GoBackButton.setObjectName("GoBackButton")
        self.gridLayout.addWidget(self.GoBackButton, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 0, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 3, 1, 1)

        self.retranslateUi(BookEditPage)
        QtCore.QMetaObject.connectSlotsByName(BookEditPage)

    def retranslateUi(self, BookEditPage):
        _translate = QtCore.QCoreApplication.translate
        BookEditPage.setWindowTitle(_translate("BookEditPage", "Form"))
        self.pushButton_2.setText(_translate("BookEditPage", "PushButton"))
        self.pushButton.setText(_translate("BookEditPage", "PushButton"))
        self.label.setText(_translate("BookEditPage", "TextLabel"))
        self.GoBackButton.setText(_translate("BookEditPage", "Go Back"))
        self.label_2.setText(_translate("BookEditPage", "TextLabel"))
