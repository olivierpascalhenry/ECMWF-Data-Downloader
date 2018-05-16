import logging
import xml.dom.minidom
import datetime
from PyQt5 import QtGui, QtCore
from functions.gui_functions import populate_fields

NAMESPACE_URI = 'ECMWFDataDownloader'

def save_xml_query(self, out_file_name):
    logging.info('xml_functions.py - save_xml_query - starting ...')
    doc = xml.dom.minidom.Document()
    doc_root = add_element(doc, "DownloaderQuery", doc)
    doc_root.setAttribute("xmlns:downloader", NAMESPACE_URI)
    add_element(doc, "CreationDate", doc_root, datetime.date.isoformat(datetime.date.today()))
    
    
    ############################
    # dataset and fields
    ############################
    dataset_field = add_element(doc, "DatasetsFields", doc_root)
    button = self.dataset_gb_1.checkedButton()
    if button:
        add_element(doc, "Dataset", dataset_field, button.text())
    else:
        add_element(doc, "Dataset", dataset_field, '')
    button = self.dataset_gb_2.checkedButton()
    if button:
        add_element(doc, "Field", dataset_field, button.text())
    else:
        add_element(doc, "Field", dataset_field, '')
    
    
    ############################
    # parameters
    ############################
    parameters = add_element(doc, "Parameters", doc_root)
    for parameter in self.parameter_cb:
        if parameter.isChecked():
            add_element(doc, "Parameter", parameters, parameter.text())
    
    
    ############################
    # time period
    ############################
    time_period = add_element(doc, "TimePeriod", doc_root)
    times = add_element(doc, "Times", time_period)
    for widget in self.time_checkboxes_list:
        if widget.isChecked():
            add_element(doc, "Time", times, widget.text())
    steps = add_element(doc, "Steps", time_period)
    for widget in self.step_checkboxes_list:
        if widget.isChecked():
            add_element(doc, "Step", steps, widget.text())
    period = add_element(doc, "Period", time_period)
    button = self.period_bg_1.checkedButton()
    if button:
        if button.text() == 'From':
            add_element(doc, "From", period, self.time_de_1.date().toString(QtCore.Qt.ISODate))
            add_element(doc, "To", period, self.time_de_2.date().toString(QtCore.Qt.ISODate))
        elif button.text() == 'Or':
            for widget in self.period_cb:
                if widget.isChecked():
                    year = widget.objectName()[9:13]
                    month = widget.objectName()[14:]
                    if month:
                        add_element(doc, "Year-Month", period, str(year) + '-' + str(month))
                    else:
                        add_element(doc, "Year", period, str(year))
    
    
    ############################
    # area and file
    ############################
    area_file = add_element(doc, "AreaFile", doc_root)
    area = self.area_cb_1.currentText()
    if area == 'Custom':
         area = add_element(doc, "Area", area_file)
         add_element(doc, "North", area, self.area_ln_1.text())
         add_element(doc, "South", area, self.area_ln_4.text())
         add_element(doc, "East", area, self.area_ln_3.text())
         add_element(doc, "West", area, self.area_ln_2.text())
    else:
        add_element(doc, "Area", area_file, area)
    add_element(doc, "Resolution", area_file, self.area_cb_2.currentText())
    add_element(doc, "Filename", area_file, self.area_ln_5.text())
    button = self.file_bg_1.checkedButton()
    if button:
        add_element(doc, "Format", area_file, button.text())
    else:
        add_element(doc, "Format", area_file, '')
    
    
    ############################
    # File Creation
    ############################
    logging.debug('xml_functions.py - save_xml_query - file creation ...')
    f = open(out_file_name, 'w')
    f.write(doc.toprettyxml())
    f.close()
    self.modified = False
    self.make_window_title()
    logging.info('xml_functions.py - save_xml_query - xml file successfully created')
    
    
