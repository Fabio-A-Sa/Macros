# Modules

from bs4 import BeautifulSoup
import requests
from os import getcwd as pwd
from string import punctuation, ascii_letters
import xlsxwriter
from xlsxwriter import Workbook
from datetime import datetime

# Functions

def do_request (link, alphabetic_orderphabetic_order):
    
    html = requests.get(link)
    return get_text(html.text, alphabetic_order)


def get_text (html, alphabetic_order):
    
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
    return to_excel(words)


def to_excel (content):
    
    global date
    global current_directory
    current_directory = pwd()
    current_day = datetime.now()
    date = current_day.strftime("%Y-%m-%d")
    title = "DataBase " + content[0].capitalize() + " " + date

    workbook = xlsxwriter.Workbook(title + ".xlsx")
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
            
        else:
            continue
    
    workbook.close()


def bomb_checker ():
        
    # In future, this function will be able to get words in current worksheet
    # and push 10 words automatically every 10 minutes
    
    return None


# Beginning

url = "https://pt.wikipedia.org/wiki/Portugal"
alphabetic_order = False

if __name__ == "__main__":
    do_request (url, alphabetic_order)