import logging
import datetime
from dateutil.relativedelta import relativedelta
from PyQt5 import QtWidgets, QtGui, QtCore
from functions.window_functions import MyInfo


def info_button(self):
    logging.debug('gui_functions.py - info_button - self.sender().objectName() ' + self.sender().objectName())
    if 'infoButton' in self.sender().objectName():
        x = QtGui.QCursor.pos().x()
        y = QtGui.QCursor.pos().y()
        x = x - 225
        y = y + 50
        self.infoWindow = MyInfo(self.info_button_text_dict[self.sender().objectName()])
        self.infoWindow.setMinimumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setMaximumSize(QtCore.QSize(450, self.infoWindow.sizeHint().height()))
        self.infoWindow.setGeometry(x, y, 450, self.infoWindow.sizeHint().height())
        self.infoWindow.exec_()


def populate_fields(self):
    logging.debug('gui_functions.py - populate_fields')
    for widget in self.field_rb:
        self.dataset_gb_2.removeButton(widget)
    disable_times_widgets(self)
    disable_steps_widgets(self)
    disable_period_widgets(self)
    clear_period_widgets(self)
    disable_area_widgets(self)
    self.dataset_lb_2.setEnabled(True)
    dataset = self.dataset_information[self.dataset_gb_1.checkedButton().text()]
    fields_dict = dataset['fields']
    fields = []
    for key, _ in fields_dict.items():
        fields.append(key)
    fields = sorted(fields)
    clear_layout(self.field_vertical_layout)
    clear_layout(self.parameter_grid_layout)
    self.parameters_lb_1.setEnabled(False)
    field_num = 0
    self.field_rb.clear()
    font = QtGui.QFont()
    font.setFamily("fonts/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    for field in fields:
        self.field_rb.append(QtWidgets.QRadioButton())
        self.field_rb[field_num].setMinimumSize(QtCore.QSize(0, 27))
        self.field_rb[field_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.field_rb[field_num].setFont(font)
        self.field_rb[field_num].setObjectName('field_rb_' + str(field_num))
        self.field_rb[field_num].setText(field)
        self.field_rb[field_num].toggled.connect(lambda: populate_parameters(self, dataset))
        self.field_rb[field_num].toggled.connect(lambda: clean_stylesheet_field(self))
        self.dataset_gb_2.addButton(self.field_rb[field_num])
        self.field_vertical_layout.addWidget(self.field_rb[field_num])
        field_num += 1
    self.field_vertical_layout.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))  
    self.set_modified()


def populate_parameters(self, dataset):
    logging.debug('gui_functions.py - populate_parameters')
    disable_times_widgets(self)
    disable_steps_widgets(self)
    disable_period_widgets(self)
    disable_area_widgets(self)
    field = self.dataset_gb_2.checkedButton().text()
    populate_pre_time(self, field)
    self.tabWidget.setCurrentIndex(1)
    clear_layout(self.parameter_grid_layout)
    self.parameters_lb_1.setEnabled(True)
    self.checked_parameter.clear()
    parameters_dict = dataset['parameters'][field]
    parameters = []
    for key, _ in parameters_dict.items():
        parameters.append(key)
    parameters = sorted(parameters)
    param_num = 0
    self.parameter_cb.clear()
    font = QtGui.QFont()
    font.setFamily("fonts/SourceSansPro-Regular.ttf")
    font.setPointSize(10)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    i, j = 0, 0
    self.parameters_bg_1 = QtWidgets.QButtonGroup()
    self.parameters_bg_1.setObjectName("parameters_bg_1")
    self.parameters_bg_1.setExclusive(False)
    for parameter in parameters:
        self.parameter_cb.append(QtWidgets.QCheckBox())
        self.parameter_cb[param_num].setMinimumSize(QtCore.QSize(0, 27))
        self.parameter_cb[param_num].setMaximumSize(QtCore.QSize(16777215, 27))
        self.parameter_cb[param_num].setFont(font)
        self.parameter_cb[param_num].setObjectName('parameter_cb_' + str(param_num))
        self.parameter_cb[param_num].setText(parameter)
        self.parameters_bg_1.addButton(self.parameter_cb[param_num])
        self.parameter_cb[param_num].toggled.connect(lambda: populate_times(self, dataset, field, parameters_dict))
        self.parameter_cb[param_num].toggled.connect(lambda: clean_stylesheet_parameter(self))
        self.parameter_cb[param_num].toggled.connect(lambda: add_checked_parameter_list(self))
        self.parameter_grid_layout.addWidget(self.parameter_cb[param_num], i, j, 1, 1)
        j += 1
        if j == 2:
            j = 0
            i += 1
        param_num += 1
    self.tabWidget.setCurrentIndex(0)
    self.set_modified()


