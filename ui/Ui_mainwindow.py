# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 659)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/downloader_update_off_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
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
        self.dataset_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage1)
        self.dataset_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
        self.dataset_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dataset_scroll_area.setWidgetResizable(True)
        self.dataset_scroll_area.setObjectName("dataset_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 951, 482))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_6.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dataset_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataset_lb_1.sizePolicy().hasHeightForWidth())
        self.dataset_lb_1.setSizePolicy(sizePolicy)
        self.dataset_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_lb_1.setFont(font)
        self.dataset_lb_1.setObjectName("dataset_lb_1")
        self.horizontalLayout_2.addWidget(self.dataset_lb_1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.mw_infoButton_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.mw_infoButton_1.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/info_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mw_infoButton_1.setIcon(icon1)
        self.mw_infoButton_1.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_1.setAutoRaise(False)
        self.mw_infoButton_1.setObjectName("mw_infoButton_1")
        self.horizontalLayout_2.addWidget(self.mw_infoButton_1)
        spacerItem3 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.dataset_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dataset_lb_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataset_lb_2.sizePolicy().hasHeightForWidth())
        self.dataset_lb_2.setSizePolicy(sizePolicy)
        self.dataset_lb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_lb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_lb_2.setFont(font)
        self.dataset_lb_2.setObjectName("dataset_lb_2")
        self.horizontalLayout_2.addWidget(self.dataset_lb_2)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.mw_infoButton_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.mw_infoButton_2.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_2.setText("")
        self.mw_infoButton_2.setIcon(icon1)
        self.mw_infoButton_2.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_2.setAutoRaise(False)
        self.mw_infoButton_2.setObjectName("mw_infoButton_2")
        self.horizontalLayout_2.addWidget(self.mw_infoButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dataset_rb_12 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_12.setEnabled(False)
        self.dataset_rb_12.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_12.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_12.setFont(font)
        self.dataset_rb_12.setObjectName("dataset_rb_12")
        self.dataset_gb_1 = QtWidgets.QButtonGroup(MainWindow)
        self.dataset_gb_1.setObjectName("dataset_gb_1")
        self.dataset_gb_1.addButton(self.dataset_rb_12)
        self.verticalLayout.addWidget(self.dataset_rb_12)
        self.dataset_rb_13 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_13.setEnabled(False)
        self.dataset_rb_13.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_13.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_13.setFont(font)
        self.dataset_rb_13.setObjectName("dataset_rb_13")
        self.dataset_gb_1.addButton(self.dataset_rb_13)
        self.verticalLayout.addWidget(self.dataset_rb_13)
        self.dataset_rb_8 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_8.setEnabled(False)
        self.dataset_rb_8.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_8.setFont(font)
        self.dataset_rb_8.setObjectName("dataset_rb_8")
        self.dataset_gb_1.addButton(self.dataset_rb_8)
        self.verticalLayout.addWidget(self.dataset_rb_8)
        self.dataset_rb_9 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_9.setEnabled(False)
        self.dataset_rb_9.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_9.setFont(font)
        self.dataset_rb_9.setObjectName("dataset_rb_9")
        self.dataset_gb_1.addButton(self.dataset_rb_9)
        self.verticalLayout.addWidget(self.dataset_rb_9)
        self.dataset_rb_10 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_10.setEnabled(False)
        self.dataset_rb_10.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_10.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_10.setFont(font)
        self.dataset_rb_10.setObjectName("dataset_rb_10")
        self.dataset_gb_1.addButton(self.dataset_rb_10)
        self.verticalLayout.addWidget(self.dataset_rb_10)
        self.dataset_rb_11 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_11.setEnabled(False)
        self.dataset_rb_11.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_11.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_11.setFont(font)
        self.dataset_rb_11.setObjectName("dataset_rb_11")
        self.dataset_gb_1.addButton(self.dataset_rb_11)
        self.verticalLayout.addWidget(self.dataset_rb_11)
        self.dataset_rb_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_2.setEnabled(False)
        self.dataset_rb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_2.setFont(font)
        self.dataset_rb_2.setObjectName("dataset_rb_2")
        self.dataset_gb_1.addButton(self.dataset_rb_2)
        self.verticalLayout.addWidget(self.dataset_rb_2)
        self.dataset_rb_1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_1.setFont(font)
        self.dataset_rb_1.setObjectName("dataset_rb_1")
        self.dataset_gb_1.addButton(self.dataset_rb_1)
        self.verticalLayout.addWidget(self.dataset_rb_1)
        self.dataset_rb_14 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.dataset_rb_14.setEnabled(False)
        self.dataset_rb_14.setMinimumSize(QtCore.QSize(0, 27))
        self.dataset_rb_14.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dataset_rb_14.setFont(font)
        self.dataset_rb_14.setObjectName("dataset_rb_14")
        self.dataset_gb_1.addButton(self.dataset_rb_14)
        self.verticalLayout.addWidget(self.dataset_rb_14)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(225, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.field_vertical_layout = QtWidgets.QVBoxLayout()
        self.field_vertical_layout.setSpacing(16)
        self.field_vertical_layout.setObjectName("field_vertical_layout")
        self.horizontalLayout_3.addLayout(self.field_vertical_layout)
        spacerItem10 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_6.addLayout(self.verticalLayout_2, 1, 1, 2, 1)
        spacerItem11 = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem11, 2, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 175, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem12, 3, 1, 1, 1)
        self.dataset_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_26.addWidget(self.dataset_scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tabWidgetPage2)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.parameters_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage2)
        self.parameters_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"\n"
"\n"
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
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
        self.parameters_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.parameters_scroll_area.setWidgetResizable(True)
        self.parameters_scroll_area.setObjectName("parameters_scroll_area")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 951, 482))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_5.addItem(spacerItem13, 0, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem14, 1, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.parameters_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.parameters_lb_1.setEnabled(False)
        self.parameters_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.parameters_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.parameters_lb_1.setFont(font)
        self.parameters_lb_1.setObjectName("parameters_lb_1")
        self.horizontalLayout_13.addWidget(self.parameters_lb_1)
        spacerItem15 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.mw_infoButton_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_6)
        self.mw_infoButton_3.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_3.setText("")
        self.mw_infoButton_3.setIcon(icon1)
        self.mw_infoButton_3.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_3.setAutoRaise(False)
        self.mw_infoButton_3.setObjectName("mw_infoButton_3")
        self.horizontalLayout_13.addWidget(self.mw_infoButton_3)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem17)
        self.parameter_grid_layout = QtWidgets.QGridLayout()
        self.parameter_grid_layout.setObjectName("parameter_grid_layout")
        self.horizontalLayout_18.addLayout(self.parameter_grid_layout)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem18)
        self.verticalLayout_10.addLayout(self.horizontalLayout_18)
        self.gridLayout_5.addLayout(self.verticalLayout_10, 1, 1, 2, 2)
        spacerItem19 = QtWidgets.QSpacerItem(51, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem19, 2, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 363, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem20, 3, 2, 1, 1)
        self.parameters_scroll_area.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_18.addWidget(self.parameters_scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabWidgetPage3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.time_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage3)
        self.time_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"\n"
