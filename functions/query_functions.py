import logging
import calendar
from PyQt5 import QtCore


def prepare_query(self):
    logging.debug('query_functions.py - prepare_query')
    query = {}
    
    dataset_class, dataset, expver, stream, type, date, grid = None, None, '1', 'oper', None, None, None
    levtype, param, step, time, format, target, area = 'sfc', None, None, None, None, None, None
    
    dataset_gui = self.dataset_gb_1.checkedButton().text()
    field_gui = self.dataset_gb_2.checkedButton().text()
    
    ### dataset
    dataset = self.datasets_dict[dataset_gui]
    
    ### class
    dataset_class = self.classes_dict[dataset_gui]
    
    ### stream
    stream = self.fields_dict[field_gui]
    
    ### resolution
    grid = self.resolution_dic[self.area_cb_2.currentIndex()]
    
    ### format
    if self.file_bg_1.checkedButton().text() == 'NetCDF':
        format = 'netcdf'
        
    ### filename
    if self.area_ln_5.text():
        target = str(self.area_ln_5.text())
        if format == 'netcdf':
            if '.grib' in target:
                target = target[:-5] + '.nc'
            if '.nc' not in target:
                target += '.nc'
        else:
            if '.nc' in target:
                target = target[:-3] + '.grib'
            if '.grib' not in target:
                target += '.grib'
    else:
        if format == 'netcdf':
            target = 'output.nc'
        else:
            target = 'output.grib'
    
    ### area
    if self.area_cb_1.currentText() == 'Custom':
        north = self.area_ln_1.text()
        west = self.area_ln_2.text()
        east = self.area_ln_3.text()
        south = self.area_ln_4.text()
        area = north + '/' + west + '/' + south + '/' + east
    else:
        area = self.area_dict[self.area_cb_1.currentText()]
    
    ### period
    if self.period_bg_1.checkedButton().text() == 'From':
        date_from = self.time_de_1.date().toString(QtCore.Qt.ISODate)
        date_to = self.time_de_2.date().toString(QtCore.Qt.ISODate)
        date = date_from + '/to/' + date_to
    elif self.period_bg_1.checkedButton().text() == 'Or select a':
        if self.period_cb_1.currentText() == 'yearly period':
            date = ''
            for widget in self.period_cb:
                if widget.isChecked():
                    year = widget.objectName()[9:]
                    if self.dataset_information[dataset_gui]['fields'][field_gui]['step'] == 'daily':
                        if calendar.isleap(int(year)):
                            days = 366
                        else:
                            days = 365
                        for i in range(days):
                            if i < 9:
                                i = '00' + str(i + 1)
                            elif i < 99:
                                i = '0' + str(i + 1)
                            else:
                                i = str(i + 1)
                            date += year + '-' + i + '/'
                    else:
                        for i in range(12):
                            if i < 9:
                                i = '0' + str(i + 1)
                            else:
                                i = str(i + 1)
                            date += year + i + '01/'
            date = date[:-1]     
        else:
            date = ''
            for widget in self.period_cb:
                if widget.isChecked():
                    year = widget.objectName()[9:13]
                    month = widget.objectName()[14:]
                    if int(month) < 10:
                        month = '0' + month
                    _, days_number = calendar.monthrange(int(year), int(month))
                    for i in range(days_number):
                        if i < 9:
                            i = '0' + str(i + 1)
                        else:
                            i = str(i + 1)
                        date += year + month + i + '/'
            date = date[:-1]     

    ### parameters
    if self.checked_parameter:
        param =''
        parameters_dict = self.dataset_information[dataset_gui]['parameters'][field_gui]
        for item in self.checked_parameter:
            param += parameters_dict[item]['id'] + '/'
        param = param[:-1]
    
    ### time
    if self.time_bg_1.checkedButton():
        time = ''
        for widget in self.time_checkboxes_list:
            if widget.isChecked():
                time += widget.text() + '/'
        time = time[:-1]
    
    ### step
    if self.step_bg_1.checkedButton():
        step = ''
        for widget in self.step_checkboxes_list:
            if widget.isChecked():
                step += widget.text() + '/'
        step = step[:-1]
    
    ### type
    if self.step_bg_1.checkedButton():
        for widget in self.step_checkboxes_list:
            if widget.isChecked():
                type = self.type_dict[widget.text()]
    
    parameter_list = [dataset_class, dataset, expver, stream, type, date, grid, levtype, param, step, time, format, target, area]
    name_list = ['class', 'dataset', 'expver', 'stream', 'type', 'date', 'grid', 'levtype', 'param', 'step', 'time', 'format', 'target', 'area']
    
    for index, parameter in enumerate(parameter_list):
        if parameter != None:
            query[name_list[index]] = parameter
    
    logging.debug('query_functions.py - prepare_query - query ' + str(query))
    return query
    
    