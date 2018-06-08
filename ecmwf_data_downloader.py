import logging
import os
import sys
import configparser
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ui.mainwindow import MainWindow
from ui._version import _downloader_version


def launch_prosim_updater(path):
    app = QApplication(sys.argv)
    splash_pix = QPixmap('icons\downloader_update_off_icon.svg')
    splash = QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    config_dict = configparser.ConfigParser()
    if not os.path.exists(os.path.join(path, 'ecmwf_downloader.ini')):
        config_dict['LOG'] = {'level': 'DEBUG',
                              'path': ''
                              }
        config_dict['OPTIONS'] = {'language':'english',
                                  'check_update':'True',
                                  'display_api_info':'True'
                                  }
        config_dict['CREDENTIALS'] = {'url':'https://api.ecmwf.int/v1',
                                      'key':'',
                                      'email':'',
                                      'folder':''
                                      }
        with open(os.path.join(path, 'ecmwf_downloader.ini'), 'w') as configfile:
            config_dict.write(configfile)
    config_dict.read(os.path.join(path, 'ecmwf_downloader.ini'))
    if not config_dict['OPTIONS'].get('language'):
        config_dict.set('OPTIONS', 'language', 'english')
        with open(os.path.join(path, 'ecmwf_downloader.ini'), 'w') as configfile:
            config_dict.write(configfile)
    if not config_dict['CREDENTIALS'].get('folder'):
        config_dict.set('CREDENTIALS', 'folder', '')
        with open(os.path.join(path, 'ecmwf_downloader.ini'), 'w') as configfile:
            config_dict.write(configfile)
    path_exist = True
    if not config_dict.get('LOG', 'path'):
        log_filename = os.path.join(path, 'ecmwf_downloader_log.out')
    else:
        path_exist = os.path.isdir(config_dict.get('LOG', 'path'))
        if path_exist:
            log_filename = os.path.join(config_dict.get('LOG', 'path'),'ecmwf_downloader_log.out')
        else:
            log_filename = os.path.join(path, 'ecmwf_downloader_log.out')
    logging.getLogger('').handlers = []
    logging.basicConfig(filename = log_filename,
                        level = getattr(logging, config_dict.get('LOG', 'level')),
                        filemode = 'w',
                        format = '%(asctime)s : %(levelname)s : %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('*****************************************')
    logging.info('ECMWF Data Downloader ' + _downloader_version + ' is starting ...')
    logging.info('*****************************************')
    if not path_exist:
        logging.exception('ecmwf_data_downloader.py - exception occured when EDD tried to write log file in a non-default folder. Please check '
                          + 'that the folder exists. The path option in the config file is going to be modified to the default folder.')
        config_dict.set('LOG', 'path', '')
        with open(os.path.join(path, 'ecmwf_downloader.ini'), 'w') as configfile:
            config_dict.write(configfile)   
    ui = MainWindow(path, config_dict)
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    launch_prosim_updater(path)
    