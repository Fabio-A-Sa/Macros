# Modules

import os
import shutil
import requests
import xlsxwriter
import xlrd
import pandas as pd
from DataBase import title
from selenium import webdriver
from bs4 import BeautifulSoup
from xlsxwriter import Workbook
from datetime import datetime
from time import sleep, perf_counter
from selenium.webdriver.common.keys import Keys

# Functions

def get_data () :
    
    # Function that removes from the Excel DataBase all data ready to be used by Bot
    
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


def brute_force () :
    
    # Function with an iterative algorithm that searches words from the Database in Excel and injects them via bot into online checker.
    # Developed for a specific online checker.

    # Get Bot for GoogleChrome
    data = get_data()
    driver = webdriver.Chrome(path)
    
    # Open the website and wait to load all the HTML code
    driver.get(url)
    sleep(10)
    
    # Search for solution location, input attemp and click in bottom to check
    # Initial page:
    search = driver.find_element_by_id('solution')
    attemp = data[0]
    search.send_keys(attemp + Keys.RETURN)
    sleep(65)
    
    # Next pages:
    pointer = 1
    flag = False
    while attemp != data[-1]:
        
        search = driver.find_element_by_name('coordinates')
        attemp = data[pointer]
        search.send_keys(attemp + Keys.RETURN)
        
        # Load new page --> this takes a few seconds
        sleep(5)
        flag = flag and False
        current_HTML = driver.page_source
        
        try:
            green = driver.find_element_by_id('solution')
        except:
            green = "something"
        
        if green in str(current_HTML):
            # Found solution! Let's save her in a txt file:
            flag = flag and True
            file_name = "Solution of " + driver.find_element_by_name('coordinates')
            
            with open (file_name + ".txt", "a") as secret:
                # Append mode available
                # It creates a txt file to contain important data
                
                solution = "The solution is {}.{}".format(attemp, "\n")
                now = datetime.now()
                current_time = "Conclusion: {}.{}".format(now.strftime("%Y-%m-%d %H-%M-%S"), "\n")
                x_cell_DataBase = pointer % 10
                y_cell_DataBase = pointer // 10 + 2
                current_cell_DataBase = "Solution is in {} column and {} row of Excel's DataBase.{}".format(x_cell_DataBase, y_cell_DataBase, "\n")
                main_HTML = driver.page_source
                
                to_write =  [
                                solution,                   # <-- Solution that makes green checker
                                current_time,               # <-- Year,Month,Day,Hour,Minute,Second
                                current_cell_DataBase,      # <-- To search faster in DataBase
                                main_HTML,                  # <-- Collect all HTML, CSS and JavaScript scripts
                            ]
                
                for thing in to_write:
                    secret.write(thing)
                    
                global solution_id
                solution_id = "{}\{}.txt".format(current_pwd, file_name)
                
            try:
                shutil.move(secret, current_pwd)   
            except:
                print("{secret.capitalize()} is in the current path")
            finally:
                secret.close()
                
        if flag:
            break
        
        # To guarantee a maximum of 10 attempts in 10 minutes
        pointer = pointer + 1
        sleep(60)
        
    sleep(10)
    driver.close() # Bot closes
    
    found_solution = flag 
    if found_solution:
        return "Successful search. Solution was saved in {} file".format(solution_id)
    return "Current Database doesn't contain solution word"


global url, pwd, path, current_pwd
url = "example.com"
current_pwd = os.getcwd()
pwd = "C:\\Users\\farau\Dropbox\\My PC (Fábio-MateBook)\\Desktop\\"
path = "C:\Program Files (x86)\chromedriver.exe"

if __name__ == "__main__":
    brute_force()