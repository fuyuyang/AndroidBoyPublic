# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/weizlian/Desktop/MyPrj/github-repos/Python/AndroidBoyPublic/src/Layout/viewOutlookDetector.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(939, 486)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.layoutDetector = QtWidgets.QHBoxLayout()
        self.layoutDetector.setObjectName("layoutDetector")
        self.layoutOutlook = QtWidgets.QVBoxLayout()
        self.layoutOutlook.setContentsMargins(0, 0, 0, 0)
        self.layoutOutlook.setObjectName("layoutOutlook")
        self.layoutFilter = QtWidgets.QHBoxLayout()
        self.layoutFilter.setContentsMargins(0, 0, 0, 0)
        self.layoutFilter.setObjectName("layoutFilter")
        self.ckFilterDate = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ckFilterDate.sizePolicy().hasHeightForWidth())
        self.ckFilterDate.setSizePolicy(sizePolicy)
        self.ckFilterDate.setMinimumSize(QtCore.QSize(90, 24))
        self.ckFilterDate.setMaximumSize(QtCore.QSize(90, 24))
        self.ckFilterDate.setObjectName("ckFilterDate")
        self.layoutFilter.addWidget(self.ckFilterDate)
        spacerItem = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem)
        self.lbStartDate = QtWidgets.QLabel(Form)
        self.lbStartDate.setObjectName("lbStartDate")
        self.layoutFilter.addWidget(self.lbStartDate)
        self.dateStart = QtWidgets.QDateEdit(Form)
        self.dateStart.setObjectName("dateStart")
        self.layoutFilter.addWidget(self.dateStart)
        self.lbToDate = QtWidgets.QLabel(Form)
        self.lbToDate.setObjectName("lbToDate")
        self.layoutFilter.addWidget(self.lbToDate)
        self.dateEnd = QtWidgets.QDateEdit(Form)
        self.dateEnd.setObjectName("dateEnd")
        self.layoutFilter.addWidget(self.dateEnd)
        spacerItem1 = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem1)
        self.btQueryMails = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btQueryMails.sizePolicy().hasHeightForWidth())
        self.btQueryMails.setSizePolicy(sizePolicy)
        self.btQueryMails.setMinimumSize(QtCore.QSize(28, 24))
        self.btQueryMails.setMaximumSize(QtCore.QSize(28, 24))
        self.btQueryMails.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/bt_find.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btQueryMails.setIcon(icon)
        self.btQueryMails.setIconSize(QtCore.QSize(16, 16))
        self.btQueryMails.setObjectName("btQueryMails")
        self.layoutFilter.addWidget(self.btQueryMails)
        self.lbLoading = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbLoading.sizePolicy().hasHeightForWidth())
        self.lbLoading.setSizePolicy(sizePolicy)
        self.lbLoading.setMinimumSize(QtCore.QSize(28, 24))
        self.lbLoading.setMaximumSize(QtCore.QSize(28, 24))
        self.lbLoading.setText("")
        self.lbLoading.setObjectName("lbLoading")
        self.layoutFilter.addWidget(self.lbLoading)
        spacerItem2 = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem2)
        self.btExportExcel = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btExportExcel.sizePolicy().hasHeightForWidth())
        self.btExportExcel.setSizePolicy(sizePolicy)
        self.btExportExcel.setMinimumSize(QtCore.QSize(28, 24))
        self.btExportExcel.setMaximumSize(QtCore.QSize(28, 24))
        self.btExportExcel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/excel.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btExportExcel.setIcon(icon1)
        self.btExportExcel.setObjectName("btExportExcel")
        self.layoutFilter.addWidget(self.btExportExcel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem3)
        self.layoutOutlook.addLayout(self.layoutFilter)
        self.treeOutlook = QtWidgets.QTreeWidget(Form)
        self.treeOutlook.setMinimumSize(QtCore.QSize(800, 0))
        self.treeOutlook.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeOutlook.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeOutlook.setColumnCount(1)
        self.treeOutlook.setObjectName("treeOutlook")
        self.treeOutlook.headerItem().setText(0, "1")
        self.layoutOutlook.addWidget(self.treeOutlook)
        self.layoutProg1 = QtWidgets.QHBoxLayout()
        self.layoutProg1.setContentsMargins(0, 0, 0, 0)
        self.layoutProg1.setObjectName("layoutProg1")
        self.lbProg1 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbProg1.sizePolicy().hasHeightForWidth())
        self.lbProg1.setSizePolicy(sizePolicy)
        self.lbProg1.setMinimumSize(QtCore.QSize(80, 25))
        self.lbProg1.setMaximumSize(QtCore.QSize(80, 25))
        self.lbProg1.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lbProg1.setObjectName("lbProg1")
        self.layoutProg1.addWidget(self.lbProg1)
        self.prog1 = QtWidgets.QProgressBar(Form)
        self.prog1.setProperty("value", 24)
        self.prog1.setObjectName("prog1")
        self.layoutProg1.addWidget(self.prog1)
        self.layoutOutlook.addLayout(self.layoutProg1)
        self.layoutProg2 = QtWidgets.QHBoxLayout()
        self.layoutProg2.setContentsMargins(0, 0, 0, 0)
        self.layoutProg2.setObjectName("layoutProg2")
        self.lbProg2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbProg2.sizePolicy().hasHeightForWidth())
        self.lbProg2.setSizePolicy(sizePolicy)
        self.lbProg2.setMinimumSize(QtCore.QSize(80, 25))
        self.lbProg2.setMaximumSize(QtCore.QSize(80, 25))
        self.lbProg2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lbProg2.setObjectName("lbProg2")
        self.layoutProg2.addWidget(self.lbProg2)
        self.prog2 = QtWidgets.QProgressBar(Form)
        self.prog2.setProperty("value", 24)
        self.prog2.setObjectName("prog2")
        self.layoutProg2.addWidget(self.prog2)
        self.layoutOutlook.addLayout(self.layoutProg2)
        self.layoutDetector.addLayout(self.layoutOutlook)
        self.gridLayout.addLayout(self.layoutDetector, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ckFilterDate.setText(_translate("Form", "Filter Date"))
        self.lbStartDate.setText(_translate("Form", "From "))
        self.lbToDate.setText(_translate("Form", " to "))
        self.lbProg1.setText(_translate("Form", "lbProg1"))
        self.lbProg2.setText(_translate("Form", "lbProg2"))
import AndroidBoy_rc
