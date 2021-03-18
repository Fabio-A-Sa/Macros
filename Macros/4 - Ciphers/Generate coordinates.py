from Modules import coordinates
import NumbersAndLetters

def generate():

    attemps = []


    for attem in attemps:
        print(attemp)

    return attemps

def start():

    global header1, header2
    answer = str(input("Coordinates will be generated in N 41 W 008 form.\nDo you agree? Yes/No ")).lower().strip()
    if answer == "no":
        header1, header2 = coordinates.personalize()
    else:
        header1, header2 = coordinates.default()
    message = str(input("Input yours attemps:"))
    
    return generate(message)    


if __name__ == "__main__":
    start()