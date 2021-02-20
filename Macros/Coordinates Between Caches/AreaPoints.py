# Modules

from math import sqrt, pow

# Functions

def Points_to_Area (points):


    return area

def Area_to_Points (area):



    return number_of_points

def search ():

    available_inputs =  {
                            "Points" : "available"
                            "Area" : "available"
                        }

    answer = "something"

    while ( answer not in [ key.lower() for key, status in available_inputs.items() 
                            if available_inputs[key] == "available" ] ) :

        answer = str(input("")).strip().lower()

        if answer == "POINTS".lower():
            return Points_to_Area (data)
        elif answer == ""
            return Area_to_Points (data)
        else:
            return "Input error. Please try again."

if __name__ == "__main__":
    search ()

