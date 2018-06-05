# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expertwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_expertWindow(object):
    def setupUi(self, expertWindow):
        expertWindow.setObjectName("expertWindow")
        expertWindow.resize(700, 450)
        expertWindow.setMinimumSize(QtCore.QSize(700, 450))
        expertWindow.setMaximumSize(QtCore.QSize(700, 600))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        expertWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/expert_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        expertWindow.setWindowIcon(icon)
        expertWindow.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(expertWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(expertWindow)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    top: -1px;\n"
"    background-color: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    border-top: 1px solid rgb(180,180,180);\n"
"    border-left: 1px solid rgb(180,180,180);\n"
"    border-right: 1px solid rgb(180,180,180);\n"
"    border-top-right-radius: 5px;\n"
"    border-top-left-radius: 5px;\n"
"    padding: 2px 10px 2px 10px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(210,210,210);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(230,230,230);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 4px; \n"
"}\n"
"\n"
"QTabBar::scroller {\n"
"}\n"
"\n"
"QTabBar QToolButton {\n"
"    border: 1px solid rgb(180,180,180);\n"
"    background-color: rgb(240,240,240);\n"
"}\n"
"\n"
"QTabBar QToolButton:hover {\n"
"    background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow {\n"
"    image: url(icons/right_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::right-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow {\n"
"    image: url(icons/left_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin : 2px 2px 2px 2px;\n"
"}\n"
"\n"
"QTabBar QToolButton::left-arrow:pressed {\n"
"    right: -1px;\n"
"    bottom: -1px;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tabWidgetPage1)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.main_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage1)
        self.main_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.main_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_scroll_area.setWidgetResizable(True)
        self.main_scroll_area.setObjectName("main_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 632, 345))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(14)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.main_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.main_lb_1.setEnabled(True)
        self.main_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_1.setFont(font)
        self.main_lb_1.setObjectName("main_lb_1")
        self.gridLayout_3.addWidget(self.main_lb_1, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_ln_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.main_ln_1.setMinimumSize(QtCore.QSize(400, 27))
        self.main_ln_1.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_ln_1.setFont(font)
        self.main_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.main_ln_1.setObjectName("main_ln_1")
        self.horizontalLayout_2.addWidget(self.main_ln_1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.ew_infoButton_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ew_infoButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ew_infoButton_1.setIcon(icon1)
        self.ew_infoButton_1.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_1.setAutoRaise(False)
        self.ew_infoButton_1.setObjectName("ew_infoButton_1")
        self.horizontalLayout_2.addWidget(self.ew_infoButton_1)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.main_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.main_lb_2.setEnabled(True)
        self.main_lb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_2.setFont(font)
        self.main_lb_2.setObjectName("main_lb_2")
        self.gridLayout_3.addWidget(self.main_lb_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.main_ln_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.main_ln_2.setMinimumSize(QtCore.QSize(400, 27))
        self.main_ln_2.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_ln_2.setFont(font)
        self.main_ln_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.main_ln_2.setObjectName("main_ln_2")
        self.horizontalLayout_3.addWidget(self.main_ln_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.ew_infoButton_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ew_infoButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_2.setText("")
        self.ew_infoButton_2.setIcon(icon1)
        self.ew_infoButton_2.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_2.setAutoRaise(False)
        self.ew_infoButton_2.setObjectName("ew_infoButton_2")
        self.horizontalLayout_3.addWidget(self.ew_infoButton_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.main_lb_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.main_lb_3.setEnabled(True)
        self.main_lb_3.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_3.setFont(font)
        self.main_lb_3.setObjectName("main_lb_3")
        self.gridLayout_3.addWidget(self.main_lb_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.main_ln_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.main_ln_3.setMinimumSize(QtCore.QSize(400, 27))
        self.main_ln_3.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_ln_3.setFont(font)
        self.main_ln_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.main_ln_3.setObjectName("main_ln_3")
        self.horizontalLayout_4.addWidget(self.main_ln_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.ew_infoButton_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ew_infoButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_3.setText("")
        self.ew_infoButton_3.setIcon(icon1)
        self.ew_infoButton_3.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_3.setAutoRaise(False)
        self.ew_infoButton_3.setObjectName("ew_infoButton_3")
        self.horizontalLayout_4.addWidget(self.ew_infoButton_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.main_lb_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.main_lb_4.setEnabled(True)
        self.main_lb_4.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_4.setFont(font)
        self.main_lb_4.setObjectName("main_lb_4")
        self.gridLayout_3.addWidget(self.main_lb_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.main_ln_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.main_ln_4.setMinimumSize(QtCore.QSize(400, 27))
        self.main_ln_4.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_ln_4.setFont(font)
        self.main_ln_4.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.main_ln_4.setObjectName("main_ln_4")
        self.horizontalLayout_5.addWidget(self.main_ln_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.ew_infoButton_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ew_infoButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_4.setText("")
        self.ew_infoButton_4.setIcon(icon1)
        self.ew_infoButton_4.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_4.setAutoRaise(False)
        self.ew_infoButton_4.setObjectName("ew_infoButton_4")
        self.horizontalLayout_5.addWidget(self.ew_infoButton_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.main_lb_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.main_lb_5.setEnabled(True)
        self.main_lb_5.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_5.setFont(font)
        self.main_lb_5.setObjectName("main_lb_5")
        self.gridLayout_3.addWidget(self.main_lb_5, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.main_ln_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.main_ln_5.setMinimumSize(QtCore.QSize(400, 27))
        self.main_ln_5.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_ln_5.setFont(font)
        self.main_ln_5.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.main_ln_5.setObjectName("main_ln_5")
        self.horizontalLayout_6.addWidget(self.main_ln_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.ew_infoButton_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ew_infoButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_5.setText("")
        self.ew_infoButton_5.setIcon(icon1)
        self.ew_infoButton_5.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_5.setAutoRaise(False)
        self.ew_infoButton_5.setObjectName("ew_infoButton_5")
        self.horizontalLayout_6.addWidget(self.ew_infoButton_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)
        self.main_lb_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.main_lb_6.setEnabled(True)
        self.main_lb_6.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_6.setFont(font)
        self.main_lb_6.setObjectName("main_lb_6")
        self.gridLayout_3.addWidget(self.main_lb_6, 5, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.main_ln_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.main_ln_6.setMinimumSize(QtCore.QSize(400, 27))
        self.main_ln_6.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_ln_6.setFont(font)
        self.main_ln_6.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.main_ln_6.setObjectName("main_ln_6")
        self.horizontalLayout_7.addWidget(self.main_ln_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.ew_infoButton_6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ew_infoButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_6.setText("")
        self.ew_infoButton_6.setIcon(icon1)
        self.ew_infoButton_6.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_6.setAutoRaise(False)
        self.ew_infoButton_6.setObjectName("ew_infoButton_6")
        self.horizontalLayout_7.addWidget(self.ew_infoButton_6)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)
        self.main_lb_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.main_lb_7.setEnabled(True)
        self.main_lb_7.setMinimumSize(QtCore.QSize(0, 27))
        self.main_lb_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_lb_7.setFont(font)
        self.main_lb_7.setObjectName("main_lb_7")
        self.gridLayout_3.addWidget(self.main_lb_7, 6, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.main_ln_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.main_ln_7.setMinimumSize(QtCore.QSize(400, 27))
        self.main_ln_7.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_ln_7.setFont(font)
        self.main_ln_7.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.main_ln_7.setObjectName("main_ln_7")
        self.horizontalLayout_8.addWidget(self.main_ln_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.ew_infoButton_7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ew_infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_7.setText("")
        self.ew_infoButton_7.setIcon(icon1)
        self.ew_infoButton_7.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_7.setAutoRaise(False)
        self.ew_infoButton_7.setObjectName("ew_infoButton_7")
        self.horizontalLayout_8.addWidget(self.ew_infoButton_7)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 6, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 1, 2, 2)
        spacerItem9 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 2, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 175, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 3, 2, 1, 1)
        self.main_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_26.addWidget(self.main_scroll_area, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tabWidgetPage2)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.area_time_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage2)
        self.area_time_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.area_time_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.area_time_scroll_area.setWidgetResizable(True)
        self.area_time_scroll_area.setObjectName("area_time_scroll_area")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 652, 319))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem11, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem12, 1, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setVerticalSpacing(14)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.area_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.area_lb_1.setEnabled(True)
        self.area_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.area_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_lb_1.setFont(font)
        self.area_lb_1.setObjectName("area_lb_1")
        self.gridLayout_5.addWidget(self.area_lb_1, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.area_ln_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.area_ln_1.setMinimumSize(QtCore.QSize(400, 27))
        self.area_ln_1.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_ln_1.setFont(font)
        self.area_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.area_ln_1.setObjectName("area_ln_1")
        self.horizontalLayout_9.addWidget(self.area_ln_1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.ew_infoButton_8 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.ew_infoButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_8.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_8.setText("")
        self.ew_infoButton_8.setIcon(icon1)
        self.ew_infoButton_8.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_8.setAutoRaise(False)
        self.ew_infoButton_8.setObjectName("ew_infoButton_8")
        self.horizontalLayout_9.addWidget(self.ew_infoButton_8)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.area_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.area_lb_2.setEnabled(True)
        self.area_lb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.area_lb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_lb_2.setFont(font)
        self.area_lb_2.setObjectName("area_lb_2")
        self.gridLayout_5.addWidget(self.area_lb_2, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.area_ln_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.area_ln_2.setMinimumSize(QtCore.QSize(400, 27))
        self.area_ln_2.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_ln_2.setFont(font)
        self.area_ln_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.area_ln_2.setObjectName("area_ln_2")
        self.horizontalLayout_10.addWidget(self.area_ln_2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.ew_infoButton_9 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.ew_infoButton_9.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_9.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_9.setText("")
        self.ew_infoButton_9.setIcon(icon1)
        self.ew_infoButton_9.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_9.setAutoRaise(False)
        self.ew_infoButton_9.setObjectName("ew_infoButton_9")
        self.horizontalLayout_10.addWidget(self.ew_infoButton_9)
        self.gridLayout_5.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
        self.area_lb_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.area_lb_3.setEnabled(True)
        self.area_lb_3.setMinimumSize(QtCore.QSize(0, 27))
        self.area_lb_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_lb_3.setFont(font)
        self.area_lb_3.setObjectName("area_lb_3")
        self.gridLayout_5.addWidget(self.area_lb_3, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.area_ln_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.area_ln_3.setMinimumSize(QtCore.QSize(400, 27))
        self.area_ln_3.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_ln_3.setFont(font)
        self.area_ln_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.area_ln_3.setObjectName("area_ln_3")
        self.horizontalLayout_11.addWidget(self.area_ln_3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.ew_infoButton_10 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.ew_infoButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_10.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_10.setText("")
        self.ew_infoButton_10.setIcon(icon1)
        self.ew_infoButton_10.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_10.setAutoRaise(False)
        self.ew_infoButton_10.setObjectName("ew_infoButton_10")
        self.horizontalLayout_11.addWidget(self.ew_infoButton_10)
        self.gridLayout_5.addLayout(self.horizontalLayout_11, 2, 1, 1, 1)
        self.area_lb_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.area_lb_4.setEnabled(True)
        self.area_lb_4.setMinimumSize(QtCore.QSize(0, 27))
        self.area_lb_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_lb_4.setFont(font)
        self.area_lb_4.setObjectName("area_lb_4")
        self.gridLayout_5.addWidget(self.area_lb_4, 3, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.area_ln_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.area_ln_4.setMinimumSize(QtCore.QSize(400, 27))
        self.area_ln_4.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_ln_4.setFont(font)
        self.area_ln_4.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.area_ln_4.setObjectName("area_ln_4")
        self.horizontalLayout_12.addWidget(self.area_ln_4)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem16)
        self.ew_infoButton_11 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.ew_infoButton_11.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_11.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_11.setText("")
        self.ew_infoButton_11.setIcon(icon1)
        self.ew_infoButton_11.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_11.setAutoRaise(False)
        self.ew_infoButton_11.setObjectName("ew_infoButton_11")
        self.horizontalLayout_12.addWidget(self.ew_infoButton_11)
        self.gridLayout_5.addLayout(self.horizontalLayout_12, 3, 1, 1, 1)
        self.area_lb_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.area_lb_5.setEnabled(True)
        self.area_lb_5.setMinimumSize(QtCore.QSize(0, 27))
        self.area_lb_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_lb_5.setFont(font)
        self.area_lb_5.setObjectName("area_lb_5")
        self.gridLayout_5.addWidget(self.area_lb_5, 4, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.area_ln_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.area_ln_5.setMinimumSize(QtCore.QSize(400, 27))
        self.area_ln_5.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_ln_5.setFont(font)
        self.area_ln_5.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.area_ln_5.setObjectName("area_ln_5")
        self.horizontalLayout_13.addWidget(self.area_ln_5)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem17)
        self.ew_infoButton_12 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.ew_infoButton_12.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_12.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_12.setText("")
        self.ew_infoButton_12.setIcon(icon1)
        self.ew_infoButton_12.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_12.setAutoRaise(False)
        self.ew_infoButton_12.setObjectName("ew_infoButton_12")
        self.horizontalLayout_13.addWidget(self.ew_infoButton_12)
        self.gridLayout_5.addLayout(self.horizontalLayout_13, 4, 1, 1, 1)
        self.area_lb_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.area_lb_6.setEnabled(True)
        self.area_lb_6.setMinimumSize(QtCore.QSize(0, 27))
        self.area_lb_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_lb_6.setFont(font)
        self.area_lb_6.setObjectName("area_lb_6")
        self.gridLayout_5.addWidget(self.area_lb_6, 5, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.area_ln_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.area_ln_6.setMinimumSize(QtCore.QSize(400, 27))
        self.area_ln_6.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_ln_6.setFont(font)
        self.area_ln_6.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.area_ln_6.setObjectName("area_ln_6")
        self.horizontalLayout_14.addWidget(self.area_ln_6)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem18)
        self.ew_infoButton_13 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.ew_infoButton_13.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_13.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_13.setText("")
        self.ew_infoButton_13.setIcon(icon1)
        self.ew_infoButton_13.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_13.setAutoRaise(False)
        self.ew_infoButton_13.setObjectName("ew_infoButton_13")
        self.horizontalLayout_14.addWidget(self.ew_infoButton_13)
        self.gridLayout_5.addLayout(self.horizontalLayout_14, 5, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 1, 2, 2)
        spacerItem19 = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem19, 2, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem20, 3, 2, 1, 1)
        self.area_time_scroll_area.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_18.addWidget(self.area_time_scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabWidgetPage3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.other_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage3)
        self.other_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 1px solid rgb(240,240,240);\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid rgb(240,240,240);\n"
"  border-right: 1px solid white;\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 1px solid white;\n"
"  border-left: 1px solid white;\n"
"  border-right: 1px solid rgb(240,240,240);\n"
"  border-bottom: 1px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.other_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.other_scroll_area.setWidgetResizable(True)
        self.other_scroll_area.setObjectName("other_scroll_area")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 652, 319))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_8.addItem(spacerItem21, 0, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem22, 1, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setVerticalSpacing(14)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.other_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.other_lb_1.setEnabled(True)
        self.other_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.other_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.other_lb_1.setFont(font)
        self.other_lb_1.setObjectName("other_lb_1")
        self.gridLayout_7.addWidget(self.other_lb_1, 0, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.other_ln_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.other_ln_1.setMinimumSize(QtCore.QSize(400, 27))
        self.other_ln_1.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.other_ln_1.setFont(font)
        self.other_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.other_ln_1.setObjectName("other_ln_1")
        self.horizontalLayout_17.addWidget(self.other_ln_1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem23)
        self.ew_infoButton_14 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_7)
        self.ew_infoButton_14.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_14.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_14.setText("")
        self.ew_infoButton_14.setIcon(icon1)
        self.ew_infoButton_14.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_14.setAutoRaise(False)
        self.ew_infoButton_14.setObjectName("ew_infoButton_14")
        self.horizontalLayout_17.addWidget(self.ew_infoButton_14)
        self.gridLayout_7.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)
        self.other_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.other_lb_2.setEnabled(True)
        self.other_lb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.other_lb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.other_lb_2.setFont(font)
        self.other_lb_2.setObjectName("other_lb_2")
        self.gridLayout_7.addWidget(self.other_lb_2, 1, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.other_ln_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.other_ln_2.setMinimumSize(QtCore.QSize(400, 27))
        self.other_ln_2.setMaximumSize(QtCore.QSize(400, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.other_ln_2.setFont(font)
        self.other_ln_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.other_ln_2.setObjectName("other_ln_2")
        self.horizontalLayout_16.addWidget(self.other_ln_2)
        spacerItem24 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem24)
        self.ew_infoButton_15 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_7)
        self.ew_infoButton_15.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_15.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_15.setText("")
        self.ew_infoButton_15.setIcon(icon1)
        self.ew_infoButton_15.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_15.setAutoRaise(False)
        self.ew_infoButton_15.setObjectName("ew_infoButton_15")
        self.horizontalLayout_16.addWidget(self.ew_infoButton_15)
        self.gridLayout_7.addLayout(self.horizontalLayout_16, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.other_lb_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.other_lb_3.setEnabled(True)
        self.other_lb_3.setMinimumSize(QtCore.QSize(0, 27))
        self.other_lb_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.other_lb_3.setFont(font)
        self.other_lb_3.setObjectName("other_lb_3")
        self.verticalLayout_2.addWidget(self.other_lb_3)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem25)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.other_ln_3 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_7)
        self.other_ln_3.setMaximumSize(QtCore.QSize(16777215, 150))
        self.other_ln_3.setStyleSheet("QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"}")
        self.other_ln_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.other_ln_3.setObjectName("other_ln_3")
        self.horizontalLayout_15.addWidget(self.other_ln_3)
        spacerItem26 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem26)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ew_infoButton_16 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_7)
        self.ew_infoButton_16.setMaximumSize(QtCore.QSize(27, 27))
        self.ew_infoButton_16.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ew_infoButton_16.setText("")
        self.ew_infoButton_16.setIcon(icon1)
        self.ew_infoButton_16.setIconSize(QtCore.QSize(23, 23))
        self.ew_infoButton_16.setAutoRaise(False)
        self.ew_infoButton_16.setObjectName("ew_infoButton_16")
        self.verticalLayout_3.addWidget(self.ew_infoButton_16)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem27)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        self.gridLayout_7.addLayout(self.horizontalLayout_15, 2, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 1, 2, 2)
        spacerItem28 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem28, 2, 3, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 24, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem29, 3, 2, 1, 1)
        self.other_scroll_area.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_2.addWidget(self.other_scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        spacerItem30 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem30)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem31 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem31)
        self.submit = QtWidgets.QToolButton(expertWindow)
        self.submit.setMinimumSize(QtCore.QSize(90, 27))
        self.submit.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.submit.setFont(font)
        self.submit.setStyleSheet("QToolButton {\n"
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
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        spacerItem32 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem32)
        self.cancel = QtWidgets.QToolButton(expertWindow)
        self.cancel.setMinimumSize(QtCore.QSize(90, 27))
        self.cancel.setMaximumSize(QtCore.QSize(90, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QToolButton {\n"
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
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem33)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(expertWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(expertWindow)

    def retranslateUi(self, expertWindow):
        _translate = QtCore.QCoreApplication.translate
        expertWindow.setWindowTitle(_translate("expertWindow", "Raw Inputs"))
        self.main_lb_1.setText(_translate("expertWindow", "dataset:"))
        self.main_lb_2.setText(_translate("expertWindow", "stream:"))
        self.main_lb_3.setText(_translate("expertWindow", "type:"))
        self.main_lb_4.setText(_translate("expertWindow", "class:"))
        self.main_lb_5.setText(_translate("expertWindow", "expver:"))
        self.main_lb_6.setText(_translate("expertWindow", "levtype:"))
        self.main_lb_7.setText(_translate("expertWindow", "levelist:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("expertWindow", "Main keywords"))
        self.area_lb_1.setText(_translate("expertWindow", "date:"))
        self.area_lb_2.setText(_translate("expertWindow", "step:"))
        self.area_lb_3.setText(_translate("expertWindow", "time:"))
        self.area_lb_4.setText(_translate("expertWindow", "grid:"))
        self.area_lb_5.setText(_translate("expertWindow", "area:"))
        self.area_lb_6.setText(_translate("expertWindow", "param:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("expertWindow", "Area, time and parameter keywords"))
        self.other_lb_1.setText(_translate("expertWindow", "target:"))
        self.other_lb_2.setText(_translate("expertWindow", "format:"))
        self.other_lb_3.setText(_translate("expertWindow", "other keywords:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("expertWindow", "Other keywords"))
        self.submit.setText(_translate("expertWindow", "Submit"))
        self.cancel.setText(_translate("expertWindow", "Cancel"))

