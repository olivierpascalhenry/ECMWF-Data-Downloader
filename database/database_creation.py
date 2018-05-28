from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json




urls = ['http://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/', 'http://apps.ecmwf.int/datasets/data/interim-full-invariant/',
        'http://apps.ecmwf.int/datasets/data/interim-full-mnth/levtype=sfc/', 'http://apps.ecmwf.int/datasets/data/interim-full-moda/levtype=sfc/',
        'http://apps.ecmwf.int/datasets/data/interim-mdfa/levtype=sfc/']
fields = ['Daily', 'Invariant', 'Synoptic Monthly Means', 'Monthly Means of Daily Means', 'Monthly Means of Daily Forecast Accumulations']
dictionaries = []


for index, url in enumerate(urls):
    
    parameters_dict = {}
    field = fields[index]
    driver = webdriver.Firefox()
    driver.get(url)

    element = driver.find_element_by_class_name('ui-button-text-only')
    element.click()

    param_checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='param']")
    
    if field in ['Daily','Synoptic Monthly Means']:
        step_0 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='step'][@value='0']")[0]
        step_3 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='step'][@value='3']")[0]
        step_6 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='step'][@value='6']")[0]
        step_9 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='step'][@value='9']")[0]
        step_12 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='step'][@value='12']")[0]
        time_0 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='time'][@value='00:00:00']")[0]
        time_6 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='time'][@value='06:00:00']")[0]
        time_12 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='time'][@value='12:00:00']")[0]
        time_18 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='time'][@value='18:00:00']")[0]
    elif field == 'Monthly Means of Daily Forecast Accumulations':
        step_0_12 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='step'][@value='0-12']")[0]
        step_12_24 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='step'][@value='12-24']")[0]
        step_24_36 = driver.find_elements_by_xpath("//input[@type='checkbox'][@name='step'][@value='24-36']")[0]

    for index, parameter in enumerate(param_checkboxes):
        text = parameter.find_elements_by_xpath("..")[0].find_elements_by_xpath(".//span")[0].text
        value = parameter.get_attribute('value')
        
        if field in ['Daily','Synoptic Monthly Means']:
            parameter.send_keys(Keys.TAB)
            parameter.click()
            time.sleep(1)
        
            parameters_dict[text] = {'id':value,
                                     'steps':{'0':step_0.is_enabled(),
                                              '3':step_3.is_enabled(),
                                              '6':step_6.is_enabled(),
                                              '9':step_9.is_enabled(),
                                              '12':step_12.is_enabled()},
                                     'times':{'00:00:00':time_0.is_enabled(),
                                              '06:00:00':time_6.is_enabled(),
                                              '12:00:00':time_12.is_enabled(),
                                              '18:00:00':time_18.is_enabled()}}
            parameter.click()
            time.sleep(1)
        elif field == 'Monthly Means of Daily Forecast Accumulations':
            parameter.send_keys(Keys.TAB)
            parameter.click()
            time.sleep(1)
            parameters_dict[text] = {'id':value,
                                     'steps':{'0-12':step_0_12.is_enabled(),
                                              '12-24':step_12_24.is_enabled(),
                                              '24-36':step_24_36.is_enabled()}}
            parameter.click()
            time.sleep(1)
        else:
            parameters_dict[text] = {'id':value}

    dictionaries.append(parameters_dict)
    driver.close()

string = ('def init_parameter_database():\n    era_interim_daily_parameters = ' + str(dictionaries[0]) + '\n    '
          + 'era_interim_invariant_parameters = ' + str(dictionaries[1]) + '\n    '
          + 'era_interim_synoptic_parameters = ' + str(dictionaries[2]) + '\n    '
          + 'era_interim_daily_means_parameters = ' + str(dictionaries[3]) + '\n    '
          + 'era_interim_daily_accumulation_parameters = ' + str(dictionaries[4]) + '\n    '
          + 'return era_interim_daily_parameters, era_interim_invariant_parameters, era_interim_synoptic_parameters, '
          + 'era_interim_daily_means_parameters, era_interim_daily_accumulation_parameters')
with open('parameters_dictionary_creation_v2.py', 'w') as file:
     file.write(string)

