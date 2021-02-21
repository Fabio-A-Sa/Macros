# Excel Macros using Visual Basic for Aplications (VBA)

<img alignment = "center" src = "Images\Main.png" title = "Header" >
<br/>

## Contents
1. [Export Field Notes from GPS to Excel](https://github.com/Fabio-A-Sa/Macros-Excel#1-export-field-notes-from-gps-to-excel)
2. [Get all Coordinates between Geocaches](https://github.com/Fabio-A-Sa/Macros-Excel#2-get-all-coordinates-between-geocaches)
3. [Create a Database of words to bomb the solution checker. Brute Force.](https://github.com/Fabio-A-Sa/Macros-Excel#3-create-a-database-of-words-to-bomb-the-solution-checker)
4. (...)
<br/>

## 1. Export Field Notes from GPS to Excel

Extract the relevant information, the field notes, from the GPS that is connected to any of the computer's inputs. It serves mainly to check for any mistakes made when pointing out before sending to [GSAK](https://gsak.net/index.php) application. In a first phase, Python extracts the main file and creates an Excel sheet with the data, line by line. Then the data is processed by a Macro in Visual Basic to make it more readable.<br/>
Script compatible with all Garmin eTrex X GPS's category.
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

## 3. Create a Database of words to bomb the solution checker.

Soon

<br/>
<br/>

## License

This project is licensed under the [MIT License](https://github.com/Fabio-A-Sa/Photo-Organizer/blob/main/Licence).<br/>
<br/>
@ Fábio Araújo de Sá <br/>
2020/2021