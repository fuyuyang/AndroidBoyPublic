# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewWBXTraceFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(590, 133)
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
        self.layoutView = QtWidgets.QVBoxLayout()
        self.layoutView.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layoutView.setSpacing(0)
        self.layoutView.setObjectName("layoutView")
        self.layoutFilter = QtWidgets.QHBoxLayout()
        self.layoutFilter.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.layoutFilter.setContentsMargins(-1, 2, -1, 2)
        self.layoutFilter.setSpacing(0)
        self.layoutFilter.setObjectName("layoutFilter")
        self.cbLogLevel = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbLogLevel.sizePolicy().hasHeightForWidth())
        self.cbLogLevel.setSizePolicy(sizePolicy)
        self.cbLogLevel.setMinimumSize(QtCore.QSize(100, 24))
        self.cbLogLevel.setObjectName("cbLogLevel")
        self.layoutFilter.addWidget(self.cbLogLevel)
        spacerItem = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem)
        self.editFilter = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editFilter.sizePolicy().hasHeightForWidth())
        self.editFilter.setSizePolicy(sizePolicy)
        self.editFilter.setMinimumSize(QtCore.QSize(200, 24))
        self.editFilter.setObjectName("editFilter")
        self.layoutFilter.addWidget(self.editFilter)
        spacerItem1 = QtWidgets.QSpacerItem(3, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem1)
        self.btFilter = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btFilter.sizePolicy().hasHeightForWidth())
        self.btFilter.setSizePolicy(sizePolicy)
        self.btFilter.setMinimumSize(QtCore.QSize(28, 24))
        self.btFilter.setMaximumSize(QtCore.QSize(28, 24))
        self.btFilter.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/bt_fliter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btFilter.setIcon(icon)
        self.btFilter.setObjectName("btFilter")
        self.layoutFilter.addWidget(self.btFilter)
        self.ckUsingRegx = QtWidgets.QCheckBox(Form)
        self.ckUsingRegx.setObjectName("ckUsingRegx")
        self.layoutFilter.addWidget(self.ckUsingRegx)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(5, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem3)
        self.btMark = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btMark.sizePolicy().hasHeightForWidth())
        self.btMark.setSizePolicy(sizePolicy)
        self.btMark.setMinimumSize(QtCore.QSize(28, 24))
        self.btMark.setMaximumSize(QtCore.QSize(28, 24))
        self.btMark.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/mark.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btMark.setIcon(icon1)
        self.btMark.setObjectName("btMark")
        self.layoutFilter.addWidget(self.btMark)
        self.btPrevMark = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btPrevMark.sizePolicy().hasHeightForWidth())
        self.btPrevMark.setSizePolicy(sizePolicy)
        self.btPrevMark.setMinimumSize(QtCore.QSize(28, 24))
        self.btPrevMark.setMaximumSize(QtCore.QSize(28, 24))
        self.btPrevMark.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/bt_prev_marked.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btPrevMark.setIcon(icon2)
        self.btPrevMark.setObjectName("btPrevMark")
        self.layoutFilter.addWidget(self.btPrevMark)
        self.btNextMark = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btNextMark.sizePolicy().hasHeightForWidth())
        self.btNextMark.setSizePolicy(sizePolicy)
        self.btNextMark.setMinimumSize(QtCore.QSize(28, 24))
        self.btNextMark.setMaximumSize(QtCore.QSize(28, 24))
        self.btNextMark.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/bt_next_marked.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btNextMark.setIcon(icon3)
        self.btNextMark.setObjectName("btNextMark")
        self.layoutFilter.addWidget(self.btNextMark)
        self.btSave = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btSave.sizePolicy().hasHeightForWidth())
        self.btSave.setSizePolicy(sizePolicy)
        self.btSave.setMinimumSize(QtCore.QSize(28, 24))
        self.btSave.setMaximumSize(QtCore.QSize(28, 24))
        self.btSave.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/bt_save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSave.setIcon(icon4)
        self.btSave.setObjectName("btSave")
        self.layoutFilter.addWidget(self.btSave)
        self.btSetting = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btSetting.sizePolicy().hasHeightForWidth())
        self.btSetting.setSizePolicy(sizePolicy)
        self.btSetting.setMinimumSize(QtCore.QSize(28, 24))
        self.btSetting.setMaximumSize(QtCore.QSize(28, 24))
        self.btSetting.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/bt_settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btSetting.setIcon(icon5)
        self.btSetting.setObjectName("btSetting")
        self.layoutFilter.addWidget(self.btSetting)
        spacerItem4 = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutFilter.addItem(spacerItem4)
        self.layoutView.addLayout(self.layoutFilter)
        self.layoutTracer = QtWidgets.QHBoxLayout()
        self.layoutTracer.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layoutTracer.setContentsMargins(-1, 2, -1, 2)
        self.layoutTracer.setSpacing(0)
        self.layoutTracer.setObjectName("layoutTracer")
        self.layoutView.addLayout(self.layoutTracer)
        self.gridLayout.addLayout(self.layoutView, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btFilter.setToolTip(_translate("Form", "Filter content"))
        self.ckUsingRegx.setText(_translate("Form", "Regx"))
        self.btPrevMark.setToolTip(_translate("Form", "Prev marked"))
        self.btNextMark.setToolTip(_translate("Form", "Next marked"))
        self.btSave.setToolTip(_translate("Form", "Save"))
        self.btSetting.setToolTip(_translate("Form", "Setting"))
import AndroidBoy_rc
