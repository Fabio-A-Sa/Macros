# Part 1 -> Decrypt message using a = 0 until j = 9
# FAS # FAS 2021/03/19

def decrypt (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            message = message.replace(caracter, str(abc.find(caracter)))
        else:
            continue
    
    total_1 = 0
    total_2 = 0
    numbers = []
    for par in message.split(" "):

        try:
            numbers.append(float(par))
            print(float(par))
            total_2 = total_2 + float(par)
        except ValueError:
            total_1 = total_2
            total_2 = 0
            continue

    print("Somatório total = {}\nPrimeira parte, antes do '+' = {}\nSegunda Parte, depois do '+' = {}".format(round(total_1 + total_2, 3), round(total_1, 3), round(total_2, 3)))

    return numbers

def get_coordinates ( alist ) :

    from math import floor as rd 
    possibilities = []
    available = []

    for number in alist:
        if (len(str(rd(number))) == 2) and rd(number) < 60:
            if len(str(number)) == 5:
                string = str(number) + "0"
                available.append(string)
            else:
                available.append(str(number))

        else:
            continue
    
    n = "N 41 "
    w = " W 008 "
    combinations = [(x, y) for x in available for y in available]
    for norte, oeste in combinations:
        attemp = n + norte + w + oeste
        possibilities.append(attemp)

    for pos in possibilities:
        print(pos)
    return possibilities



def decrypt_MAIN (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            if abc.find(caracter) == 9:
                message = message.replace(caracter, str(0))
            else:   
                message = message.replace(caracter, str(abc.find(caracter)+1))
        else:
            continue
    
    print("A == 1 --> J == 0")
    return message

def decrypt_A0 (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            message = message.replace(caracter, str(abc.find(caracter)))
        else:
            continue
    
    print("A == 0 --> J == 9")
    for item in message.split(" "):
        print(item)

def decrypt_A1 (message):

    from string import ascii_lowercase as abc
    for caracter in message:
        if caracter in abc:
            if abc.find(caracter) == 9:
                message = message.replace(caracter, str(0))
            else:   
                message = message.replace(caracter, str(abc.find(caracter)+1))
        else:
            continue
    
    print("A == 1 --> J == 0")
    for item in message.split(" "):
        print(item)
    

code = "bch.ga dc.ag bia.jeh bf.jjj hc.gda bf.jjj ea.ahi bc.abb b.aai bbe.ibi gj.hcd cg.jib bcg.jae he.jcb + eh.igh fi.jdd"
decrypt_A0(code)
decrypt_A1(code)
print(get_coordinates(numbers))

 

