import logging
import os
import tempfile
import time
import platform
import webbrowser
from PyQt5 import QtCore, QtWidgets, QtGui
from ui.Ui_mainwindow import Ui_MainWindow
from ui._version import _downloader_version, _eclipse_version, _py_version, _qt_version
from functions.window_functions import MyAbout, MyLog, MyOptions, MyUpdate, MySelect, MyQuery
from functions.material_functions import info_button_text, object_init, dataset_data_information
from functions.thread_functions import CheckECMWFDownloaderOnline
from functions.gui_functions import populate_period_elements, populate_fields, hide_area_map, set_visibility_area_map, clean_stylesheet_labels
from functions.gui_functions import clean_stylesheet_dataset, clean_stylesheet_time, clean_stylesheet_step, clean_stylesheet_period
from functions.checking_functions import tabs_checking
from functions.xml_functions import save_xml_query, open_xml_query
from functions.query_functions import prepare_query


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
            widget.toggled.connect(lambda: populate_fields(self))
            widget.toggled.connect(lambda: clean_stylesheet_dataset(self))
        for widget in self.time_bg_1.buttons():
            widget.toggled.connect(lambda: clean_stylesheet_time(self))
            widget.toggled.connect(self.set_modified)
        for widget in self.step_bg_1.buttons():
            widget.toggled.connect(lambda: clean_stylesheet_step(self))
            widget.toggled.connect(self.set_modified)
        for widget in self.period_bg_1.buttons():
            widget.toggled.connect(lambda: populate_period_elements(self))
            widget.toggled.connect(lambda: clean_stylesheet_period(self))
            widget.toggled.connect(self.set_modified)
        for widget in self.file_bg_1.buttons():
            widget.toggled.connect(self.set_modified)
        self.area_cb_1.currentIndexChanged.connect(lambda: set_visibility_area_map(self))
        self.area_cb_1.currentIndexChanged.connect(self.set_modified)
        self.area_cb_2.currentIndexChanged.connect(self.set_modified)
        self.area_ln_5.textChanged.connect(self.set_modified)
        self.time_de_1.dateChanged.connect(self.set_modified)
        self.time_de_2.dateChanged.connect(self.set_modified)
        self.download_bt_1.clicked.connect(self.check_tabs_for_download)
        
        #self.download_bt_1.clicked.connect(self.download_ecmwf_data)
        
        self.check_downloader_update()
        self.make_window_title()
        logging.info('mainwindow.py - UI initialized ...')
        logging.info('*****************************************')
        
    
    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        self.close()
    
    @QtCore.pyqtSlot()
    def on_actionSave_triggered(self):
        self.save_document()
    
    @QtCore.pyqtSlot()
    def on_actionOpen_triggered(self):
        self.open_document()
    
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
                + "ferent projects by using the official ECMWF web API.")
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
    
    def save_document(self):
        logging.debug('mainwindow.py - save_document')
        filename = self.get_file_name('save')
        if filename:
            save_xml_query(self, filename)
    
    def open_document(self):
        logging.debug('mainwindow.py - open_document')
        filename = self.get_file_name('open')
        if filename:
            open_xml_query(self, filename)
    
    def check_tabs_for_download(self):
        logging.debug('mainwindow.py - check_tabs_for_download')
        checking_passed = tabs_checking(self)
        if not checking_passed:
            self.selectionWindow = MySelect()
            x1, y1, w1, h1 = self.geometry().getRect()
            _, _, w2, h2 = self.selectionWindow.geometry().getRect()
            self.selectionWindow.setGeometry(x1 + w1/2 - w2/2, y1 + h1/2 - h2/2, w2, h2)
            self.selectionWindow.setMinimumSize(QtCore.QSize(500, self.selectionWindow.sizeHint().height()))
            self.selectionWindow.setMaximumSize(QtCore.QSize(500, self.selectionWindow.sizeHint().height()))
            self.selectionWindow.exec_()
        else:
            self.download_ecmwf_data()
    
    def download_ecmwf_data(self):
        logging.debug('mainwindow.py - download_ecmwf_data')
        self.query =  prepare_query(self)
        logging.debug('mainwindow.py - download_ecmwf_data - query: ' + str(self.query))
        self.queryWindow = MyQuery(self.query, self.config_dict)
        x1, y1, w1, h1 = self.geometry().getRect()
        _, _, w2, h2 = self.queryWindow.geometry().getRect()
        x2 = x1 + w1/2 - w2/2
        y2 = y1 + h1/2 - h2/2
        self.queryWindow.setGeometry(x2, y2, w2, h2)
        self.queryWindow.exec_()
    
    def closeEvent(self, event):
        logging.debug('mainwindow.py - closeEvent')
        self.close()

    def make_window_title(self):
        logging.debug('mainwindow.py - make_window_title - self.modified ' + str(self.modified))
        title_string = 'ECMWF Data Downloader v' + _downloader_version
        modified_string = ''
        if self.modified:
            modified_string = ' - modified'
        title_string = title_string + modified_string
        self.setWindowTitle(title_string)

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
            if platform.system() == 'Windows':
                self.actionUpdate.setToolTip('A new update is available for ECMWF Data Downloader ! Click here to install it automatically.')
            elif platform.system() == 'Linux':
                self.actionUpdate.setToolTip('A new update is available for ECMWF Data Downloader ! Click here to download it.')
            self.link_latest_version = val
    
    def download_and_install_downloader_update(self):
        logging.debug('mainwindow.py - download_and_install_downloader_update - link_latest_version ' + str(self.link_latest_version))
        if self.link_latest_version:
            if platform.system() == 'Windows':
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
            elif platform.system() == 'Linux':
                webbrowser.open(self.link_latest_version)
    
    def get_file_name(self, action):
        logging.debug('mainwindow.py - get_file_name')
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setDefaultSuffix('xml')
        if action == 'save':
            file_name, _ = file_dialog.getSaveFileName(self, 'Save XML File', '', filter='XML Files (*.xml)')
        elif action == 'open':
            file_name, _ = file_dialog.getOpenFileName(self, 'Open XML File', '', filter='XML Files (*.xml)')
        logging.debug('mainwindow.py - get_file_name - file_name ' + file_name)
        return file_name
    