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

def do_request (link) :
    
    html = requests.get(link)
    return get_text(html.text)


def title () :
    
    global date
    global current_directory

    current_day = datetime.now()
    date = current_day.strftime("%Y-%m-%d")
    title = "DataBase " + date + ".xlsx"

    return title


def settings () :

    wordsByAttemp = "something"
    order = "something"
    url = "something"

    options =   [
                    "yes",
                    "no",
                ]

    while ( "www" not in url and "." not in url and "http" not in url ):
        url = str(input("Please enter a url"))
        if ( "www" not in url and "." not in url and "http" not in url ):
            print("URL invalid. Please try again")

    while ( type(wordsByAttemp) != int and wordsByAttemp > 5 ):
        wordsByAttemp = int(input("How many words would you like per attemp? "))
        if type(wordsByAttemp) != int:
            print("Please enter a integer number")
        elif wordsByAttemp > 5:
            print("Maximum words per attempt exceeded")

    while (answer.lower() not in options):
        answer = str(input("Alphabetic order? Yes/No: "))
        if answer.lower() not in options:
            print("Input {} is not valid. Please try again".format(answer))
    alpOrder = True if answer.lower() == "yes" else False

    while (answer.lower() not in options):
        answer = str(input("Attemps with numbers? Yes/No: "))
        if answer.lower() not in options:
            print("Input {} is not valid. Please try again".format(answer))
    enabledNumbers = True if answer.lower() == "yes" else False

    return url, wordsByAttemp, alpOrder, enabledNumbers


def combinations(words, wordsByAttemp):

    def two_words () :

        all_combinations = [w1+w2 for w1 in words for w2 in words if w1 != w2] 
        return all_combinations


    def three_words() :

        all_combinations = [w1+w2+w3 for w1 in words for w2 in words for w3 in words if w1 != w2 and w2 != w3 and w2 != w3] 
        return all_combinations


    def four_words():

        all_combinations = [w1+w2+w3+w4 for w1 in words for w2 in words for w3 in words for w4 in words
                            if w1 != w2 and w1 != w3 and w1 != w4 and w2 != w3 and w2 != w4 and w3 != w4]
        return all_combinations


    if wordsByAttemp == 2:
        return two_words()
    if wordsByAttemp == 3:
        return three_words()
    if wordsByAttemp == 4:
        return four_words()
        


def get_text (html) :
    
    def normalize (lines) :
    
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
                    another_flag = False

                    for number in numbers:
                        for letter in ascii_letters:
                            flag = flag or (number in word and letter in word)

                    if not flag and word != "":
                        if not enabledNumbers:
                            for number in numbers:
                                another_flag = another_flag or (number in word)
                            if another_flag:
                                continue
                            else:
                                norm.append(word)
                        else:
                            norm.append(word)

        if alpOrder:
            norm = sorted(norm)
        if wordsByAttemp > 1:
            norm = combinations(norm, wordsByAttemp)
            if alpOrder:
                norm = sorted(norm)
                
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
    return excel(words)


def excel (content) :
    
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


def start () :

    global url, wordsByAttemp, alpOrder, enabledNumbers
    url, wordsByAttemp, alpOrder, enabledNumbers = settings()
    return do_request (url)


if __name__ == "__main__" :
    start()