# Modules

import os
import shutil
import requests
import xlsxwriter
import xlrd
import pandas as pd
from WebScraping import title
from selenium import webdriver
from bs4 import BeautifulSoup
from xlsxwriter import Workbook
from datetime import datetime
from time import sleep, perf_counter
from selenium.webdriver.common.keys import Keys

# Functions

def get_data ():
    
    data = []
    document_path = pwd + title()
    wb = xlrd.open_workbook(document_path)
    sheet = wb.sheet_by_index(0)
    
    y = 2
    x = 0
    while y < sheet.nrows:
        
        attemp = sheet.cell_value(y, x)
        data.append(attemp)
        x = x + 1
        if x == 10:
            # Next row
            x = 0
            y = y + 1
            continue

    return data


def brute_force():
    
    # Developed for a specific online checker. For legal reasons I will not mention which one.

    data = get_data()
    driver = webdriver.Chrome(path)
    
    # Open the website and wait to load all the html code
    driver.get(url)
    sleep(10)
    
    # Search for solution location, input attemp and click to check
    # Initial page:
    search = driver.find_element_by_id('solution')
    attemp = data[0]
    search.send_keys(attemp + Keys.RETURN)
    sleep(65)
    
    # Next pages:
    pointer = 1
    flag = true
    while attemp != data[-1]:
        
        search = driver.find_element_by_id('solution')
        search.send_keys(attemp + Keys.RETURN)
        sleep(65)
        search.send_keys("another_test" + Keys.RETURN)
        
        if
    
    sleep()
    driver.close()
    
    return "Complete"


global url, pwd, path, current_pwd
url = "example.com"
current_pwd = os.getcwd()
pwd = "C:\\Users\\farau\Dropbox\\My PC (Fábio-MateBook)\\Desktop\\"
path = "C:\Program Files (x86)\chromedriver.exe"

if __name__ == "__main__":
    brute_force()