# Modules

from bs4 import BeautifulSoup
import math
import os
import shutil
import requests

# Functions

def do_request (link):

    request = requests.get(link)
    soup = BeautifulSoup(request, 'lxml')
    important = soup.find_all('p').get_text()
    print(important)


def get_text ():
    return content


def to_excel (content):
    return None

# Beginning

url = "https://pt.wikipedia.org/wiki/Geocaching"
if __name__ == "__main__":
    do_request (url)