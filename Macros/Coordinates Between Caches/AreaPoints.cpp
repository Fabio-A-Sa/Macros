// Modules

#include <iostream>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

// Functions

void Points_to_area (double points) {

    int area;
    area = ceil(pow((sqrt(points)-1),2)*(pow(1.39,2)));
    cout << "Area: " << area << endl;
}

void Area_to_points (double area) {

    int points;
    points = floor(pow((((sqrt(area))/1.39)+1),2));
    cout << "Number of points: " << points << endl;
}

int main () 
{
    string answer;
    double qtd;
    vector<string> inputs = {
                                "Points", 
                                "Area",
                            } ;
    answer = "something";

    do  {
            cout << "Would you like to ask for the number of points or available area? Points/Area: ";
            cin >> answer;

            if (answer != inputs[0] && answer != inputs[1]) {
                cout << "Input error. Please try again." << endl;
            }

            else { 
                cout << "Number: ";
                cin >> qtd;
                if (answer == "Points") {
                    Area_to_points (qtd);
                }
                else {
                    Points_to_area (qtd);
                }
            }
        }   while (answer != inputs[0] && answer != inputs[1]);
    return 0;
}