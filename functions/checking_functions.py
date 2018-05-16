from functions.gui_functions import clean_stylesheet_labels
from PyQt5 import QtGui


def tabs_checking(self):
    clean_stylesheet_labels(self)
        
    label_in_red = []
    tabs_in_red = []
        
    ### check datasets
    if self.dataset_gb_1.checkedButton() == None:
        label_in_red.append(self.dataset_lb_1)
        tabs_in_red.append(0)
        
    ### check fields
    if self.field_vertical_layout.count() == 0:
        tabs_in_red.append(0)
    else:
        if self.dataset_gb_2.checkedButton() == None:
            label_in_red.append(self.dataset_lb_2)
            tabs_in_red.append(0)
        
    ### check parameters
    param_checked = False
    if self.parameter_grid_layout.count() == 0:
        tabs_in_red.append(1)
    else:
        for widget in self.parameter_cb:
            if widget.isChecked():
                param_checked = True
        if not param_checked:
            label_in_red.append(self.parameters_lb_1)
            tabs_in_red.append(1)
        
    ### check time period
    if param_checked:
        if self.time_lb_1.isEnabled() or self.time_lb_2.isEnabled() or self.time_lb_3.isEnabled():
            time_checked = True
            if self.time_lb_1.isEnabled():
                time_checked = False
                for widget in self.time_checkboxes_list:
                    if widget.isChecked():
                        time_checked = True
            step_checked = True
            if self.time_lb_2.isEnabled():
                step_checked = False
                for widget in self.step_checkboxes_list:
                    if widget.isChecked():
                        step_checked = True
            period_checked = True
            if self.time_lb_3.isEnabled():
                period_checked = False
                if self.time_rb_1.isChecked():
                    period_checked = True
                elif self.time_rb_2.isChecked():
                    for widget in self.period_cb:
                        if widget.isChecked():
                            period_checked = True
            if not time_checked:
                label_in_red.append(self.time_lb_1)
                tabs_in_red.append(2)
            if not step_checked:
                label_in_red.append(self.time_lb_2)
                tabs_in_red.append(2)
            if not period_checked:
                label_in_red.append(self.time_lb_3)
                tabs_in_red.append(2)
    else:
        tabs_in_red.append(2)
        
    ### check area
    area_enabled = self.area_lb_1.isEnabled()
    if area_enabled and self.area_cb_1.currentText() == 'Custom':
        if self.area_ln_1.text() == '' or self.area_ln_2.text() == '' or self.area_ln_3.text() == '' or self.area_ln_4.text() == '':
            label_in_red.append(self.area_lb_1)
            tabs_in_red.append(3)
    elif not area_enabled:
        tabs_in_red.append(3)
        
    ### coloring labels and tabs
    for label in label_in_red:
        label.setStyleSheet("color: rgb(200,0,0);")
    for tab in tabs_in_red:
        self.tabWidget.tabBar().setTabTextColor(tab, QtGui.QColor(200,0,0))

    if label_in_red or tabs_in_red:
        return False
    else:
        return True
