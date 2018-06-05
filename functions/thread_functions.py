import logging
import requests
import time
import json
import os
import platform
import sys
from urllib.request import urlopen
from hurry.filesize import size, alternative
from PyQt5 import QtCore, Qt
from distutils.version import LooseVersion
from ui._version import _downloader_version
from PyQt5 import QtWidgets

        
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
            format = ''
            if getattr(sys, 'frozen', False) :
                if platform.system() == 'Windows':
                    format = '.msi'
                elif platform.system() == 'Linux':
                    format = '.tar.gz'
            else:
                format = 'sources.zip'
                
            if LooseVersion(_downloader_version) < LooseVersion(json_object['tag_name']):
                assets = json_object['assets']
                download_url = 'no new version'
                for asset in assets:
                    link = asset['browser_download_url']
                    if format in link:
                        download_url = link  
                self.finished.emit(download_url)
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
        self.filename = self.url_name[self.url_name.rfind("/")+1:]
        self.cancel = False
        
    def run(self):
        logging.debug('thread_functions.py - DownloadFile - run - download started')
        if len(self.filename) > 35:
            if platform.system() == 'Windows':
                self.filename = self.filename[:21] + '[...]' + self.filename[-4:]
            elif platform.system() == 'Linux':
                self.filename = self.filename[:21] + '[...]' + self.filename[-7:]
            
        self.download_update.emit([0, 'Downloading %s...' % self.filename])
        opened_file = open(self.update_file, 'wb')
        try:
            opened_url = urlopen(self.url_name, timeout=10)
            totalFileSize = int(opened_url.info()['Content-Length'])
            bufferSize = 9192
            fileSize = 0
            start = time.time()
            while True:
                if self.cancel:
                    opened_file.close()
                    break
                buffer = opened_url.read(bufferSize)
                if not buffer:
                    break
                fileSize += len(buffer)
                opened_file.write(buffer)
                download_speed = self.set_size(fileSize/(time.time() - start)) + '/s'
                self.download_update.emit([round(fileSize * 100 / totalFileSize), 'Downloading %s at %s' % (self.filename, download_speed)])
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
    
    def set_size(self, bytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while bytes >= 1024 and i < len(suffixes)-1:
            bytes /= 1024.
            i += 1
        f = ('%.2f' % bytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])
    
    def cancel_download(self):
        logging.debug('thread_functions.py - DownloadFile - cancel_download')
        self.cancel = True
    
    def stop(self):
        logging.debug('thread_functions.py - DownloadFile - stop')
        self.terminate()
        
        
