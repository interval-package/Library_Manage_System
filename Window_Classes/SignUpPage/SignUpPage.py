# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUpPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpPage(object):
    def setupUi(self, SignUpPage):
        SignUpPage.setObjectName("SignUpPage")
        SignUpPage.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(SignUpPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.UserIdLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UserIdLine.setObjectName("UserIdLine")
        self.gridLayout.addWidget(self.UserIdLine, 1, 1, 1, 1)
        self.SignUpButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.SignUpButton.setObjectName("SignUpButton")
        self.gridLayout.addWidget(self.SignUpButton, 4, 0, 1, 2)
        self.UserNameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.UserNameLine.setObjectName("UserNameLine")
        self.gridLayout.addWidget(self.UserNameLine, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)
        self.PassWordLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PassWordLine.setObjectName("PassWordLine")
        self.gridLayout.addWidget(self.PassWordLine, 2, 1, 1, 1)
        self.GoBackButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.GoBackButton.setObjectName("GoBackButton")
        self.gridLayout.addWidget(self.GoBackButton, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.RoleCombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.RoleCombo.setObjectName("RoleCombo")
        self.RoleCombo.addItem("")
        self.RoleCombo.addItem("")
        self.gridLayout.addWidget(self.RoleCombo, 3, 1, 1, 1)
        self.label_4.setBuddy(self.RoleCombo)
        self.label.setBuddy(self.UserNameLine)
        self.label_3.setBuddy(self.PassWordLine)
        self.label_2.setBuddy(self.UserIdLine)

        self.retranslateUi(SignUpPage)
        QtCore.QMetaObject.connectSlotsByName(SignUpPage)

    def retranslateUi(self, SignUpPage):
        _translate = QtCore.QCoreApplication.translate
        SignUpPage.setWindowTitle(_translate("SignUpPage", "Form"))
        self.label_4.setText(_translate("SignUpPage", "Role"))
        self.SignUpButton.setText(_translate("SignUpPage", "Sign up!"))
        self.label.setText(_translate("SignUpPage", "User Name"))
        self.pushButton_2.setText(_translate("SignUpPage", "Clear"))
        self.GoBackButton.setText(_translate("SignUpPage", "Go Back"))
        self.label_3.setText(_translate("SignUpPage", "Password"))
        self.label_2.setText(_translate("SignUpPage", "User ID"))
        self.RoleCombo.setItemText(0, _translate("SignUpPage", "Student"))
        self.RoleCombo.setItemText(1, _translate("SignUpPage", "Teacher"))
