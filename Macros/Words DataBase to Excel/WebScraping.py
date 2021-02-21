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
        
        from string import punctuation
        
        norm = []
        trash_words =  [
                        'a', 'as', 'e', 'é', 'o', 'os', 'de', 'por', 'para', 'um', 'uma', 'uns',
                        'tal', 'em', 'mas', 'como', 'no', 'na', 'ou',  
                       ]
            
        for line in lines:
            
            line = line.replace("\n", "")
            for char in line:
                if char in punctuation:
                    line = line.replace(char, "") 
            
            words = line.split(" ")
            for word in words:
                if word not in trash_words and word not in norm:
                    norm.append(word)
                    
        print(len(norm))
        return norm
    
    content = []
    lines = BeautifulSoup(html, 'lxml')
    
    titles = lines.find_all('title')[0].getText()
    content.append(titles.lower())
    
    index = 0
    flag = True
    while flag:
        try:
            content.append(lines.find_all('p')[index].getText().lower())
            index = index + 1
            flag = flag and True
            
        except:
            flag = flag and False
            continue
            
    words = normalize(content)
    print(words)


def to_excel (content):
    
    
    
    return None


# Beginning

url = "https://pt.wikipedia.org/wiki/Geocaching"
if __name__ == "__main__":
    do_request (url)