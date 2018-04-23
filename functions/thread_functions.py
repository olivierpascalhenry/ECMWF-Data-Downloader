import logging
import requests
import time
from urllib.request import urlopen
from hurry.filesize import size, alternative
from PyQt5 import QtCore, Qt
from distutils.version import LooseVersion
from ui._version import _downloader_version

        
class CheckECMWFDownloaderOnline(Qt.QThread):
    finished = QtCore.pyqtSignal(str)
    
    def __init__(self):
        Qt.QThread.__init__(self)
        logging.debug('thread_functions.py - CheckECMWFDownloaderOnline - __init__')
    
    def run(self):
        logging.debug('thread_functions.py - CheckECMWFDownloaderOnline - run')
        url = 'https://api.github.com/repos/olivierpascalhenry/ECMWF-Data-Downloader/releases/latest'
        try:
            json_object = requests.get(url=url).json() 
            if LooseVersion(_downloader_version) < LooseVersion(json_object['tag_name']):
                self.finished.emit(json_object['assets'][0]['browser_download_url'])
            else:
                self.finished.emit('no new version')
        except Exception:
            logging.exception('thread_functions.py - CheckECMWFDownloaderOnline - run - internet connection error - url ' + url)
    
    def stop(self):
        self.terminate()
        
        
class DownloadFile(Qt.QThread):
    download_update = QtCore.pyqtSignal(list)
    download_done = QtCore.pyqtSignal()
    download_failed = QtCore.pyqtSignal()
    def __init__(self, url_name, update_file=None):
        Qt.QThread.__init__(self)
        logging.debug('thread_functions.py - DownloadFile - __init__ - url_name ' + str(url_name)
                      + ' ; update_file ' + str(update_file))
        self.url_name = url_name
        self.update_file = update_file
        self.cancel = False
        
    def run(self):
        logging.debug('thread_functions.py - DownloadFile - run - download started')
        self.download_update.emit([0, 'Downloading %s...' % self.url_name[self.url_name.rfind("/")+1:]])
        opened_file = open(self.update_file, 'wb')
        try:
            opened_url = urlopen(self.url_name, timeout=10)
            totalFileSize = int(opened_url.info()['Content-Length'])
            bufferSize = 9192
            fileSize = 0
            start = time.clock()
            while True:
                if self.cancel:
                    opened_file.close()
                    break
                buffer = opened_url.read(bufferSize)
                if not buffer:
                    break
                fileSize += len(buffer)
                opened_file.write(buffer)
                download_speed = size(fileSize/(time.clock() - start), system=alternative) + '/s'
                self.download_update.emit([round(fileSize * 100 / totalFileSize), 'Downloading %s at %s' % (self.url_name[self.url_name.rfind("/")+1:], download_speed)])
            opened_file.close()
            if not self.cancel:
                logging.debug('thread_functions.py - DownloadFile - run - download finished')
                self.download_done.emit()
            else:
                logging.debug('thread_functions.py - DownloadFile - run - download canceled')
        except Exception:
            logging.exception('thread_functions.py - DownloadFile - run - connexion issue ; self.url_name ' + self.url_name)
            opened_file.close()
            self.download_failed.emit()
            
    
    def cancel_download(self):
        logging.debug('thread_functions.py - DownloadFile - cancel_download')
        self.cancel = True
    
    def stop(self):
        logging.debug('thread_functions.py - DownloadFile - stop')
        self.terminate()
    