def populate_pre_time(self, field):
    logging.debug('gui_functions.py - populate_pre_time')
    if field == 'Monthly Means of Daily Forecast Accumulations':
        self.time_cb_8.setVisible(False)
        self.time_cb_9.setVisible(False)
        self.time_cb_5.setText('0-12')
        self.time_cb_6.setText('12-24')
        self.time_cb_7.setText('24-36')
    else:
        self.time_cb_8.setVisible(True)
        self.time_cb_9.setVisible(True)
        self.time_cb_5.setText('0')
        self.time_cb_6.setText('3')
        self.time_cb_7.setText('6')


def populate_times(self, dataset, field, parameters_dict):
    logging.debug('gui_functions.py - populate_times')
    disable_times_widgets(self)
    disable_steps_widgets(self)
    disable_period_widgets(self)
    disable_area_widgets(self)
    if self.parameters_bg_1.checkedButton():
        enable_area_widgets(self)
        field_steps = dataset['steps'][field]
        field_times = dataset['times'][field]
        field_fields = dataset['fields'][field] 
        if field_times:
            enable_times_widgets(self)
        if field_steps:
            enable_steps_widgets(self)
        if field_fields:
            enable_period_widgets(self)
        time_true_false_list = []
        step_true_false_list = []
        if field_times:
            for widget in self.parameter_cb:
                if widget.isChecked():
                    times = parameters_dict[widget.text()]['times']
                    if not time_true_false_list:
                        time_true_false_list.append(times['00:00:00'])
                        time_true_false_list.append(times['06:00:00'])
                        time_true_false_list.append(times['12:00:00'])
                        time_true_false_list.append(times['18:00:00'])
                    else:
                        if time_true_false_list[0]:
                            time_true_false_list[0] = times['00:00:00']
                        if time_true_false_list[1]:
                            time_true_false_list[1] = times['06:00:00']
                        if time_true_false_list[2]:
                            time_true_false_list[2] = times['12:00:00']
                        if time_true_false_list[3]:
                            time_true_false_list[3] = times['18:00:00']
            parameter_times_checkboxes(self, time_true_false_list)            
        if field_steps:            
            for widget in self.parameter_cb:
                if widget.isChecked():
                    steps = parameters_dict[widget.text()]['steps']
                    if not step_true_false_list:
                        for widget_2 in self.step_checkboxes_list:
                            if not widget_2.isHidden():
                                step_true_false_list.append(steps[widget_2.text()])
                    else:
                        for index, widget_2 in enumerate(self.step_checkboxes_list):
                            if not widget_2.isHidden():
                                if step_true_false_list[index]:
                                    step_true_false_list[index] = steps[widget_2.text()]
            parameter_steps_checkboxes(self, step_true_false_list)
    self.set_modified()

    
def parameter_times_checkboxes(self, list):
    logging.debug('gui_functions.py - parameter_times_checkboxes')
    if list:
        for index, widget in enumerate(self.time_checkboxes_list):
            widget.setEnabled(list[index])
    else:
        disable_times_widgets(self)
        disable_steps_widgets(self)
        disable_period_widgets(self)
    

def parameter_steps_checkboxes(self, list):
    logging.debug('gui_functions.py - parameter_steps_checkboxes')
    if list:
        for index, widget in enumerate(self.step_checkboxes_list):
            if not widget.isHidden():
                widget.setEnabled(list[index])
    else:
        disable_times_widgets(self)
        disable_steps_widgets(self)
        disable_period_widgets(self)


