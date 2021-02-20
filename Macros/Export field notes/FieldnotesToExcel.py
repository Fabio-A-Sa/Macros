# Modules

import os
import shutil
from string import ascii_letters as abc

# Functions

def search ():

    pwd = os.getcwd()
    enable_plugs = [letter for letter in abc.upper()]
    ways = ["{}:\Garmin\geocache_visits.txt".format(plug) for plug in enable_plugs]
    pointer = False
    counter = 0

    while (pointer != True and counter < len(ways)):
        
        field_note = ways[counter]

        try:
            shutil.copy(field_note, pwd)
            pointer = pointer or True
            return export ()

        except FileNotFoundError:
            error = "Directory {} cannot be found".format(field_note)
            print(error)

            pointer = pointer and True
            counter = counter + 1
            continue
    
    main_error = "GPS is not connected"
    print (main_error)
    return None


def export ():
    
    import xlsxwriter
    from xlsxwriter import Workbook
    from datetime import datetime

    current_day = datetime.now()
    date = current_day.strftime("%Y-%m-%d")
    workbook = xlsxwriter.Workbook("Logs " + date + ".xlsx")
    Excel = workbook.add_worksheet(date)
    os.rename("geocache_visits.txt", "drafts.txt")
    drafts = open("drafts.txt", "r+") # Read and paste

    DATA = drafts.readlines()
    top = "Cache Date Hour Found? Notes".strip().split(" ")

    y = 0
    for flag in range(len(top)):
        Excel.write(y, flag, top[flag])

    y = 1
    for index in range(0, len(DATA), 2):

        log = DATA[index]

        if y == 1:
            log = log[2:6] + (log[6:]).replace("T", ",").replace("Z", "")
            print(log)
        else:
            log = log[:6] + (log[6:]).replace("T", ",").replace("Z", "")
            print(log)

        items = log.split(",")

        x = 0
        for i in items:
            
            item = "".join(i.split(" "))
            
            if x == 0:
                Excel.write(y, x, "testenormal")
                #url = "http://coord.info/" + item
                #Excel.write_url(str("A" + str(y)), url , string = "some")
            else:
                Excel.write(y, x, item)

            x += 1
        y += 1

    drafts.close()
    workbook.close()
    #os.remove("drafts.txt")


if __name__ == "__main__":
    search ()