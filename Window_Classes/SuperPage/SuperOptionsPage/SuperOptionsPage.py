# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperOptionsPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SuperOptionsPage(object):
    def setupUi(self, SuperOptionsPage):
        SuperOptionsPage.setObjectName("SuperOptionsPage")
        SuperOptionsPage.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(SuperOptionsPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.CheckInfoButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.CheckInfoButton.setObjectName("CheckInfoButton")
        self.gridLayout.addWidget(self.CheckInfoButton, 2, 1, 2, 1)
        self.BookEditButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BookEditButton.setObjectName("BookEditButton")
        self.gridLayout.addWidget(self.BookEditButton, 4, 1, 1, 1)
        self.GoBackButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GoBackButton.setObjectName("GoBackButton")
        self.gridLayout.addWidget(self.GoBackButton, 2, 0, 2, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.UserEditButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.UserEditButton.setObjectName("UserEditButton")
        self.gridLayout.addWidget(self.UserEditButton, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)

        self.retranslateUi(SuperOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(SuperOptionsPage)

    def retranslateUi(self, SuperOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        SuperOptionsPage.setWindowTitle(_translate("SuperOptionsPage", "Form"))
        self.CheckInfoButton.setText(_translate("SuperOptionsPage", "Check info"))
        self.BookEditButton.setText(_translate("SuperOptionsPage", "Book Edit"))
        self.GoBackButton.setText(_translate("SuperOptionsPage", "Go Back"))
        self.label.setText(_translate("SuperOptionsPage", "This is the super user page, you can change any parameter of this manage system."))
        self.UserEditButton.setText(_translate("SuperOptionsPage", "User Edit"))