def enable_times_widgets(self):
    logging.debug('gui_functions.py - enable_times_widgets')
    self.time_lb_1.setEnabled(True)
    self.time_lb_1.setStyleSheet("QLabel {\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QLabel:disabled {\n"
    "    color: rgb(120,120,120);\n"
    "}")
    self.time_cb_1.setEnabled(True)
    self.time_cb_2.setEnabled(True)
    self.time_cb_3.setEnabled(True)
    self.time_cb_4.setEnabled(True)
    

def enable_steps_widgets(self):
    logging.debug('gui_functions.py - enable_steps_widgets')
    self.time_lb_2.setEnabled(True)
    self.time_lb_2.setStyleSheet("QLabel {\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "    color: rgb(120,120,120);\n"
            "}")
    self.time_cb_5.setEnabled(True)
    self.time_cb_6.setEnabled(True)
    self.time_cb_7.setEnabled(True)
    self.time_cb_8.setEnabled(True)
    self.time_cb_9.setEnabled(True)
    
    
def enable_period_widgets(self):
    logging.debug('gui_functions.py - enable_period_widgets')
    clear_period_widgets(self)
    
    if self.dataset_information[self.dataset_gb_1.checkedButton().text()]['fields'][self.dataset_gb_2.checkedButton().text()]['step'] == 'daily':
        self.time_rb_1.setEnabled(True)
        #self.time_de_1.setEnabled(True)
        #self.time_de_2.setEnabled(True)

    self.time_rb_2.setEnabled(True)
    #self.period_cb_1.setEnabled(True)
    self.time_lb_3.setEnabled(True)
    self.time_lb_4.setEnabled(True)
    self.time_lb_3.setStyleSheet("QLabel {\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "    color: rgb(120,120,120);\n"
            "}")
    self.time_lb_4.setStyleSheet("QLabel {\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "    color: rgb(120,120,120);\n"
            "}")


def disable_times_widgets(self):
    logging.debug('gui_functions.py - disable_times_widgets')
    self.time_lb_1.setEnabled(False)
    self.time_lb_1.setStyleSheet("QLabel {\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "    color: rgb(120,120,120);\n"
            "}")
    self.time_cb_1.setEnabled(False)
    self.time_cb_2.setEnabled(False)
    self.time_cb_3.setEnabled(False)
    self.time_cb_4.setEnabled(False)
    self.time_cb_1.setChecked(False)
    self.time_cb_2.setChecked(False)
    self.time_cb_3.setChecked(False)
    self.time_cb_4.setChecked(False)
    

def disable_steps_widgets(self):
    logging.debug('gui_functions.py - disable_steps_widgets')
    self.time_lb_2.setEnabled(False)
    self.time_lb_2.setStyleSheet("QLabel {\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "    color: rgb(120,120,120);\n"
            "}")
    self.time_cb_5.setEnabled(False)
    self.time_cb_6.setEnabled(False)
    self.time_cb_7.setEnabled(False)
    self.time_cb_8.setEnabled(False)
    self.time_cb_9.setEnabled(False)
    self.time_cb_5.setChecked(False)
    self.time_cb_6.setChecked(False)
    self.time_cb_7.setChecked(False)
    self.time_cb_8.setChecked(False)
    self.time_cb_9.setChecked(False)
    
    
def disable_period_widgets(self):
    logging.debug('gui_functions.py - disable_period_widgets')
    clear_period_widgets(self)
    self.time_rb_1.setEnabled(False)
    self.time_rb_2.setEnabled(False)
    self.time_de_1.setEnabled(False)
    self.time_de_2.setEnabled(False)
    self.period_cb_1.setEnabled(False)
    self.time_lb_3.setEnabled(False)
    self.time_lb_4.setEnabled(False)
    self.time_lb_3.setStyleSheet("QLabel {\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "    color: rgb(120,120,120);\n"
            "}")
    self.time_lb_4.setStyleSheet("QLabel {\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QLabel:disabled {\n"
            "    color: rgb(120,120,120);\n"
            "}")


def clear_period_widgets(self):
    logging.debug('gui_functions.py - clear_period_widgets')
    clear_layout(self.time_vertical_layout)
    self.period_bg_1.setExclusive(False)
    self.time_rb_1.setChecked(False)
    self.time_rb_2.setChecked(False)
    self.period_bg_1.setExclusive(True)


