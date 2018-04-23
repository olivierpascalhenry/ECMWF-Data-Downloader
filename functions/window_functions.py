import logging
import os
import time
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_aboutwindow import Ui_aboutWindow
from ui.Ui_logwindow import Ui_Changelog
from ui.Ui_optionwindow import Ui_optionWindow
from ui.Ui_storewindow import Ui_storeWindow
from functions.thread_functions import DownloadFile
from PyQt5 import QtWidgets, QtCore, QtGui


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, infoText):
        logging.debug('window_functions.py - MyInfo - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.iw_label_1.setText(infoText)
        self.iw_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        logging.debug('window_functions.py - MyInfo - closeWindow')
        self.close()


class MyAbout(QtWidgets.QDialog, Ui_aboutWindow):
    def __init__(self, text):
        logging.debug('window_functions.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.aw_label_1.setText(text)
        self.aw_okButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        logging.debug('window_functions.py - MyAbout - closeWindow')
        self.close()
        
        
class MyLog(QtWidgets.QDialog, Ui_Changelog):
    def __init__(self):
        logging.debug('window_functions.py - MyLog - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.lg_txBrower.setPlainText(open("documentation/changelog.txt").read())
        self.lg_okButton.clicked.connect(self.closeWindow)
        
    def closeWindow(self):
        logging.debug('window_functions.py - MyLog - closeWindow')
        self.close()
        

class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, config_dict, info_text):
        logging.debug('window_functions.py - MyOptions - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.config_dict = config_dict
        self.info_text = info_text
        itemDelegate = QtWidgets.QStyledItemDelegate()
        self.ow_comboBox_1.setItemDelegate(itemDelegate)
        self.ow_okButton.clicked.connect(self.save_and_close)
        self.ow_cancelButton.clicked.connect(self.close_window)
        self.ow_openButton_1.clicked.connect(self.get_directory)
        all_info_boxes = self.findChildren(QtWidgets.QToolButton,)
        for widget in all_info_boxes:
            if 'infoButton' in widget.objectName():
                widget.clicked.connect(lambda: self.info_button())
        self.cancel = True
        self.read_config_dict()
    
    def read_config_dict(self):
        logging.debug('window_functions.py - MyOptions - read_config_dict')
        log_level = self.config_dict.get('LOG', 'level')
        log_path = self.config_dict.get('LOG', 'path')
        check_update = self.config_dict['OPTIONS'].getboolean('check_update')
        display_api = self.config_dict['OPTIONS'].getboolean('display_api_info')
        url = self.config_dict.get('CREDENTIALS', 'url')
        key = self.config_dict.get('CREDENTIALS', 'key')
        email = self.config_dict.get('CREDENTIALS', 'email')
        self.ow_comboBox_1.setCurrentIndex(self.ow_comboBox_1.findText(log_level))
        self.ow_lineEdit_1.setText(log_path)
        self.ow_lineEdit_2.setText(url)
        self.ow_lineEdit_3.setText(key)
        self.ow_lineEdit_4.setText(email)
        self.ow_checkBox_1.setChecked(display_api)
        self.ow_checkBox_2.setChecked(check_update)
    
    def get_directory(self):
        logging.debug('window_functions.py - MyOptions - get_directory invoked')
        file_dialog = QtWidgets.QFileDialog()
        out_dir = file_dialog.getExistingDirectory(self, "Select Directory")
        self.ow_lineEdit_1.setText(str(out_dir.replace('/','\\')))
        logging.debug('window_functions.py - MyOptions - get_directory: ' + str(out_dir))
    
    def save_and_close(self):
        logging.debug('window_functions.py - MyOptions - save_and_close')
        self.cancel = False
        self.config_dict.set('LOG', 'level', str(self.ow_comboBox_1.currentText()))
        self.config_dict.set('LOG', 'path', str(self.ow_lineEdit_1.text()))
        self.config_dict.set('OPTIONS', 'check_update', str(self.ow_checkBox_2.isChecked()))
        self.config_dict.set('OPTIONS', 'display_api_info', str(self.ow_checkBox_1.isChecked()))
        self.config_dict.set('CREDENTIALS', 'url', str(self.ow_lineEdit_2.text()))
        self.config_dict.set('CREDENTIALS', 'key', str(self.ow_lineEdit_3.text()))
        self.config_dict.set('CREDENTIALS', 'email', str(self.ow_lineEdit_4.text()))
        
        
        self.close_window()
    
    def info_button(self):
        logging.debug('window_functions.py - MyOptions - info_button - self.sender().objectName() ' + self.sender().objectName())
        if 'infoButton' in self.sender().objectName():
            x = QtGui.QCursor.pos().x()
            y = QtGui.QCursor.pos().y()
            x = x - 175
            y = y + 50
            self.infoWindow = MyInfo(self.info_text[self.sender().objectName()])
            self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
            self.infoWindow.setGeometry(x, y, 450, self.infoWindow.sizeHint().height())
            self.infoWindow.exec_()
    
    def close_window(self):
        logging.debug('window_functions.py - MyOptions - closeWindow')
        self.close()


class MyUpdate(QtWidgets.QDialog, Ui_storeWindow):
    def __init__(self, url, folder):
        logging.debug('window_functions.py - MyUpdate - __init__')
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.temp_folder = folder
        self.url = url
        self.update_file = self.temp_folder + '\\' + self.url[self.url.rfind('/')+1:]
        self.sw_button.clicked.connect(self.cancel_download)
        self.cancel = False
        self.download_update()
    
    def update_progress_bar(self, val):
        if isinstance(val, list):
            self.progressBar.setValue(val[0])
            self.sw_label.setText(val[1])
        else:
            self.progressBar.setValue(val)
    
    def download_update(self):
        logging.debug('window_functions.py - MyUpdate - download_update')
        self.thread = DownloadFile(self.url, self.update_file)
        self.thread.download_update.connect(self.update_progress_bar)
        self.thread.download_done.connect(self.close)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()
    
    def cancel_download(self):
        logging.debug('window_functions.py - MyUpdate - cancel_download')
        self.thread.cancel_download()
        self.cancel = True
        time.sleep(0.25)
        self.close()
        
    def download_failed(self):
        logging.debug('window_functions.py - MyUpdate - download_failed')
        self.update_progress_bar(0)
        self.sw_label.setText('Download failed')
        self.cancel_download()
        
    def closeEvent(self, event):
        logging.debug('window_functions.py - MyUpdate - closeEvent')
        self.thread.download_update.disconnect(self.update_progress_bar)
        self.thread.stop()
        if self.cancel:
            os.remove(self.update_file)
