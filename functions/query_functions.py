import logging
from PyQt5 import QtCore


def prepare_query(self):
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
    if self.file_bg_1.checkedButton():
        format = self.file_bg_1.checkedButton().text().lower()
        
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
    elif self.period_bg_1.checkedButton().text() == 'Or':
        pass
    
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
        
    return query
    
    