def activate_period_elements(self):
    logging.info('gui_functions.py - acxtivate_period_elements')
    if self.time_rb_1.isChecked():
        self.time_de_1.setEnabled(True)
        self.time_de_2.setEnabled(True)
        self.period_cb_1.setEnabled(False)
        if self.time_vertical_layout.count() > 0:
            self.period_cb.clear()
            clear_layout(self.time_vertical_layout)
    elif self.time_rb_2.isChecked():
        self.time_de_1.setEnabled(False)
        self.time_de_2.setEnabled(False)
        self.period_cb_1.setEnabled(True)
        populate_period_elements(self)
            
            
def populate_period_elements(self):
    self.period_cb.clear()
    clear_layout(self.time_vertical_layout)
    dataset = self.dataset_gb_1.button(self.dataset_gb_1.checkedId()).text()
    field = self.dataset_gb_2.button(self.dataset_gb_2.checkedId()).text()
    start = self.dataset_information[dataset]['fields'][field]['start']
    step = self.dataset_information[dataset]['fields'][field]['step']
    end = self.dataset_information[dataset]['fields'][field]['end']
    start_year = int(start[:4])
    start_month = int(start[5:])
    if end == 'now':
        end_year = (datetime.date.today() - relativedelta(months=+3)).year
        end_month = (datetime.date.today() - relativedelta(months=+3)).month
    time_grid = QtWidgets.QGridLayout()
    time_grid.setContentsMargins(0, 0, 0, 0)
    time_grid.setObjectName("time_grid")
    self.time_vertical_layout.addLayout(time_grid)
    font = QtGui.QFont()
    font.setFamily("fonts/SourceSansPro-Regular.ttf")
    font.setPointSize(9)
    font.setBold(False)
    font.setWeight(50)
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    if self.period_cb_1.currentText() == 'monthly period':
        n_month = ((datetime.datetime(end_year,end_month,1).year - datetime.datetime(start_year,start_month,1).year) * 12
                    + datetime.datetime(end_year,end_month,1).month - datetime.datetime(start_year,start_month,1).month)
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',
                  '','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for j in range(len(months)):
            label = QtWidgets.QLabel()
            label.setMinimumSize(QtCore.QSize(0, 27))
            label.setMaximumSize(QtCore.QSize(16777215, 27))
            label.setFont(font)
            label.setText(months[j])
            label.setObjectName("label_" + months[j])
            time_grid.addWidget(label, 0, j, 1, 1)
        k = 0
        start_year -= 1
        for i in range(int((n_month / 24) + 1)):
            tmp = []
            l = 1
            for j in range(26):
                if k <= n_month:
                    if j == 0 or j == 13:
                        start_year += 1
                        label = QtWidgets.QLabel()
                        label.setMinimumSize(QtCore.QSize(0, 27))
                        label.setMaximumSize(QtCore.QSize(16777215, 27))
                        label.setFont(font)
                        label.setText(str(start_year))
                        label.setObjectName("label_" + str(start_year))
                        time_grid.addWidget(label, i + 1, j, 1, 1)
                    else:
                        k += 1
                        checkbox = QtWidgets.QCheckBox()
                        checkbox.setMinimumSize(QtCore.QSize(0, 27))
                        checkbox.setMaximumSize(QtCore.QSize(16777215, 27))
                        checkbox.setFont(font)
                        checkbox.setObjectName("checkbox_" + str(start_year) + "_" + str(l))
                        checkbox.toggled.connect(self.set_modified)
                        checkbox.toggled.connect(lambda: clean_stylesheet_period(self))
                        self.period_cb.append(checkbox)
                        time_grid.addWidget(checkbox, i + 1, j, 1, 1)
                        l += 1
                        if l == 13:
                            l = 1
        for j in range(len(months)):
            label = QtWidgets.QLabel()
            label.setMinimumSize(QtCore.QSize(0, 27))
            label.setMaximumSize(QtCore.QSize(16777215, 27))
            label.setFont(font)
            label.setText(months[j])
            label.setObjectName("label_" + months[j])
            time_grid.addWidget(label, i + 2, j, 1, 1)
    else:
        n_year = end_year - start_year
        i, j = 0, 0
        for k in range(n_year + 1):
            checkbox = QtWidgets.QCheckBox()
            checkbox.setMinimumSize(QtCore.QSize(0, 27))
            checkbox.setMaximumSize(QtCore.QSize(16777215, 27))
            checkbox.setFont(font)
            checkbox.setText(str(start_year))
            checkbox.setObjectName("checkbox_" + str(start_year))
            checkbox.toggled.connect(self.set_modified)
            checkbox.toggled.connect(lambda: clean_stylesheet_period(self))
            self.period_cb.append(checkbox)
            time_grid.addWidget(checkbox, j, i, 1, 1)
            i += 1
            if i > 12:
                i = 0
                j += 1
            start_year += 1


