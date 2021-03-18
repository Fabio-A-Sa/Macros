# Macros using VisualBasic, C++ and Python

<img alignment = "center" src = "Images\Main.png" title = "Header" >
<br/>

## Contents

- [x] [1. Export Field Notes from GPS to Excel](https://github.com/Fabio-A-Sa/Macros#1-export-field-notes-from-gps-to-excel)
- [x] [2. Get all Coordinates between Geocaches](https://github.com/Fabio-A-Sa/Macros#2-get-all-coordinates-between-geocaches)
- [x] [3. Create a Database with possible attemps. Use them with Brute Force.](https://github.com/Fabio-A-Sa/Macros#3-create-a-database-with-possible-attemps-use-them-with-brute-force)
    - [x] [3.1 Pull words from web and push them to Excel DataBase]() 
    - [x] [3.2 Brute Force using DataBase]()
    - [ ] [3.3 Auto-Send emails using DataBase]()
- [x] [4. Ciphers](https://github.com/Fabio-A-Sa/Macros#3-create-a-database-with-possible-attemps-use-them-with-brute-force)
    - [x] [4.1 Numbers or letters]() 
    - [x] [4.2 Get Coordinates]()
    - [ ] [4.3 Morse code]()
- [ ] [5. Periodic auto-backup of web pages]()


## 1. Export Field Notes from GPS to Excel

Extract the relevant information, the field notes, from the GPS that is connected to any of the computer's inputs. It serves mainly to check for any mistakes made when pointing out before sending to [GSAK](https://gsak.net/index.php) application. In a first phase, Python extracts the copy of main file and creates an Excel sheet with the data, line by line. Then the data is processed by a Macro in Visual Basic to make it more readable.<br/>
Script compatible at least with all Garmin eTrex X GPS's category.
<br/>

<img alignment = "center" src = "Images\Export.png" title = "Export" >

<br/>

## 2. Get all Coordinates between Geocaches

Sometimes geocaches are hidden among others. Based on the minimum distance between physical points, 161 meters, it is possible to approximate the area in which the geocache can be hidden and with Excel to generate all possible coordinates. The growth in the number of points due to the increase in area is linear. <br/>
For example, to obtain the number of coordinates that the Visual Basic script will generate use C++ function:

```
#include <iostream>
#include <cmath>
using namespace std;

void Area_to_points (double area) {

    int points;
    points = floor(pow((((sqrt(area))/1.39)+1),2));
    cout << "Number of points: " << points << endl;
}

int main () { cout << Area_to_points( x ) << endl; return 0; }
```

On the other hand, if we want to obtain the area taking into account the number of coordinates generated, we use the function in Python:

```
from math import pow, sqrt

def Points_to_Area (points):

    area = round((pow((sqrt(points)-1),2))*pow(1.39,2),2)
    return "Available area: {}".format(area)
```

<br/>

<img alignment = "center" src = "Images\Scheme.png" title = "Areas" >

<br/>

## 3. Create a Database with possible attemps. Use them with Brute Force.

### 3.1 Get all words from a website and push them to Excel

A script that analyzes any webpage and pull all words contained there. Apply various filters to the text, namely:
- removing punctuation, 
- removing common words, 
- removing repeated words, 
- removing paragraphs, 
- removing indexing numbers, 
- removing additional links.

The result is what I show in the following figure. For example, in wikipédia [Portugal](https://pt.wikipedia.org/wiki/Portugal), the script generates in 3 seconds an Excel sheet with 10 columns and 351 lines, which means more than 3500 unique and ready-to-use words. There is also the option to sort by alphabetic order.

<img alignment = "center" src = "Images\Base.PNG" title = "DataBase" >

In addition, all words will be placed separately, 10 per line, in all available cells. Finally, apply a common Macro with Visual Basic to make all cells in the DataBase more readable.

<img alignment = "center" src = "Images\Part1.png" title = "Scheme" >

### 3.2 Use them with Brute Force

Use Excel as a DataBase of previously selected and filtered words. Each word is injected into the verifier website through a bot, where it is tested. If you hit the key, it saves all in a text file (date, time, solution, resulting HTML code) and break a loop. If does not work, the bot returns to the database to push next word. The cycle continues at a frequency of approximately one word per minute (frequency adaptable to each situation) until the entire database is consumed.

<br/>

<img alignment = "center" src = "Images\Part2.png" title = "Forced" >

<br/>

## 4. Ciphers

description soon

<br/>

## 5. Periodic auto-backup of all my web pages.

soon

<br/>
<br/>

## License

This project is licensed under the [MIT License](https://github.com/Fabio-A-Sa/Photo-Organizer/blob/main/Licence).<br/>
<br/>
@ Fábio Araújo de Sá <br/>
2020/2021