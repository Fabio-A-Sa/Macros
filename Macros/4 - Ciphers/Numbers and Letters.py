from string import ascii_lowercase as abc
numbers = [str(x) for x in range(0, 10)]

def numbers_to_letters (message) :

    solution = ""
    for character in message.lower():
        try:
            solution = solution + abc[int(character) - offset]
        except ValueError:
            solution = solution + character
        
    return solution

def letters_to_numbers (message) :
    
    solution = ""
    for character in message.lower():
        if character in abc:
            solution = solution + str(int(abc.find(character) + offset))
        else:
            solution = solution + character

    return solution

def start():

    message = str(input("Your message: ")).strip().lower()
    global offset
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