def enable_area_widgets(self):
    logging.debug('gui_functions.py - enable_area_widgets')
    self.area_lb_1.setEnabled(True)
    self.area_lb_2.setEnabled(True)
    self.area_lb_3.setEnabled(True)
    self.area_ln_1.setEnabled(True)
    self.area_ln_2.setEnabled(True)
    self.area_ln_3.setEnabled(True)
    self.area_ln_4.setEnabled(True)
    self.area_rb_1.setEnabled(True)


def disable_area_widgets(self):
    logging.debug('gui_functions.py - disable_area_widgets')
    self.area_lb_1.setEnabled(False)
    self.area_lb_2.setEnabled(False)
    self.area_lb_3.setEnabled(False)
    self.area_ln_1.setEnabled(False)
    self.area_ln_2.setEnabled(False)
    self.area_ln_3.setEnabled(False)
    self.area_ln_4.setEnabled(False)
    self.area_rb_1.setEnabled(False)


def set_visibility_area_map(self):
    logging.debug('gui_functions.py - set_visibility_area_map')
    if self.area_cb_1.currentText() == 'Custom':
        show_area_map(self)
    else:
        hide_area_map(self)
    
    
def enable_area_widgets(self):
    logging.debug('gui_functions.py - enable_area_widgets')
    self.area_lb_1.setEnabled(True)
    self.area_lb_2.setEnabled(True)
    self.area_cb_1.setEnabled(True)
    self.area_cb_2.setEnabled(True)
    self.area_cb_1.setCurrentIndex(1)
    self.area_cb_2.setCurrentIndex(4)


def disable_area_widgets(self):
    logging.debug('gui_functions.py - disable_area_widgets')
    self.area_lb_1.setEnabled(False)
    self.area_lb_2.setEnabled(False)
    self.area_cb_1.setEnabled(False)
    self.area_cb_2.setEnabled(False)
    self.area_cb_1.setCurrentIndex(1)
    self.area_cb_2.setCurrentIndex(4)


def hide_area_map(self):
    logging.debug('gui_functions.py - hide_area_map')
    if self.area_vertical_layout.count() > 0:
        clear_layout(self.area_vertical_layout)


