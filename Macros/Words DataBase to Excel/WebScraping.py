# Modules

from bs4 import BeautifulSoup
import math
import os
import shutil
import requests

# Functions

def do_request (link):

    html = requests.get(link)
    return get_text(html.text)


def get_text (html):
    
    def normalize (lines):
        
        words = []
        trash_words = ['a', 'as', 'e', 'o', 'os', 'de', 'por', 'para', 'um', 'uma', 'uns']
        
        
        
        return alist
    
    content = [] # Empty list
    trash_words = ['a', 'as', 'e', 'o', 'os', 'de', 'por', 'para', 'um', 'uma', 'uns']
    lines = BeautifulSoup(html, 'lxml')
    
    titles = lines.find_all('title')
    content.append(titles)
    
    index = 0
    flag = True
    while flag:
        try:
            content.append(lines.find_all('p')[index].getText())
            index = index + 1
            flag = flag and True
            
        except:
            flag = flag and False
            continue
            
            
    print(content)


def to_excel (content):
    
    
    
    return None


# Beginning

url = "https://pt.wikipedia.org/wiki/Geocaching"
if __name__ == "__main__":
    do_request (url)