from string import ascii_lowercase as abc
numbers = [str(x) for x in range(0, 10)]
global offset

def numbers_to_letters (message) :

    solution = ""
    for character in message.lower():
        solution + " "
        
    return solution

def letters_to_numbers (message) :
    
    return None



def start():

    message = str(input("Your message: ")).strip().lower()
    try:
        offset = int(input("A = "))
    except ValueError:
        offset = 0
    finally:
        if message[0] in abc:
            print(letters_to_numbers(message))
        else:
            print(numbers_to_letters(message))

if __name__ == "__main__":
    start()
