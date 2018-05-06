import logging
import os
import tempfile
import time
from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from ui.Ui_mainwindow import Ui_MainWindow
from ui._version import _downloader_version, _eclipse_version, _py_version, _qt_version
from functions.window_functions import MyAbout, MyLog, MyOptions, MyUpdate, MySelect
from functions.material_functions import info_button_text, object_init, dataset_data_information
from functions.thread_functions import CheckECMWFDownloaderOnline
from functions.gui_functions import populate_period_elements, populate_fields, hide_area_map, set_visibility_area_map


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, config_dict, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.config_dict = config_dict
        self.config_path = path
        logging.info('mainwindow.py - UI initialization ...')
        self.setupUi(self)
        object_init(self)
        info_button_text(self)
        dataset_data_information(self)
        hide_area_map(self)
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.area_cb_1.setItemDelegate(itemDelegate)
        self.area_cb_2.setItemDelegate(itemDelegate)
        for widget in self.dataset_gb_1.buttons():
            widget.clicked.connect(lambda: populate_fields(self))
        self.time_rb_1.clicked.connect(lambda: populate_period_elements(self))
        self.time_rb_2.clicked.connect(lambda: populate_period_elements(self))
        self.area_cb_1.activated.connect(lambda: set_visibility_area_map(self))
        self.download_bt_1.clicked.connect(lambda: self.check_tabs_for_download())
        self.check_downloader_update()
        self.make_window_title()
        logging.info('mainwindow.py - UI initialized ...')
        logging.info('*****************************************')
        
    
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()
    
    @QtCore.pyqtSlot()
    def on_actionSave_triggered(self):
        print('Not available yet')
    
    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        print('Not available yet')
    
    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self):
        self.open_about()
        
    @QtCore.pyqtSlot()
    def on_actionChangelog_triggered(self):
        self.open_changelog()
        
    @QtCore.pyqtSlot()
    def on_actionOptions_triggered(self):
        self.open_options()
    
    @QtCore.pyqtSlot()
    def on_actionUpdate_triggered(self):
        self.download_and_install_downloader_update()
    
    def open_about(self):
        logging.debug('mainwindow.py - open_about')
        text = ("The ECMWF Data Downloader v" + _downloader_version + " was developed by Olivier Henry"
                + ", using Eclipse " + _eclipse_version + ", Python " + _py_version + " and PyQt "
                + _qt_version + ". It was designed to help researchers to download data from ECMWF dif"
                + "ferent projects by using the official web API. The API used in this program is "
                + "developed and maintained by ECMWF (https://software.ecmwf.int/wiki/display/WEBAPI/"
                + "Access+ECMWF+Public+Datasets), and its code has been integrated in a threaded "
                + "function.")

        self.aboutWindow = MyAbout(text)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.aboutWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.aboutWindow.setGeometry(x2, y2, w2, h2)
        self.aboutWindow.setMinimumSize(QtCore.QSize(560, 260))
        self.aboutWindow.setMaximumSize(QtCore.QSize(560, 360))
        self.aboutWindow.exec_()
    
    def open_changelog(self):
        logging.debug('mainwindow.py - open_changelog')
        self.logWindow = MyLog()
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.logWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.logWindow.setGeometry(x2, y2, w2, h2)
        self.logWindow.exec_()
    
    def open_options(self):
        logging.debug('mainwindow.py - open_options')
        self.optionWindow = MyOptions(self.config_dict, self.info_button_text_dict)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.optionWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.optionWindow.setGeometry(x2, y2, w2, h2)
        self.optionWindow.exec_()
        if not self.optionWindow.cancel:
            self.config_dict = self.optionWindow.config_dict
            with open(os.path.join(self.config_path, 'ecmwf_downloader.ini'), 'w') as config_file:
                self.config_dict.write(config_file)
            logging.getLogger().setLevel(self.config_dict.get('LOG', 'level'))
            self.check_downloader_update()

    def check_tabs_for_download(self):
        logging.debug('mainwindow.py - check_tabs_for_download')
        labels = self.findChildren(QtWidgets.QLabel)
        for label in labels:
            if label.isEnabled():
                label.setStyleSheet("color: black")
            
        for i in range(self.tabWidget.count()):
            self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))
        
        label_in_red = []
        tabs_in_red = []
        
        ### check datasets
        if self.dataset_gb_1.checkedButton() == None:
            label_in_red.append(self.dataset_lb_1)
            tabs_in_red.append(0)
        
        ### check fields
        if self.field_vertical_layout.count() == 0:
            tabs_in_red.append(0)
        else:
            if self.dataset_gb_2.checkedButton() == None:
                label_in_red.append(self.dataset_lb_2)
                tabs_in_red.append(0)
        
        ### check parameters
        param_checked = False
        if self.parameter_grid_layout.count() == 0:
            tabs_in_red.append(1)
        else:
            for widget in self.parameter_cb:
                if widget.isChecked():
                    param_checked = True
            if not param_checked:
                label_in_red.append(self.parameters_lb_1)
                tabs_in_red.append(1)
        
        ### check time period
        if param_checked:
            if self.time_lb_1.isEnabled() or self.time_lb_2.isEnabled() or self.time_lb_3.isEnabled():
                if self.time_lb_1.isEnabled():
                    time_checked = False
                    for widget in self.time_checkboxes_list:
                        if widget.isChecked():
                            time_checked = True
                if self.time_lb_2.isEnabled():
                    step_checked = False
                    for widget in self.step_checkboxes_list:
                        if widget.isChecked():
                            step_checked = True
                if self.time_lb_3.isEnabled():
                    period_checked = False
                    if self.time_rb_1.isChecked():
                        period_checked = True
                    elif self.time_rb_2.isChecked():
                        for widget in self.period_cb:
                            if widget.isChecked():
                                period_checked = True
                if not time_checked:
                    label_in_red.append(self.time_lb_1)
                    tabs_in_red.append(2)
                if not step_checked:
                    label_in_red.append(self.time_lb_2)
                    tabs_in_red.append(2)
                if not period_checked:
                    label_in_red.append(self.time_lb_3)
                    tabs_in_red.append(2)
        else:
            tabs_in_red.append(2)
        
        ### check area
        area_enabled = self.area_lb_1.isEnabled()
        if area_enabled and self.area_cb_1.currentText() == 'Custom':
            if self.area_ln_1.text() == '' or self.area_ln_2.text() == '' or self.area_ln_3.text() == '' or self.area_ln_4.text() == '':
                label_in_red.append(self.area_lb_1)
                tabs_in_red.append(3)
        elif not area_enabled:
            tabs_in_red.append(3)
        
        ### coloring labels and tabs
        for label in label_in_red:
            label.setStyleSheet("color: rgb(200,0,0);")
        for tab in tabs_in_red:
            self.tabWidget.tabBar().setTabTextColor(tab, QtGui.QColor(200,0,0))
        
        ### warning message
        if label_in_red or tabs_in_red:
            self.selectionWindow = MySelect()
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.selectionWindow.geometry().getRect()
            self.selectionWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
            self.selectionWindow.setMinimumSize(QtCore.QSize(500, self.selectionWindow.sizeHint().height()))
            self.selectionWindow.setMaximumSize(QtCore.QSize(500, self.selectionWindow.sizeHint().height()))
            self.selectionWindow.exec_()
            
    def closeEvent(self, event):
        logging.debug('mainwindow.py - closeEvent')
        self.close()


    def make_window_title(self):
        logging.debug('mainwindow.py - make_window_title - self.modified ' + str(self.modified))
        '''title_string = 'Prosim737 Updater v' + _updater_version
        saved_string = ''
        modified_string = ''
        if not self.saved:
            saved_string = ' - unsaved'
        if self.modified:
            modified_string = ' - modified'
        title_string = title_string + saved_string + modified_string
        self.setWindowTitle(title_string)'''

    def set_modified(self):
        logging.debug('mainwindow.py - set_modified')
        if not self.modified:
            self.modified = True
            self.make_window_title()

 
    def check_downloader_update(self):
        logging.debug('mainwindow.py - check_downloader_update')
        if self.config_dict['OPTIONS'].getboolean('check_update'):
            self.check_downloader = CheckECMWFDownloaderOnline()
            self.check_downloader.start()
            self.check_downloader.finished.connect(self.parse_downloader_update)
        else:
            self.actionUpdate.setEnabled(False)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/downloader_update_off_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionUpdate.setIcon(icon)
            self.actionUpdate.setToolTip('')
            logging.info('mainwindow.py - check_downloader_update - from options, no update check')
    
    def parse_downloader_update(self, val):
        logging.debug('mainwindow.py - parse_downloader_update - val ' + str(val))
        if val == 'no new version':
            self.actionUpdate.setEnabled(False)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/downloader_update_off_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionUpdate.setIcon(icon)
            self.actionUpdate.setToolTip('No update available !')
        elif 'http' in val:
            self.actionUpdate.setEnabled(True)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/downloader_update_on_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionUpdate.setIcon(icon)
            self.actionUpdate.setToolTip('A new update is available for ECMWF Data Downloader ! Click here to install it automatically.')
            self.link_latest_version = val
    
    def download_and_install_downloader_update(self):
        logging.debug('mainwindow.py - download_and_install_downloader_update - link_latest_version ' + str(self.link_latest_version))
        if self.link_latest_version:
            temp_folder = tempfile.gettempdir()
            self.downloadWindow = MyUpdate(self.link_latest_version, temp_folder)
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.downloadWindow.geometry().getRect()
            x2 = x1 + w1/2 - w2/2
            y2 = y1 + h1/2 - h2/2
            self.downloadWindow.setGeometry(x2, y2, w2, h2)
            self.downloadWindow.setMinimumSize(QtCore.QSize(500, self.downloadWindow.sizeHint().height()))
            self.downloadWindow.setMaximumSize(QtCore.QSize(500, self.downloadWindow.sizeHint().height()))
            self.downloadWindow.exec_()
            if not self.downloadWindow.cancel:
                os.startfile(temp_folder + '\\' + self.link_latest_version[self.link_latest_version.rfind('/')+1:])
                time.sleep(0.1)
                self.close()
    