# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/weizlian/Desktop/MyPrj/github-repos/Python/AndroidBoyPublic/src/Layout/viewPicture.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 478)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saPicture = QtWidgets.QScrollArea(Form)
        self.saPicture.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.saPicture.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.saPicture.setWidgetResizable(True)
        self.saPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.saPicture.setObjectName("saPicture")
        self.lbPicture = QtWidgets.QLabel()
        self.lbPicture.setGeometry(QtCore.QRect(0, 0, 549, 474))
        self.lbPicture.setText("")
        self.lbPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.lbPicture.setObjectName("lbPicture")
        self.saPicture.setWidget(self.lbPicture)
        self.horizontalLayout.addWidget(self.saPicture)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
