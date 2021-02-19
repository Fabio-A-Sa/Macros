# Modules

import os
import shutil

# Functions

def search ():

    pwd = os.getcwd()
    field_note = "E:\Garmin\geocache_visits.txt" # --> "F:same"

    try:
        shutil.copy(field_note, pwd)
        return export ()

    except NotADirectoryError:
        error = "This file cannot be found"
        return error


def export ():
    
    import xlwt
    import xlrd
    from datetime import datetime

    current_day = datetime.now()
    date = current_day.strftime("%Y-%m-%d")
    sheet = xlwt.Workbook()
    Excel = sheet.add_sheet(date)
    os.rename("geocache_visits.txt", "drafts.txt")
    drafts = open("drafts.txt", "r+") # Read and paste

    DATA = drafts.readlines()
    for i in range(len(DATA)):
        row = DATA[i].split(",") 

        for j in range(len(row)):
            Excel.write(i, j, row[j])

    sheet.save("Logs " + date + ".xls")
    drafts.close()


if __name__ == "__main__":
    search ()