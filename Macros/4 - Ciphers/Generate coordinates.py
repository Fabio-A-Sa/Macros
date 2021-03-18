from Modules import coordinates
import NumbersAndLetters

def generate(message):

    def filter_impossible_attemps(message):

        some = []
        for number in message:

            

        return some

    attemps = []
    pairs = [(p1.strip(), p2.strip()) for p1 in message for p2 in message]

    for p1, p2 in pairs:
        attemp = header1 + " " + p1 + " " + header2 + " " + p2
        attemps.append(attemp)

    for attemp in attemps:
        print(attemp)

    return attemps


def start():

    global header1, header2
    answer = str(input("Coordinates will be generated in N 41 W 008 form.\nDo you agree? Yes/No ")).lower().strip()
    if answer == "no":
        header1, header2 = coordinates.personalize()
    else:
        header1, header2 = coordinates.default()
    message = str(input("Numbers: "))
    
    return generate(message.split(" "))    


if __name__ == "__main__":
    start()