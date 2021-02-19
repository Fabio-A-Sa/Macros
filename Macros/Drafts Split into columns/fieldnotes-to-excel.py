# Modules

import os
import shutil

# Functions

def search ():

    current_pwd = os.getcwd()
    field_note = "E:\Garmin\geocache_visits.txt" # --> "F:same"

    try:
        shutil.copy(field_note, pwd)
        return export (pwd)

    except NotADirectoryError:
        error = "This file cannot be found"
        return error


def export (directory):

    file = os.rename("geocache_visits.txt", "drafts.txt")

    drafts = open("drafts.txt", "r+") # Read and paste



    


if __name__ = "__main__":
    search ()