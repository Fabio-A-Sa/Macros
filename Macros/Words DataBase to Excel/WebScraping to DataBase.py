# Modules

from bs4 import BeautifulSoup
import requests
import shutil
from os import getcwd as pwd
from string import punctuation, ascii_letters
import xlsxwriter
from xlsxwriter import Workbook
from datetime import datetime

# Functions

def do_request (link):
    
    html = requests.get(link)
    return get_text(html.text)


def get_text (html):
    
    def normalize (lines):
    
        numbers = [str(x) for x in range(10)]
        norm = []
        trash_words =  [
                        'a', 'as', 'e', 'é', 'o', 'os', 'de', 'por', 'para', 'um', 'uma', 'uns',
                        'tal', 'em', 'mas', 'como', 'no', 'na', 'ou', 'and', 'or', 'the', 'se',
                        'nesta', 'porém', 'esta', 'da', 'do', 'n', 'w', 'ac', 'dc', 'ad', 'este',
                        'nas', 'tem', 'are', 'inc', 'if', 'more', 'us', 'd', 'for', 'be','das',
                        'dos', 'com', 'in', 'pela', 'pelo', 'pelas', 'pelos', 'isto', 'aquilo',
                        'by', 'que', 'cuja', 'seu', 'sua', 'foi', 'nos', 'ao', 'aos', 'à', 'à',
                       ]
            
        for line in lines:
            
            # Remove all punctuation and paragraphs
            line = line.replace("\n", "").replace("–", " ").replace("\r", " ")
            for char in line:
                if char in punctuation.replace("-", ""):
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
    return excel(words)


def title ():
    
    global date
    global current_directory

    current_day = datetime.now()
    date = current_day.strftime("%Y-%m-%d")
    title = "DataBase " + date + ".xlsx"

    return title


def excel (content):
    

    titled = title()
    workbook = xlsxwriter.Workbook(title)
    Excel = workbook.add_worksheet(date)
      
    y = 0
    x = 0
    Excel.write(y, x, "Attemps")
    for header in [x for x in range(1, 11)]:
        Excel.write(y+1, x, header)
        x += 1
       
    x = 0
    y = 2
    for word in content:
        Excel.write(y, x, word)
        x += 1
        if x == 10:
            x = 0
            y += 1

    workbook.close()
    shutil.move(titled, pwd)


def start ():

    global url, alphabetic_order
    url = str(input("Link: "))
    answer = str(input("Alphabetic order? Yes/No: "))
    alphabetic_order = True if answer.lower() == "yes" else False

    return do_request (url)


if __name__ == "__main__":
    start()