# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 801, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(50, 50, 50, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.UserPageTabContainer = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.UserPageTabContainer.setObjectName("UserPageTabContainer")
        self.UserInfo = QtWidgets.QWidget()
        self.UserInfo.setEnabled(True)
        self.UserInfo.setStyleSheet("background-color: rgb(212, 238, 255);")
        self.UserInfo.setObjectName("UserInfo")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.UserInfo)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, -1, 681, 461))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(50, 50, 50, 50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(30, -1, 30, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.IDlable = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.IDlable.setObjectName("IDlable")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.IDlable)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.RoleLable = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.RoleLable.setObjectName("RoleLable")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.RoleLable)
        self.NameLable = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.NameLable.setObjectName("NameLable")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.NameLable)
        self.RentedBookTable = QtWidgets.QTableView(self.horizontalLayoutWidget)
        self.RentedBookTable.setStyleSheet("background-color: rgb(255, 253, 207);")
        self.RentedBookTable.setObjectName("RentedBookTable")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.RentedBookTable)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.UserInfoDispList = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.UserInfoDispList.setStyleSheet("background-color: rgb(255, 253, 207);")
        self.UserInfoDispList.setObjectName("UserInfoDispList")
        self.verticalLayout_3.addWidget(self.UserInfoDispList)
        self.RentButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.RentButton.setStyleSheet("background-color: rgb(100, 98, 96);")
        self.RentButton.setObjectName("RentButton")
        self.verticalLayout_3.addWidget(self.RentButton)
        self.ReturnButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ReturnButton.setStyleSheet("background-color: rgb(100, 98, 96);")
        self.ReturnButton.setObjectName("ReturnButton")
        self.verticalLayout_3.addWidget(self.ReturnButton)
        self.PayButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.PayButton.setObjectName("PayButton")
        self.verticalLayout_3.addWidget(self.PayButton)
        self.SuperButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SuperButton.setObjectName("SuperButton")
        self.verticalLayout_3.addWidget(self.SuperButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem1)
        self.UserPageTabContainer.addTab(self.UserInfo, "")
        self.BookRank = QtWidgets.QWidget()
        self.BookRank.setObjectName("BookRank")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.BookRank)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 701, 471))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(50, 50, 50, 50)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BookRankTable = QtWidgets.QTableView(self.gridLayoutWidget_2)
        self.BookRankTable.setObjectName("BookRankTable")
        self.gridLayout_2.addWidget(self.BookRankTable, 0, 0, 1, 1)
        self.UserPageTabContainer.addTab(self.BookRank, "")
        self.UserRank = QtWidgets.QWidget()
        self.UserRank.setObjectName("UserRank")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.UserRank)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 701, 471))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.UserRankTable = QtWidgets.QTableView(self.horizontalLayoutWidget_2)
        self.UserRankTable.setObjectName("UserRankTable")
        self.horizontalLayout_2.addWidget(self.UserRankTable)
        self.UserPageTabContainer.addTab(self.UserRank, "")
        self.gridLayout.addWidget(self.UserPageTabContainer, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.UserPageTabContainer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name:"))
        self.label_3.setText(_translate("Form", "Id:"))
        self.IDlable.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "Role"))
        self.RoleLable.setText(_translate("Form", "TextLabel"))
        self.NameLable.setText(_translate("Form", "TextLabel"))
        self.RentButton.setText(_translate("Form", "Rent Book"))
        self.ReturnButton.setText(_translate("Form", "Return Book"))
        self.PayButton.setText(_translate("Form", "Extend"))
        self.SuperButton.setText(_translate("Form", "Super"))
        self.UserPageTabContainer.setTabText(self.UserPageTabContainer.indexOf(self.UserInfo), _translate("Form", "User Info"))
        self.UserPageTabContainer.setTabText(self.UserPageTabContainer.indexOf(self.BookRank), _translate("Form", "Book Rank"))
        self.UserPageTabContainer.setTabText(self.UserPageTabContainer.indexOf(self.UserRank), _translate("Form", "User Rank"))