class ECMWFDataDownloadThread(Qt.QThread):
    download_update = QtCore.pyqtSignal(dict)
    download_done = QtCore.pyqtSignal()
    download_failed = QtCore.pyqtSignal(str)
    
    def __init__(self, query, api_url, api_key, api_email, path):
        Qt.QThread.__init__(self)
        logging.debug('thread_functions.py - ECMWFDataDownloadThread - __init__')
        self.query = query
        self.api_url = api_url
        self.api_key = api_key
        self.api_email = api_email
        self.filename = query['target']
        self.path = path + '\\'
        self.error = ''
        self.cancel = False
        self.downloading = False
        
    def run(self):
        logging.debug('thread_functions.py - ECMWFDataDownloadThread - run')
        headers_get = {'Accept':'application/json',
                       'From':self.api_email,
                       'X-ECMWF-KEY':self.api_key}
        headers_post = {'Accept':'application/json',
                        'From':self.api_email,
                        'X-ECMWF-KEY':self.api_key,
                        'Content-Type': 'application/json'}
        check_url = self.api_url + '/who-am-i'
        news_url = self.api_url + '/datasets/' + self.query['dataset'] + '/news'
        query_url = self.api_url + '/datasets/' + self.query['dataset'] + '/requests?offset=0&limit=500'
        try:
            check_res = requests.get(check_url, headers=headers_get)  
            status_code = check_res.status_code
            logging.debug('thread_functions.py - ECMWFDataDownloadThread - run - connection check - status code ' + str(status_code))
            if status_code == 200:
                full_name = check_res.json()['full_name']
                email = check_res.json()['full_name']
                    
                text = ('Welcome ' + full_name + '.<br>Testing the connection to the ECMWF API ... OK.<br>')
                self.download_update.emit({'browser_text':text,
                                           'bar_text':'Testing...',
                                           'progress':0})
            else:
                try:
                    self.error = str(check_res.json()['error'])
                except KeyError:
                    self.error = 'No error message'
                logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - check - Exception - status code '
                                  + str(status_code) + ' ; error ' + self.error)
                raise Exception
            news_res = requests.get(news_url, headers=headers_get)
            status_code = news_res.status_code
            if status_code == 200:
                news = news_res.json()['news'] + '<br>'
                self.download_update.emit({'browser_text':news,
                                           'bar_text':'Announcing...',
                                           'progress':0})
            else:
                try:
                    self.error = str(news_res.json()['error'])
                except KeyError:
                    self.error = 'No error message'
                logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - news - Exception - status code '
                                  + str(status_code) + ' ; error ' + self.error)
                raise Exception
            data = json.dumps(self.query).encode('utf-8')
            submit_res = requests.post(url=query_url, data=data, headers=headers_post)
            status_code = submit_res.status_code
            if status_code == 202:
                text = ('Request is now submitted.<br>Depending on the server load and the complexity of the query, '
                        + 'the processing of the request can take some time.<br>')
                self.download_update.emit({'browser_text':text,
                                           'bar_text':'Submitting...',
                                           'progress':0})
                retry = int(submit_res.headers['Retry-After'])
                location = submit_res.headers['Location']
                token = submit_res.json()['name']
                if 'messages' in submit_res.json():
                    for n in submit_res.json()["messages"]:
                        print(n)
                query_res = requests.get(url=location, headers=headers_get)
                status_code = query_res.status_code
                if status_code == 202:
                    text = 'Request ID ' + str(token) + ' is now queued. Please wait...<br>'
                    self.download_update.emit({'browser_text':text,
                                           'bar_text':'Queued...',
                                           'progress':0})
                    status = query_res.json()['status']
                    retry = int(query_res.headers['Retry-After'])
                    while status_code == 202:
                        time.sleep(retry)
                        query_res = requests.get(url=location, headers=headers_get, allow_redirects=False)
                        status_code = query_res.status_code
                        if status_code >= 400:
                            try:
                                self.error = str(query_res.json()['error'])
                            except KeyError:
                                self.error = 'No error message'
                            logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - queued - Exception'
                                                + ' - status code ' + str(status_code) + ' ; error ' + self.error)
                            raise Exception
                    final_res = requests.get(location, headers=headers_get, stream=True)
                    status_code = final_res.status_code
                    if status_code == 200:
                        with open(self.path + self.filename, 'wb') as f:
                            text = 'The processing of the query is finished and the file is ready to be downloaded.<br>'
                            self.download_update.emit({'browser_text':text,
                                                       'bar_text':'Ready to download...',
                                                       'progress':0})
                            start = time.time()
                            total_length = int(final_res.headers.get('content-length'))
                            downloaded = 0
                            self.download_update.emit({'browser_text':'Downloading...',
                                                       'bar_text':'Downloading...',
                                                       'progress':0})
                            self.downloading = True
                            for chunk in final_res.iter_content(chunk_size=1024):
                                if self.cancel:
                                    break
                                downloaded += len(chunk)
                                f.write(chunk)
                                try:
                                    download_speed = self.set_size(downloaded/(time.time() - start)) + '/s'
                                except ZeroDivisionError:
                                    download_speed= '0 KB/s'
                                progress = round(downloaded * 100 / total_length)
                                bar_text = 'Downloading at ' + download_speed
                                self.download_update.emit({'browser_text':'',
                                                           'bar_text':bar_text,
                                                           'progress':progress})
                        f.close()
                        requests.delete(location, headers=headers_get)
                        if self.cancel:
                            self.download_cancel.emit()
                            try:
                                os.remove(self.path + self.filename)
                            except Exception:
                                logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - Trying to remove aborted file')
                        else:
                            self.download_done.emit()
                    else:
                        try:
                            self.error = str(final_res.json()['error'])
                        except KeyError:
                            self.error = 'No error message'
                        logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - final - Exception'
                                              + ' - status code ' + str(status_code) + ' ; error ' + self.error)
                        raise Exception
                else:
                    try:
                        self.error = str(query_res.json()['error'])
                    except KeyError:
                        self.error = 'No error message'
                    logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - query - Exception'
                                      + ' - status code ' + str(status_code) + ' ; error ' + self.error)
                    raise Exception  
            else:
                try:
                    self.error = str(submit_res.json()['error'])
                except KeyError:
                    self.error = 'No error message'
                logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - submission - Exception - status code '
                                  + str(status_code) + ' ; error ' + self.error)
                raise Exception
        except Exception:
            logging.exception('thread_functions.py - ECMWFDataDownloadThread - run - Exception')
            self.download_failed.emit(self.error)
    
    def set_size(self, bytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while bytes >= 1024 and i < len(suffixes)-1:
            bytes /= 1024.
            i += 1
        f = ('%.2f' % bytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])
    
    def cancel_download(self):
        logging.debug('thread_functions.py - ECMWFDataDownloadThread - cancel_download')
        self.cancel = True
    
    def stop(self):
        logging.debug('thread_functions.py - ECMWFDataDownloadThread - stop')
        self.terminate()

