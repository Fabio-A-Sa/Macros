# Modules

from math import sqrt, pow

# Functions

def Points_to_Area (points):

    area = round((pow((sqrt(points)-1),2))*pow(1.39,2),2)
    print ("Available area: {}".format(area))
    return "Finished"


def Area_to_Points (area):

    number_of_points = round(pow(((sqrt(area)/1.39)+1),2))
    print ("Number of points: {}".format(number_of_points))
    return "Finished"


def search ():

    available_inputs =  {
                            "Points" : "available",
                            "Area" : "available",
                        }

    answer = "something"

    while ( answer.lower() not in [ key.lower() for key, status in available_inputs.items() 
                            if available_inputs[key] == "available" ] ) :

        answer = str(input("Would you like to ask for the number of points or available area? Points/Area: ")).strip().upper()

        if answer == "AREA":

            data = int(input("Number of points: "))
            return Points_to_Area (data)

        elif answer == "POINTS":

            data = int(input("Area: "))
            return Area_to_Points (data)
            
        else:
            return "Input error. Please try again."


if __name__ == "__main__":
    search ()