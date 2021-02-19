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
    top = "Cache Date Hour Found? Notes".strip().split(" ")

    y = 0
    for flag in range(len(top)):
        Excel.write(y, flag, top[flag])

    y = 1
    for log in DATA:

        items = log.replace("T", ",").replace("Z", "").split(",")

        x = 0
        for item in items:
            Excel.write(y, x, item)
            x += 1

        y += 1

    sheet.save("Logs " + date + ".xls")
    drafts.close()


if __name__ == "__main__":
    search ()
