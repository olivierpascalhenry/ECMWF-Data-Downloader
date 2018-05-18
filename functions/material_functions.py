import logging
from database.parameters_dictionary_creation import init_parameter_database
from PyQt5 import QtWidgets


def object_init(self):
    logging.debug('material_functions.py - object_init')
    self.modified = False
    self.time_times_visible = True
    self.time_steps_visible = True
    self.dataset_gb_2 = QtWidgets.QButtonGroup()
    self.dataset_gb_2.setObjectName('dataset_gb_2')
    self.time_activation = False
    self.time_checkboxes_list = [self.time_cb_1,self.time_cb_2,self.time_cb_3,self.time_cb_4]
    self.step_checkboxes_list = [self.time_cb_5,self.time_cb_6,self.time_cb_7,self.time_cb_8,self.time_cb_9]
    self.time_tab_status = True
    self.period_cb = []
    self.field_rb = []
    self.parameter_cb = []
    self.checked_parameter = []


def info_button_text(self):
    logging.debug('material_functions.py - info_button_text')
    self.info_button_text_dict = {'ow_infoButton_1':('You can change here the verbose level of the logging system. If an issue is '
                                                     + 'noticed, it is a good idea to change the level to DEBUG and send the log '
                                                     + 'file to the developer.'),
                                  'ow_infoButton_2':('The path where to save the log file, for those who appreciate to keep all '
                                                     + 'their logs at the same place. A reboot of the software is necessary if the '
                                                     + 'location of the log file is changed.'),
                                  'ow_infoButton_3':'The URL of the API should be entered here.',
                                  'ow_infoButton_4':('A personal key, provided by ECMWF, is required to use the web API. For more'
                                                     + ' information and to obtain your key, please click on the following link: '
                                                     + ' <a href=https://software.ecmwf.int/wiki/display/WEBAPI/Access+ECMWF+Publ'
                                                     + 'ic+Datasets#AccessECMWFPublicDatasets-key>https://software.ecmwf.int/wiki'
                                                     + '/display/WEBAPI/Access+ECMWF+Public+Datasets #AccessECMWFPublicDatasets-key</a>'),
                                  'ow_infoButton_5':'The user email address is required to use the web API.',
                                  'ow_infoButton_6':('If checked, ECMWF Data Downloader displays information about the ECMWF web API '
                                                     + 'at startup.'),
                                  'ow_infoButton_7':'Activate this option to allow ECMWF Data Downloader to check for an update online.',
                                  'ow_infoButton_8':'A folder where to save the file/data downloaded on ECMWF server.',
                                  }


