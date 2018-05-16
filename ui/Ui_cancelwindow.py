# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cancelwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cancelWindow(object):
    def setupUi(self, cancelWindow):
        cancelWindow.setObjectName("cancelWindow")
        cancelWindow.resize(500, 220)
        cancelWindow.setMinimumSize(QtCore.QSize(500, 220))
        cancelWindow.setMaximumSize(QtCore.QSize(500, 220))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        cancelWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cancelWindow.setWindowIcon(icon)
        cancelWindow.setStyleSheet("QWidget {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(cancelWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cw_label_2 = QtWidgets.QLabel(cancelWindow)
        self.cw_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.cw_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.cw_label_2.setText("")
        self.cw_label_2.setPixmap(QtGui.QPixmap("icons/warning_popup_icon.svg"))
        self.cw_label_2.setScaledContents(True)
        self.cw_label_2.setObjectName("cw_label_2")
        self.verticalLayout_2.addWidget(self.cw_label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cw_label_1 = QtWidgets.QLabel(cancelWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cw_label_1.sizePolicy().hasHeightForWidth())
        self.cw_label_1.setSizePolicy(sizePolicy)
        self.cw_label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.cw_label_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cw_label_1.setFont(font)
        self.cw_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.cw_label_1.setWordWrap(True)
        self.cw_label_1.setObjectName("cw_label_1")
        self.horizontalLayout.addWidget(self.cw_label_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.cw_okButton = QtWidgets.QToolButton(cancelWindow)
        self.cw_okButton.setMinimumSize(QtCore.QSize(90, 27))
        self.cw_okButton.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cw_okButton.setFont(font)
        self.cw_okButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.cw_okButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.cw_okButton.setObjectName("cw_okButton")
        self.horizontalLayout_2.addWidget(self.cw_okButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.cw_cancelButton = QtWidgets.QToolButton(cancelWindow)
        self.cw_cancelButton.setMinimumSize(QtCore.QSize(150, 27))
        self.cw_cancelButton.setMaximumSize(QtCore.QSize(150, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cw_cancelButton.setFont(font)
        self.cw_cancelButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.cw_cancelButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.cw_cancelButton.setObjectName("cw_cancelButton")
        self.horizontalLayout_2.addWidget(self.cw_cancelButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(cancelWindow)
        QtCore.QMetaObject.connectSlotsByName(cancelWindow)

    def retranslateUi(self, cancelWindow):
        _translate = QtCore.QCoreApplication.translate
        cancelWindow.setWindowTitle(_translate("cancelWindow", "Warning"))
        self.cw_label_1.setText(_translate("cancelWindow", "<html><head/><body><p align=\"justify\">A query can\'t be canceled when it is queued from the API. By clicking on <span style=\" font-weight:600;\">Cancel anyway</span>, you will quit the <span style=\" font-weight:600;\">Download window</span>, but the query will still on going on ECMWF servers. To cancel a query, you have to access your ECMWF account and check your jobs.</p></body></html>"))
        self.cw_okButton.setText(_translate("cancelWindow", "Ok"))
        self.cw_cancelButton.setText(_translate("cancelWindow", "Cancel anyway"))