"\n"
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
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
        self.time_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.time_scroll_area.setWidgetResizable(True)
        self.time_scroll_area.setObjectName("time_scroll_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 951, 482))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem21 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem21, 0, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem22, 1, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.time_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.time_lb_1.setEnabled(False)
        self.time_lb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.time_lb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_lb_1.setFont(font)
        self.time_lb_1.setObjectName("time_lb_1")
        self.horizontalLayout_14.addWidget(self.time_lb_1)
        spacerItem23 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem23)
        self.mw_infoButton_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.mw_infoButton_4.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_4.setText("")
        self.mw_infoButton_4.setIcon(icon1)
        self.mw_infoButton_4.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_4.setAutoRaise(False)
        self.mw_infoButton_4.setObjectName("mw_infoButton_4")
        self.horizontalLayout_14.addWidget(self.mw_infoButton_4)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem24)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem25)
        self.time_cb_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_1.setEnabled(False)
        self.time_cb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_1.setFont(font)
        self.time_cb_1.setObjectName("time_cb_1")
        self.time_bg_1 = QtWidgets.QButtonGroup(MainWindow)
        self.time_bg_1.setObjectName("time_bg_1")
        self.time_bg_1.setExclusive(False)
        self.time_bg_1.addButton(self.time_cb_1)
        self.horizontalLayout_16.addWidget(self.time_cb_1)
        self.time_cb_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_2.setEnabled(False)
        self.time_cb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_2.setFont(font)
        self.time_cb_2.setObjectName("time_cb_2")
        self.time_bg_1.addButton(self.time_cb_2)
        self.horizontalLayout_16.addWidget(self.time_cb_2)
        self.time_cb_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_3.setEnabled(False)
        self.time_cb_3.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_3.setFont(font)
        self.time_cb_3.setObjectName("time_cb_3")
        self.time_bg_1.addButton(self.time_cb_3)
        self.horizontalLayout_16.addWidget(self.time_cb_3)
        self.time_cb_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_4.setEnabled(False)
        self.time_cb_4.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_4.setFont(font)
        self.time_cb_4.setObjectName("time_cb_4")
        self.time_bg_1.addButton(self.time_cb_4)
        self.horizontalLayout_16.addWidget(self.time_cb_4)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem26)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        spacerItem27 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem27)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.time_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.time_lb_2.setEnabled(False)
        self.time_lb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.time_lb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_lb_2.setFont(font)
        self.time_lb_2.setObjectName("time_lb_2")
        self.horizontalLayout_15.addWidget(self.time_lb_2)
        spacerItem28 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem28)
        self.mw_infoButton_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.mw_infoButton_5.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_5.setText("")
        self.mw_infoButton_5.setIcon(icon1)
        self.mw_infoButton_5.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_5.setAutoRaise(False)
        self.mw_infoButton_5.setObjectName("mw_infoButton_5")
        self.horizontalLayout_15.addWidget(self.mw_infoButton_5)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem29)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem30)
        self.time_cb_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_5.setEnabled(False)
        self.time_cb_5.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_5.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_5.setFont(font)
        self.time_cb_5.setObjectName("time_cb_5")
        self.step_bg_1 = QtWidgets.QButtonGroup(MainWindow)
        self.step_bg_1.setObjectName("step_bg_1")
        self.step_bg_1.setExclusive(False)
        self.step_bg_1.addButton(self.time_cb_5)
        self.horizontalLayout_17.addWidget(self.time_cb_5)
        self.time_cb_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_6.setEnabled(False)
        self.time_cb_6.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_6.setFont(font)
        self.time_cb_6.setObjectName("time_cb_6")
        self.step_bg_1.addButton(self.time_cb_6)
        self.horizontalLayout_17.addWidget(self.time_cb_6)
        self.time_cb_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_7.setEnabled(False)
        self.time_cb_7.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_7.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_7.setFont(font)
        self.time_cb_7.setObjectName("time_cb_7")
        self.step_bg_1.addButton(self.time_cb_7)
        self.horizontalLayout_17.addWidget(self.time_cb_7)
        self.time_cb_8 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_8.setEnabled(False)
        self.time_cb_8.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_8.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_8.setFont(font)
        self.time_cb_8.setObjectName("time_cb_8")
        self.step_bg_1.addButton(self.time_cb_8)
        self.horizontalLayout_17.addWidget(self.time_cb_8)
        self.time_cb_9 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_3)
        self.time_cb_9.setEnabled(False)
        self.time_cb_9.setMinimumSize(QtCore.QSize(0, 27))
        self.time_cb_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_cb_9.setFont(font)
        self.time_cb_9.setObjectName("time_cb_9")
        self.step_bg_1.addButton(self.time_cb_9)
        self.horizontalLayout_17.addWidget(self.time_cb_9)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem31)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        spacerItem32 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem32)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.time_lb_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.time_lb_3.setEnabled(False)
        self.time_lb_3.setMinimumSize(QtCore.QSize(0, 27))
        self.time_lb_3.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_lb_3.setFont(font)
        self.time_lb_3.setObjectName("time_lb_3")
        self.horizontalLayout_7.addWidget(self.time_lb_3)
        spacerItem33 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem33)
        self.mw_infoButton_6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.mw_infoButton_6.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_6.setText("")
        self.mw_infoButton_6.setIcon(icon1)
        self.mw_infoButton_6.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_6.setAutoRaise(False)
        self.mw_infoButton_6.setObjectName("mw_infoButton_6")
        self.horizontalLayout_7.addWidget(self.mw_infoButton_6)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem34)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem35 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem35)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.time_rb_1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_3)
        self.time_rb_1.setEnabled(False)
        self.time_rb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.time_rb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_rb_1.setFont(font)
        self.time_rb_1.setObjectName("time_rb_1")
        self.period_bg_1 = QtWidgets.QButtonGroup(MainWindow)
        self.period_bg_1.setObjectName("period_bg_1")
        self.period_bg_1.addButton(self.time_rb_1)
        self.horizontalLayout_4.addWidget(self.time_rb_1)
        self.time_de_1 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_3)
        self.time_de_1.setEnabled(False)
        self.time_de_1.setMinimumSize(QtCore.QSize(130, 27))
        self.time_de_1.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_de_1.setFont(font)
        self.time_de_1.setStyleSheet("QDateEdit {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QDateEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}")
        self.time_de_1.setFrame(False)
        self.time_de_1.setAlignment(QtCore.Qt.AlignCenter)
        self.time_de_1.setAccelerated(True)
        self.time_de_1.setDateTime(QtCore.QDateTime(QtCore.QDate(1979, 1, 1), QtCore.QTime(23, 0, 0)))
        self.time_de_1.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.time_de_1.setCalendarPopup(True)
        self.time_de_1.setTimeSpec(QtCore.Qt.UTC)
        self.time_de_1.setDate(QtCore.QDate(1979, 1, 1))
        self.time_de_1.setObjectName("time_de_1")
        self.horizontalLayout_4.addWidget(self.time_de_1)
        self.time_lb_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.time_lb_4.setEnabled(False)
        self.time_lb_4.setMinimumSize(QtCore.QSize(0, 27))
        self.time_lb_4.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_lb_4.setFont(font)
        self.time_lb_4.setObjectName("time_lb_4")
        self.horizontalLayout_4.addWidget(self.time_lb_4)
        self.time_de_2 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_3)
        self.time_de_2.setEnabled(False)
        self.time_de_2.setMinimumSize(QtCore.QSize(130, 27))
        self.time_de_2.setMaximumSize(QtCore.QSize(130, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_de_2.setFont(font)
        self.time_de_2.setStyleSheet("QDateEdit {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QDateEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}")
        self.time_de_2.setFrame(False)
        self.time_de_2.setAlignment(QtCore.Qt.AlignCenter)
        self.time_de_2.setAccelerated(True)
        self.time_de_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 1, 1), QtCore.QTime(23, 0, 0)))
        self.time_de_2.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.time_de_2.setCalendarPopup(True)
        self.time_de_2.setTimeSpec(QtCore.Qt.UTC)
        self.time_de_2.setDate(QtCore.QDate(2018, 1, 1))
        self.time_de_2.setObjectName("time_de_2")
        self.horizontalLayout_4.addWidget(self.time_de_2)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem36)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.time_rb_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_3)
        self.time_rb_2.setEnabled(False)
        self.time_rb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.time_rb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_rb_2.setFont(font)
        self.time_rb_2.setObjectName("time_rb_2")
        self.period_bg_1.addButton(self.time_rb_2)
        self.horizontalLayout_5.addWidget(self.time_rb_2)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem37)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.time_vertical_layout = QtWidgets.QVBoxLayout()
        self.time_vertical_layout.setObjectName("time_vertical_layout")
        self.verticalLayout_6.addLayout(self.time_vertical_layout)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 1, 1, 1, 2)
        spacerItem38 = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem38, 1, 3, 1, 1)
        spacerItem39 = QtWidgets.QSpacerItem(20, 363, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem39, 2, 2, 1, 1)
        self.time_scroll_area.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.time_scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.tabWidgetPage4)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.area_scroll_area = QtWidgets.QScrollArea(self.tabWidgetPage4)
        self.area_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(167, 167, 167);\n"
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
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"\n"
"\n"
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
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
        self.area_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.area_scroll_area.setWidgetResizable(True)
        self.area_scroll_area.setObjectName("area_scroll_area")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 951, 482))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem40 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem40, 0, 1, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem41, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.area_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.area_lb_1.setEnabled(False)
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
        self.horizontalLayout_10.addWidget(self.area_lb_1)
        spacerItem42 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem42)
        self.area_cb_1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.area_cb_1.setEnabled(False)
        self.area_cb_1.setMinimumSize(QtCore.QSize(180, 27))
        self.area_cb_1.setMaximumSize(QtCore.QSize(180, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_cb_1.setFont(font)
        self.area_cb_1.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
"}")
        self.area_cb_1.setMaxVisibleItems(12)
        self.area_cb_1.setObjectName("area_cb_1")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.area_cb_1.addItem("")
        self.horizontalLayout_10.addWidget(self.area_cb_1)
        spacerItem43 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem43)
        self.mw_infoButton_7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.mw_infoButton_7.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_7.setText("")
        self.mw_infoButton_7.setIcon(icon1)
        self.mw_infoButton_7.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_7.setAutoRaise(False)
        self.mw_infoButton_7.setObjectName("mw_infoButton_7")
        self.horizontalLayout_10.addWidget(self.mw_infoButton_7)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem44)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.area_vertical_layout = QtWidgets.QVBoxLayout()
        self.area_vertical_layout.setObjectName("area_vertical_layout")
        self.verticalLayout_3.addLayout(self.area_vertical_layout)
        spacerItem45 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem45)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.area_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.area_lb_2.setEnabled(False)
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
        self.horizontalLayout_12.addWidget(self.area_lb_2)
        spacerItem46 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem46)
        self.area_cb_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.area_cb_2.setEnabled(False)
        self.area_cb_2.setMinimumSize(QtCore.QSize(140, 27))
        self.area_cb_2.setMaximumSize(QtCore.QSize(140, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_cb_2.setFont(font)
        self.area_cb_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, \n"
"                                stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(200,200,200);\n"
"    selection-color: black;\n"
"    background: #f0f0f0;\n"
"    border: 0px solid #f0f0f0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 5px 5px 5px 5px;\n"
"}")
        self.area_cb_2.setMaxVisibleItems(12)
        self.area_cb_2.setObjectName("area_cb_2")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.area_cb_2.addItem("")
        self.horizontalLayout_12.addWidget(self.area_cb_2)
        spacerItem47 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem47)
        self.mw_infoButton_8 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.mw_infoButton_8.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_8.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_8.setText("")
        self.mw_infoButton_8.setIcon(icon1)
        self.mw_infoButton_8.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_8.setAutoRaise(False)
        self.mw_infoButton_8.setObjectName("mw_infoButton_8")
        self.horizontalLayout_12.addWidget(self.mw_infoButton_8)
        spacerItem48 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem48)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        spacerItem49 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem49)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        spacerItem50 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem50)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.area_lb_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
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
        self.horizontalLayout_8.addWidget(self.area_lb_5)
        spacerItem51 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem51)
        self.area_ln_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
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
        self.horizontalLayout_8.addWidget(self.area_ln_5)
        spacerItem52 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem52)
        self.mw_infoButton_9 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.mw_infoButton_9.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_9.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_9.setText("")
        self.mw_infoButton_9.setIcon(icon1)
        self.mw_infoButton_9.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_9.setAutoRaise(False)
        self.mw_infoButton_9.setObjectName("mw_infoButton_9")
        self.horizontalLayout_8.addWidget(self.mw_infoButton_9)
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem53)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        spacerItem54 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem54)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.area_lb_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
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
        self.horizontalLayout_9.addWidget(self.area_lb_6)
        spacerItem55 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem55)
        self.area_rb_1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_4)
        self.area_rb_1.setMinimumSize(QtCore.QSize(0, 27))
        self.area_rb_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_rb_1.setFont(font)
        self.area_rb_1.setObjectName("area_rb_1")
        self.file_bg_1 = QtWidgets.QButtonGroup(MainWindow)
        self.file_bg_1.setObjectName("file_bg_1")
        self.file_bg_1.addButton(self.area_rb_1)
        self.horizontalLayout_9.addWidget(self.area_rb_1)
        self.area_rb_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_4)
        self.area_rb_2.setMinimumSize(QtCore.QSize(0, 27))
        self.area_rb_2.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.area_rb_2.setFont(font)
        self.area_rb_2.setObjectName("area_rb_2")
        self.file_bg_1.addButton(self.area_rb_2)
        self.horizontalLayout_9.addWidget(self.area_rb_2)
        spacerItem56 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem56)
        self.mw_infoButton_10 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.mw_infoButton_10.setMaximumSize(QtCore.QSize(27, 27))
        self.mw_infoButton_10.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.mw_infoButton_10.setText("")
        self.mw_infoButton_10.setIcon(icon1)
        self.mw_infoButton_10.setIconSize(QtCore.QSize(23, 23))
        self.mw_infoButton_10.setAutoRaise(False)
        self.mw_infoButton_10.setObjectName("mw_infoButton_10")
        self.horizontalLayout_9.addWidget(self.mw_infoButton_10)
        spacerItem57 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem57)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 2, 1)
        spacerItem58 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem58, 2, 2, 1, 1)
        spacerItem59 = QtWidgets.QSpacerItem(20, 363, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem59, 3, 1, 1, 1)
        self.area_scroll_area.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_31.addWidget(self.area_scroll_area, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem60)
        self.download_bt_1 = QtWidgets.QToolButton(self.centralwidget)
        self.download_bt_1.setEnabled(True)
        self.download_bt_1.setMinimumSize(QtCore.QSize(150, 35))
        self.download_bt_1.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.download_bt_1.setFont(font)
        self.download_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
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
        self.download_bt_1.setObjectName("download_bt_1")
        self.horizontalLayout.addWidget(self.download_bt_1)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem61)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem62 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem62, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/save_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/about_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionChangelog = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/changelog_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangelog.setIcon(icon6)
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.actionChangelog.setFont(font)
        self.actionChangelog.setObjectName("actionChangelog")
        self.actionSeparator1 = QtWidgets.QAction(MainWindow)
        self.actionSeparator1.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/separator_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSeparator1.setIcon(icon7)
        self.actionSeparator1.setObjectName("actionSeparator1")
        self.actionSeparator2 = QtWidgets.QAction(MainWindow)
        self.actionSeparator2.setEnabled(False)
        self.actionSeparator2.setIcon(icon7)
        self.actionSeparator2.setObjectName("actionSeparator2")
        self.actionSeparator3 = QtWidgets.QAction(MainWindow)
        self.actionSeparator3.setEnabled(False)
        self.actionSeparator3.setIcon(icon7)
        self.actionSeparator3.setObjectName("actionSeparator3")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setEnabled(False)
        self.actionUpdate.setIcon(icon)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOptions.setIcon(icon8)
        self.actionOptions.setObjectName("actionOptions")
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addAction(self.actionSeparator1)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSeparator2)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionChangelog)
        self.toolBar.addAction(self.actionSeparator3)
        self.toolBar.addAction(self.actionOptions)
        self.toolBar.addAction(self.actionUpdate)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.area_cb_1.setCurrentIndex(1)
        self.area_cb_2.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ECMWF Data Downloader"))
        self.dataset_lb_1.setText(_translate("MainWindow", "1) Select a dataset:"))
        self.dataset_lb_2.setText(_translate("MainWindow", "2) And a field:"))
        self.dataset_rb_12.setText(_translate("MainWindow", "CERA-20C"))
        self.dataset_rb_13.setText(_translate("MainWindow", "CERA-SAT"))
        self.dataset_rb_8.setText(_translate("MainWindow", "ERA5"))
        self.dataset_rb_9.setText(_translate("MainWindow", "ERA-15"))
        self.dataset_rb_10.setText(_translate("MainWindow", "ERA-20C"))
        self.dataset_rb_11.setText(_translate("MainWindow", "ERA-20CM"))
        self.dataset_rb_2.setText(_translate("MainWindow", "ERA-40"))
        self.dataset_rb_1.setText(_translate("MainWindow", "ERA-Interim"))
        self.dataset_rb_14.setText(_translate("MainWindow", "ERA-Interim/LAND"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("MainWindow", "Datasets and fields"))
        self.parameters_lb_1.setText(_translate("MainWindow", "3) Select one or multiple parameters:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("MainWindow", "Parameters"))
        self.time_lb_1.setText(_translate("MainWindow", "4) Select a time:"))
        self.time_cb_1.setText(_translate("MainWindow", "00:00:00"))
        self.time_cb_2.setText(_translate("MainWindow", "06:00:00"))
        self.time_cb_3.setText(_translate("MainWindow", "12:00:00"))
        self.time_cb_4.setText(_translate("MainWindow", "18:00:00"))
        self.time_lb_2.setText(_translate("MainWindow", "5) A time step:"))
        self.time_cb_5.setText(_translate("MainWindow", "0"))
        self.time_cb_6.setText(_translate("MainWindow", "3"))
        self.time_cb_7.setText(_translate("MainWindow", "6"))
        self.time_cb_8.setText(_translate("MainWindow", "9"))
        self.time_cb_9.setText(_translate("MainWindow", "12"))
        self.time_lb_3.setText(_translate("MainWindow", "6) And a time period:"))
        self.time_rb_1.setText(_translate("MainWindow", "From"))
        self.time_de_1.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.time_lb_4.setText(_translate("MainWindow", "to"))
        self.time_de_2.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))
        self.time_rb_2.setText(_translate("MainWindow", "Or"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("MainWindow", "Time period"))
        self.area_lb_1.setText(_translate("MainWindow", "7) Select an area:"))
        self.area_cb_1.setItemText(0, _translate("MainWindow", "Custom"))
        self.area_cb_1.setItemText(1, _translate("MainWindow", "Default (as archived)"))
        self.area_cb_1.setItemText(2, _translate("MainWindow", "Europe"))
        self.area_cb_1.setItemText(3, _translate("MainWindow", "Indonesia"))
        self.area_cb_1.setItemText(4, _translate("MainWindow", "Inter-tropical band"))
        self.area_cb_1.setItemText(5, _translate("MainWindow", "North America"))
        self.area_cb_1.setItemText(6, _translate("MainWindow", "Northern Hemisphere"))
        self.area_cb_1.setItemText(7, _translate("MainWindow", "South Asia"))
        self.area_cb_1.setItemText(8, _translate("MainWindow", "Southern Hemisphere"))
        self.area_cb_1.setItemText(9, _translate("MainWindow", "Tropical Pacific"))
        self.area_lb_2.setText(_translate("MainWindow", "8) And a grid resolution:"))
        self.area_cb_2.setItemText(0, _translate("MainWindow", "0.125° x 0.125°"))
        self.area_cb_2.setItemText(1, _translate("MainWindow", "0.25° x 0.25°"))
        self.area_cb_2.setItemText(2, _translate("MainWindow", "0.4° x 0.4°"))
        self.area_cb_2.setItemText(3, _translate("MainWindow", "0.5° x 0.5°"))
        self.area_cb_2.setItemText(4, _translate("MainWindow", "0.75° x 0.75°"))
        self.area_cb_2.setItemText(5, _translate("MainWindow", "1° x 1°"))
        self.area_cb_2.setItemText(6, _translate("MainWindow", "1.125° x 1.125°"))
        self.area_cb_2.setItemText(7, _translate("MainWindow", "1.5° x 1.5°"))
        self.area_cb_2.setItemText(8, _translate("MainWindow", "2° x 2°"))
        self.area_cb_2.setItemText(9, _translate("MainWindow", "2.5° x 2.5°"))
        self.area_cb_2.setItemText(10, _translate("MainWindow", "3° x 3°"))
        self.area_lb_5.setText(_translate("MainWindow", "Name of the file:"))
        self.area_lb_6.setText(_translate("MainWindow", "Format of the file:"))
        self.area_rb_1.setText(_translate("MainWindow", "Grib"))
        self.area_rb_2.setText(_translate("MainWindow", "NetCDF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), _translate("MainWindow", "Area and file"))
        self.download_bt_1.setText(_translate("MainWindow", "Download"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save..."))
        self.actionSave.setToolTip(_translate("MainWindow", "Save job in an XML file"))
        self.actionOpen.setText(_translate("MainWindow", "Open..."))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open an XML file containing a job"))
        self.actionExit.setText(_translate("MainWindow", "Exit..."))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit EMWF Data Downloader"))
        self.actionAbout.setText(_translate("MainWindow", "Prosim737 Updater..."))
        self.actionAbout.setToolTip(_translate("MainWindow", "About ECMWF Data Downloader"))
        self.actionChangelog.setText(_translate("MainWindow", "Changelog..."))
        self.actionChangelog.setToolTip(_translate("MainWindow", "Read the changelog"))
        self.actionSeparator1.setText(_translate("MainWindow", "separator1"))
        self.actionSeparator2.setText(_translate("MainWindow", "separator2"))
        self.actionSeparator2.setToolTip(_translate("MainWindow", "separator2"))
        self.actionSeparator3.setText(_translate("MainWindow", "separator3"))
        self.actionSeparator3.setToolTip(_translate("MainWindow", "separator3"))
        self.actionUpdate.setText(_translate("MainWindow", "Update..."))
        self.actionUpdate.setToolTip(_translate("MainWindow", "No update available !"))
        self.actionOptions.setText(_translate("MainWindow", "Options..."))
        self.actionOptions.setToolTip(_translate("MainWindow", "Click to modify EMCWF Data Downloader options"))