def dataset_data_information(self):
    logging.debug('material_functions.py - dataset_data_information')
    (era_interim_daily_parameters, era_interim_invariant_parameters, era_interim_synoptic_parameters,
     era_interim_daily_means_parameters, era_interim_daily_accumulation_parameters) = init_parameter_database()
     
    self.dataset_information = {'CERA-20C':{},
                                'CERA-SAT':{},
                                'ERA5':{},
                                'ERA-15':{},
                                'ERA-20C':{},
                                'ERA-20CM':{},
                                'ERA-40':{},
                                'ERA-Interim':{'fields':{'Daily':{'start':'1979-01','end':'now','step':'month'},
                                                         'Invariant':{},
                                                         'Synoptic Monthly Means':{'start':'1979-01','end':'now','step':'year'},
                                                         'Monthly Means of Daily Means':{'start':'1979-01','end':'now','step':'year'},
                                                         'Monthly Means of Daily Forecast Accumulations':{'start':'1979-01','end':'now','step':'year'}},
                                               'steps':{'Daily':['0','3','6','9','12'],
                                                        'Invariant':[],
                                                        'Synoptic Monthly Means':['0','3','6','9','12'],
                                                        'Monthly Means of Daily Means':[],
                                                        'Monthly Means of Daily Forecast Accumulations':['0-12','12-24','24-36']},
                                               'times':{'Daily':{'00:00:00':{'0':True,'3':True,'6':True,'9':True,'12':True},
                                                                 '06:00:00':{'0':True,'3':False,'6':False,'9':False,'12':False},
                                                                 '12:00:00':{'0':True,'3':True,'6':True,'9':True,'12':True},
                                                                 '18:00:00':{'0':True,'3':False,'6':False,'9':False,'12':False}},
                                                                 'Invariant':{},
                                                                 'Synoptic Monthly Means':{'00:00:00':{'0':True,'3':True,'6':True,'9':True,'12':True},
                                                                                           '06:00:00':{'0':True,'3':False,'6':False,'9':False,'12':False},
                                                                                           '12:00:00':{'0':True,'3':True,'6':True,'9':True,'12':True},
                                                                                           '18:00:00':{'0':True,'3':False,'6':False,'9':False,'12':False}},
                                                                 'Monthly Means of Daily Means':{},
                                                                 'Monthly Means of Daily Forecast Accumulations':{}},
                                               'parameters':{'Daily':era_interim_daily_parameters,
                                                             'Invariant':era_interim_invariant_parameters,
                                                             'Synoptic Monthly Means':era_interim_synoptic_parameters,
                                                             'Monthly Means of Daily Means':era_interim_daily_means_parameters,
                                                             'Monthly Means of Daily Forecast Accumulations':era_interim_daily_accumulation_parameters}},
                                'ERA-Interim/LAND':{}}
    
    
    
    self.classes_dict = {'ERA-Interim':'ei',
                       'ERA-Interim/LAND':'ei',
                       'ERA-15':'er',
                       'ERA-40':'e4',
                       'ERA5':'ea',
                       'ERA-20C':'e2',
                       'ERA-20CM':'em',
                       'CERA-20C':'ep',
                       'CERA-SAT':'et'}
    
    self.datasets_dict = {'ERA-Interim':'interim',
                         'ERA-Interim/LAND':'interim_land',
                         'ERA-15':'era15',
                         'ERA-40':'era40',
                         'ERA5':'era5',
                         'ERA-20C':'era20c',
                         'ERA-20CM':'era20cm',
                         'CERA-20C':'cera20c',
                         'CERA-SAT':'cera_sat'}
        
    self.fields_dict = {'Daily':'oper',
                        'Invariant':'oper',
                        'Synoptic Monthly Means':'mnth',
                        'Monthly Means of Daily Means':'moda',
                        'Monthly Means of Daily Forecast Accumulations':'mdfa'}
    
    self.resolution_dic = ['0.125/0.125','0.25/0.25','0.4/0.4','0.5/0.5','0.75/0.75','1/1','1.125/1.125','1.5/1.5','2/2','2.5/2.5','3/3']
    
    self.area_dict = {'Default (as archived)':None, #North/West/South/East
                      'South Asia':'30/60/0/120',
                      'Europe':'75/-20/10/60',
                      'Indonesia':'5/100/-10/150',
                      'Inter-tropical band':'30/0/-30/360',
                      'North America':'70/-130/30/-60',
                      'Northern Hemisphere':'87.5/0/30/360',
                      'Southern Hemisphere':'-30/0/-87.5/360',
                      'Tropical Pacific':'10/160/-10/260'}
    
    self.type_dict = {'0':'an',
                      '3':'fc',
                      '6':'fc',
                      '9':'fc',
                      '12':'fc'}
    
    
    
    
    '''00:00:00 :  0 : an
            3 : fc
            6 : fc
            9 : fc
            12 : fc

    06:00:00 :  0 : an 
            3 : /
            6 : /
            9 : /
            12 : /

    12:00:00 :  0 : an
            3 : fc
            6 : fc
            9 : fc
            12 : fc

    18:00:00 :  0 : an
            3 : /
            6 : /
            9 : /
            12 : /'''
    
    