def open_xml_query(self, file_name):
    logging.info('xml_functions.py - open_xml_query - starting ...')
    f = open(file_name, 'r')
    doc = xml.dom.minidom.parse(f)
    
    
    ############################
    # dataset and fields
    ############################
    index = self.tabWidget.currentIndex()
    datasets_fields = get_element(doc, "DatasetsFields")
    dataset = get_element_value(datasets_fields, 'Dataset')
    for button in self.dataset_gb_1.buttons():
        if button.text() == dataset:
            button.setChecked(True)
    field = get_element_value(datasets_fields, 'Field')
    for button in self.dataset_gb_2.buttons():
        if button.text() == field:
            button.setChecked(True)
    self.tabWidget.setCurrentIndex(index)
    
    
    ############################
    # parameters
    ############################
    index = self.tabWidget.currentIndex()
    parameters = get_element(doc, "Parameters")
    parameter_list = get_element_values(parameters, 'Parameter')
    for widget in self.parameter_cb:
        if widget.text() in parameter_list:
            widget.setChecked(True)
    self.tabWidget.setCurrentIndex(index)
    

    ############################
    # time period
    ############################
    times = get_element(get_element(doc, "TimePeriod"), "Times")
    time_list = get_element_values(times, 'Time')
    for widget in self.time_checkboxes_list:
        if widget.text() in time_list:
            widget.setChecked(True)
    steps = get_element(get_element(doc, "TimePeriod"), "Steps")
    step_list = get_element_values(steps, 'Step')
    for widget in self.step_checkboxes_list:
        if widget.text() in step_list:
            widget.setChecked(True)
    period = get_element(get_element(doc, "TimePeriod"), "Period")
    if get_element_value(period, 'Year-Month'):
        tmp = get_element_values(period, 'Year-Month')
        year_month_list = []
        for item in tmp:
            year_month_list.append('checkbox_' + item[:4] + '_' + item[5:])
        index = self.tabWidget.currentIndex()
        self.tabWidget.setCurrentIndex(2)
        self.time_rb_2.setChecked(True)
        for widget in self.period_cb:
            if widget.objectName() in year_month_list:
                widget.setChecked(True)
        self.tabWidget.setCurrentIndex(index)
    elif get_element_value(period, 'Year'):
        tmp = get_element_values(period, 'Year')
        year_list = []
        for item in tmp:
            year_list.append('checkbox_' + item)
        index = self.tabWidget.currentIndex()
        self.tabWidget.setCurrentIndex(2)
        self.time_rb_2.setChecked(True)
        for widget in self.period_cb:
            if widget.objectName() in year_list:
                widget.setChecked(True)
        self.tabWidget.setCurrentIndex(index)
    elif get_element_value(period, 'From'):
        self.time_rb_1.setChecked(True)
        period_from = get_element_value(period, 'From')
        period_to = get_element_value(period, 'To')
        self.time_de_1.setDate(QtCore.QDate.fromString(period_from, QtCore.Qt.ISODate))
        self.time_de_2.setDate(QtCore.QDate.fromString(period_to, QtCore.Qt.ISODate))
    

    ############################
    # area and file
    ############################
    area_file = get_element(doc, "AreaFile")
    if get_element_value(area_file, "Area"):
        area = get_element_value(area_file, "Area")
        self.area_cb_1.setCurrentIndex(self.area_cb_1.findText(area))
    else:
        index = self.tabWidget.currentIndex()
        self.tabWidget.setCurrentIndex(3)
        self.area_cb_1.setCurrentIndex(0)
        area = get_element(area_file, "Area")
        self.area_ln_1.setText(get_element_value(area,'North'))
        self.area_ln_2.setText(get_element_value(area,'West'))
        self.area_ln_3.setText(get_element_value(area,'East'))
        self.area_ln_4.setText(get_element_value(area,'South'))
        self.tabWidget.setCurrentIndex(index)
    self.area_cb_2.setCurrentIndex(self.area_cb_2.findText(get_element_value(area_file, "Resolution")))
    self.area_ln_5.setText(get_element_value(area_file, "Filename"))
    format = get_element_value(area_file, 'Format')
    if format == 'Grib':
        self.area_rb_1.setChecked(True)
    elif format == 'NetCDF':
        self.area_rb_2.setChecked(True)
    
    self.modified = False
    self.make_window_title()
    logging.info('xml_functions.py - open_xml_query - xml file successfully parsed')

    
def add_element(doc, element_name, parent, value=None):
    logging.info('xml_functions.py - add_element')
    new_element = doc.createElementNS(NAMESPACE_URI, 'downloader:' + element_name)
    if value:
        new_text = doc.createTextNode(value)
        new_element.appendChild(new_text)
    parent.appendChild(new_element)
    return new_element


def get_element(parent, element_name):
    logging.info('xml_functions.py - get_element')
    return parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)[0]


def get_element_value(parent, element_name):
    logging.info('xml_functions.py - get_element_value')
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    if elements:
        element = elements[0]
        nodes = element.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                return node.data.strip()


def get_check_value(parent, element_name):
    logging.info('xml_functions.py - get_check_value')
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    return elements[0].childNodes[0].data.strip()


def get_element_values(parent, element_name):
    logging.info('xml_functions.py - get_element_values')
    value_list = []
    elements = parent.getElementsByTagNameNS(NAMESPACE_URI, element_name)
    for element in elements:
        value_list.append(element.childNodes[0].data.strip())
    return value_list
