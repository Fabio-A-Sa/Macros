# Modules

import os
import shutil
import requests
import xlsxwriter
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
    document = pd.read_excel(document_path)
    
    
    
    return data


def brute_force():

    data = get_data()
    driver = webdriver.Chrome(path)
    
    # Open website
    driver.get(url)
    sleep(5)
    
    # Search for solution location, input attemp and click to check
    search = driver.find_element_by_id('solution')
    search.send_keys("test" + Keys.RETURN)
    sleep(60)
    search.send_keys("another_test" + Keys.RETURN)

    return "Complete"


global url, pwd, path
url = "something.com"
pwd = "C:\\Users\\farau\Dropbox\\My PC (Fábio-MateBook)\\Desktop\\"
path = "C:\Program Files (x86)\chromedriver.exe"

if __name__ == "__main__":
    brute_force()