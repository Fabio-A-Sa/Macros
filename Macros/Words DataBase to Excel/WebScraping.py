# Modules

from bs4 import BeautifulSoup
import math
import os
import shutil
import requests

# Functions

def do_request (link, alphabetic_orderphabetic_order):
    
    html = requests.get(link)
    return get_text(html.text, alphabetic_order)


def get_text (html, alphabetic_order):
    
    def normalize (lines):
        
        from string import punctuation, ascii_letters
        numbers = [str(x) for x in range(10)]
        
        norm = []
        trash_words =  [
                        'a', 'as', 'e', 'é', 'o', 'os', 'de', 'por', 'para', 'um', 'uma', 'uns',
                        'tal', 'em', 'mas', 'como', 'no', 'na', 'ou', 'and', 'or', 'the', 'se',
                        'nesta', 'porém', 'esta', 'da', 'do', 'n', 'w', 'ac', 'dc', 'ad', 'este',
                        '','','','','','','','','','','','','','',
                       ]
            
        for line in lines:
            
            # Remove all punctuation and paragraphs
            line = line.replace("\n", "").replace("–", "")
            for char in line:
                if char in punctuation:
                    line = line.replace(char, "") 
            
            # Filter word by word
            words = line.split(" ")
            for word in words:
                if word not in trash_words and word not in norm:
                    
                    flag = False
                    for number in numbers:
                        for letter in ascii_letters:
                            flag = flag or (number in word and letter in word)
                            
                    if not flag and word != "":
                        norm.append(word)
                        
        print(len(norm)) 
        
        if alphabetic_order:
            return sorted(norm)
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
    return to_excel(words)


def to_excel (content):
    
    from datetime import datetime
    
    current_day = datetime.now()
    date = current_day.strftime(" %Y-%m-%d")
    title = "DataBase " + content[0].capitalize() + date
    print(title)
    
    return None


# Beginning

url = "https://pt.wikipedia.org/wiki/Portugal"
alphabetic_order = False

if __name__ == "__main__":
    do_request (url, alphabetic_order)