# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/weizlian/Desktop/MyPrj/github-repos/Python/AndroidBoyPublic/src/Layout/widgetTracerList.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(690, 511)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.findLayout = QtWidgets.QHBoxLayout()
        self.findLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.findLayout.setContentsMargins(-1, 0, -1, 2)
        self.findLayout.setSpacing(6)
        self.findLayout.setObjectName("findLayout")
        self.tbFindContent = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbFindContent.sizePolicy().hasHeightForWidth())
        self.tbFindContent.setSizePolicy(sizePolicy)
        self.tbFindContent.setMinimumSize(QtCore.QSize(280, 24))
        self.tbFindContent.setMaximumSize(QtCore.QSize(280, 24))
        self.tbFindContent.setObjectName("tbFindContent")
        self.findLayout.addWidget(self.tbFindContent)
        self.ckRegular = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ckRegular.sizePolicy().hasHeightForWidth())
        self.ckRegular.setSizePolicy(sizePolicy)
        self.ckRegular.setMinimumSize(QtCore.QSize(0, 24))
        self.ckRegular.setMaximumSize(QtCore.QSize(16777215, 24))
        self.ckRegular.setObjectName("ckRegular")
        self.findLayout.addWidget(self.ckRegular)
        self.ckCase = QtWidgets.QCheckBox(Form)
        self.ckCase.setMinimumSize(QtCore.QSize(0, 24))
        self.ckCase.setMaximumSize(QtCore.QSize(16777215, 24))
        self.ckCase.setObjectName("ckCase")
        self.findLayout.addWidget(self.ckCase)
        self.ckWords = QtWidgets.QCheckBox(Form)
        self.ckWords.setMinimumSize(QtCore.QSize(0, 24))
        self.ckWords.setMaximumSize(QtCore.QSize(16777215, 24))
        self.ckWords.setObjectName("ckWords")
        self.findLayout.addWidget(self.ckWords)
        self.btFindNext = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btFindNext.sizePolicy().hasHeightForWidth())
        self.btFindNext.setSizePolicy(sizePolicy)
        self.btFindNext.setMinimumSize(QtCore.QSize(28, 24))
        self.btFindNext.setMaximumSize(QtCore.QSize(28, 24))
        self.btFindNext.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/bt_next_marked.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btFindNext.setIcon(icon)
        self.btFindNext.setObjectName("btFindNext")
        self.findLayout.addWidget(self.btFindNext)
        self.btFindPrev = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btFindPrev.sizePolicy().hasHeightForWidth())
        self.btFindPrev.setSizePolicy(sizePolicy)
        self.btFindPrev.setMinimumSize(QtCore.QSize(28, 24))
        self.btFindPrev.setMaximumSize(QtCore.QSize(28, 24))
        self.btFindPrev.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/bt_prev_marked.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btFindPrev.setIcon(icon1)
        self.btFindPrev.setObjectName("btFindPrev")
        self.findLayout.addWidget(self.btFindPrev)
        self.btHideFindToolbar = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btHideFindToolbar.sizePolicy().hasHeightForWidth())
        self.btHideFindToolbar.setSizePolicy(sizePolicy)
        self.btHideFindToolbar.setMinimumSize(QtCore.QSize(28, 24))
        self.btHideFindToolbar.setMaximumSize(QtCore.QSize(28, 24))
        self.btHideFindToolbar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/bt_close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btHideFindToolbar.setIcon(icon2)
        self.btHideFindToolbar.setObjectName("btHideFindToolbar")
        self.findLayout.addWidget(self.btHideFindToolbar)
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.findLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.findLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listTrace = QtWidgets.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.listTrace.setFont(font)
        self.listTrace.setFrameShape(QtWidgets.QFrame.Box)
        self.listTrace.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listTrace.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.listTrace.setObjectName("listTrace")
        self.horizontalLayout.addWidget(self.listTrace)
        self.listImportant = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listImportant.sizePolicy().hasHeightForWidth())
        self.listImportant.setSizePolicy(sizePolicy)
        self.listImportant.setMinimumSize(QtCore.QSize(150, 0))
        self.listImportant.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listImportant.setObjectName("listImportant")
        self.horizontalLayout.addWidget(self.listImportant)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbStatus = QtWidgets.QLabel(Form)
        self.lbStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbStatus.setObjectName("lbStatus")
        self.verticalLayout.addWidget(self.lbStatus)
        self.pbLoading = QtWidgets.QProgressBar(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbLoading.sizePolicy().hasHeightForWidth())
        self.pbLoading.setSizePolicy(sizePolicy)
        self.pbLoading.setMinimumSize(QtCore.QSize(0, 20))
        self.pbLoading.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pbLoading.setProperty("value", 0)
        self.pbLoading.setObjectName("pbLoading")
        self.verticalLayout.addWidget(self.pbLoading)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ckRegular.setText(_translate("Form", "Regular"))
        self.ckCase.setText(_translate("Form", "Case"))
        self.ckWords.setText(_translate("Form", "Words"))
        self.btFindNext.setToolTip(_translate("Form", "Find next"))
        self.btFindPrev.setToolTip(_translate("Form", "Find prev"))
        self.btHideFindToolbar.setToolTip(_translate("Form", "Hide find toolbar"))
        self.lbStatus.setText(_translate("Form", "0/0"))
import AndroidBoy_rc