def show_area_map(self):
    logging.debug('gui_functions.py - show_area_map')
    if self.area_vertical_layout.count() == 0:
        font = QtGui.QFont()
        font.setFamily("fonts/SourceSansPro-Regular.ttf")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        font2 = QtGui.QFont()
        font2.setFamily("fonts/SourceSansPro-Regular.ttf")
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.addItem(QtWidgets.QSpacerItem(230, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.area_lb_4 = QtWidgets.QLabel()
        self.area_lb_4.setMinimumSize(QtCore.QSize(15, 15))
        self.area_lb_4.setMaximumSize(QtCore.QSize(15, 15))
        self.area_lb_4.setFont(font)
        self.area_lb_4.setPixmap(QtGui.QPixmap("icons/bottom_icon.svg"))
        self.area_lb_4.setScaledContents(True)
        self.area_lb_4.setObjectName("area_lb_4")
        self.horizontalLayout_11.addWidget(self.area_lb_4)
        self.horizontalLayout_11.addItem(QtWidgets.QSpacerItem(688, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.area_vertical_layout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.addItem(QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.area_ln_1 = QtWidgets.QLineEdit()
        self.area_ln_1.setMinimumSize(QtCore.QSize(60, 27))
        self.area_ln_1.setMaximumSize(QtCore.QSize(60, 27))
        self.area_ln_1.setFont(font2)
        self.area_ln_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.area_ln_1.setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.area_ln_1.setFrame(False)
        self.area_ln_1.setAlignment(QtCore.Qt.AlignCenter)
        self.area_ln_1.setObjectName("area_ln_1")
        self.horizontalLayout_8.addWidget(self.area_ln_1)
        self.horizontalLayout_8.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_8.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.area_ln_2 = QtWidgets.QLineEdit()
        self.area_ln_2.setMinimumSize(QtCore.QSize(60, 27))
        self.area_ln_2.setMaximumSize(QtCore.QSize(60, 27))
        self.area_ln_2.setFont(font2)
        self.area_ln_2.setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.area_ln_2.setFrame(False)
        self.area_ln_2.setAlignment(QtCore.Qt.AlignCenter)
        self.area_ln_2.setObjectName("area_ln_2")
        self.verticalLayout_7.addWidget(self.area_ln_2)
        self.verticalLayout_7.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.gridLayout_8.addLayout(self.verticalLayout_7, 1, 0, 1, 1)
        self.area_lb_3 = QtWidgets.QLabel()
        self.area_lb_3.setMinimumSize(QtCore.QSize(250, 250))
        self.area_lb_3.setMaximumSize(QtCore.QSize(250, 250))
        self.area_lb_3.setPixmap(QtGui.QPixmap("icons/EMC_globe_terrestre.png"))
        self.area_lb_3.setScaledContents(True)
        self.area_lb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.area_lb_3.setObjectName("area_lb_3")
        self.gridLayout_8.addWidget(self.area_lb_3, 1, 1, 1, 1)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_28.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.area_ln_3 = QtWidgets.QLineEdit()
        self.area_ln_3.setMinimumSize(QtCore.QSize(60, 27))
        self.area_ln_3.setMaximumSize(QtCore.QSize(60, 27))
        self.area_ln_3.setFont(font2)
        self.area_ln_3.setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.area_ln_3.setFrame(False)
        self.area_ln_3.setAlignment(QtCore.Qt.AlignCenter)
        self.area_ln_3.setObjectName("area_ln_3")
        self.verticalLayout_28.addWidget(self.area_ln_3)
        self.verticalLayout_28.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        self.gridLayout_8.addLayout(self.verticalLayout_28, 1, 2, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.area_ln_4 = QtWidgets.QLineEdit()
        self.area_ln_4.setMinimumSize(QtCore.QSize(60, 27))
        self.area_ln_4.setMaximumSize(QtCore.QSize(60, 27))
        self.area_ln_4.setFont(font2)
        self.area_ln_4.setStyleSheet("QLineEdit {\n"
        "    border-radius: 3px;\n"
        "    padding: 1px 4px 1px 4px;\n"
        "    background-color:  rgb(240, 240, 240);\n"
        "}")
        self.area_ln_4.setFrame(False)
        self.area_ln_4.setAlignment(QtCore.Qt.AlignCenter)
        self.area_ln_4.setObjectName("area_ln_4")
        self.horizontalLayout_9.addWidget(self.area_ln_4)
        self.horizontalLayout_9.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.gridLayout_8.addLayout(self.horizontalLayout_9, 2, 1, 1, 1)
        self.horizontalLayout_19.addLayout(self.gridLayout_8)
        self.horizontalLayout_19.addItem(QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.area_vertical_layout.addLayout(self.horizontalLayout_19)
        self.area_ln_1.textChanged.connect(lambda: clean_stylesheet_area(self))
        self.area_ln_2.textChanged.connect(lambda: clean_stylesheet_area(self))
        self.area_ln_3.textChanged.connect(lambda: clean_stylesheet_area(self))
        self.area_ln_4.textChanged.connect(lambda: clean_stylesheet_area(self))
        self.area_ln_1.textChanged.connect(self.set_modified)
        self.area_ln_2.textChanged.connect(self.set_modified)
        self.area_ln_3.textChanged.connect(self.set_modified)
        self.area_ln_4.textChanged.connect(self.set_modified)


def clear_layout(layout):
    logging.debug('gui_functions.py - clear_layout')
    for i in reversed(range(layout.count())):   
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)        


def clean_stylesheet_labels(self):
    logging.debug('gui_functions.py - clean_stylesheet_labels')
    labels = self.findChildren(QtWidgets.QLabel)
    for label in labels:
        label.setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}\n"
        "\n"
        "QLabel:disabled {\n"
        "    color: rgb(120,120,120);\n"
        "}")
    for i in range(self.tabWidget.count()):
        self.tabWidget.tabBar().setTabTextColor(i, QtGui.QColor(0,0,0))


def clean_stylesheet_dataset(self):
    logging.debug('gui_functions.py - clean_stylesheet_dataset')
    self.dataset_lb_1.setStyleSheet("QLabel {\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QLabel:disabled {\n"
    "    color: rgb(120,120,120);\n"
    "}")
    clean_stylesheet_dataset_tab(self)


def clean_stylesheet_field(self):
    logging.debug('gui_functions.py - clean_stylesheet_field')
    self.dataset_lb_2.setStyleSheet("QLabel {\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QLabel:disabled {\n"
    "    color: rgb(120,120,120);\n"
    "}")
    clean_stylesheet_dataset_tab(self)

    
def clean_stylesheet_dataset_tab(self):
    logging.debug('gui_functions.py - clean_stylesheet_dataset_tab')
    if self.dataset_gb_1.checkedButton() != None and self.dataset_gb_2.checkedButton() != None:
        self.tabWidget.tabBar().setTabTextColor(0, QtGui.QColor(0,0,0))


def clean_stylesheet_parameter(self):
    logging.debug('gui_functions.py - clean_stylesheet_parameter')
    self.parameters_lb_1.setStyleSheet("QLabel {\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QLabel:disabled {\n"
    "    color: rgb(120,120,120);\n"
    "}")
    self.tabWidget.tabBar().setTabTextColor(1, QtGui.QColor(0,0,0))


def clean_stylesheet_time(self):
    logging.debug('gui_functions.py - clean_stylesheet_time')
    self.time_lb_1.setStyleSheet("QLabel {\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QLabel:disabled {\n"
    "    color: rgb(120,120,120);\n"
    "}")
    clean_stylesheet_time_tab(self)


def clean_stylesheet_step(self):
    logging.debug('gui_functions.py - clean_stylesheet_step')
    self.time_lb_2.setStyleSheet("QLabel {\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QLabel:disabled {\n"
    "    color: rgb(120,120,120);\n"
    "}")
    clean_stylesheet_time_tab(self)


def clean_stylesheet_period(self):
    logging.debug('gui_functions.py - clean_stylesheet_period')
    self.time_lb_3.setStyleSheet("QLabel {\n"
    "    color: black;\n"
    "}\n"
    "\n"
    "QLabel:disabled {\n"
    "    color: rgb(120,120,120);\n"
    "}")
    clean_stylesheet_time_tab(self)


def clean_stylesheet_time_tab(self):
    logging.debug('gui_functions.py - clean_stylesheet_time_tab')
    time_enabled, step_enabled, period_enabled = False, False, False
    if self.time_lb_1.isEnabled():
        if self.time_bg_1.checkedButton() != None:
            time_enabled = True
    else:
        time_enabled = True
    if self.time_lb_2.isEnabled():
        if self.step_bg_1.checkedButton() != None:
            step_enabled = True
    else:
        step_enabled = True
    if self.time_lb_3.isEnabled():
        if self.period_bg_1.checkedButton() != None:
            period_enabled = True
    else:
        period_enabled = True
    if time_enabled and step_enabled and period_enabled:
        self.tabWidget.tabBar().setTabTextColor(2, QtGui.QColor(0,0,0))


def clean_stylesheet_area(self):
    logging.debug('gui_functions.py - clean_stylesheet_area')
    if self.area_ln_1.text() and self.area_ln_2.text() and self.area_ln_3.text() and self.area_ln_4.text():
        self.area_lb_1.setStyleSheet("QLabel {\n"
        "    color: black;\n"
        "}\n"
        "\n"
        "QLabel:disabled {\n"
        "    color: rgb(120,120,120);\n"
        "}")
        self.tabWidget.tabBar().setTabTextColor(3, QtGui.QColor(0,0,0))


def add_checked_parameter_list(self):
    logging.debug('gui_functions.py - add_checked_parameter_list')
    widget = self.sender()
    if widget.isChecked():
        self.checked_parameter.append(widget.text())
    else:
        self.checked_parameter.remove(widget.text())
