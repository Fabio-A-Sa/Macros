# Part 5 -> Santiago de Compostela
# FAS 2021/03/19


from string import ascii_uppercase as abc

instructions = "Para Santiago por vezes segue-se o azul e só depois o amarelo. Nas termas recupera-se melhor a cantar."

message1 = "9-13-1-6-21-18-9-19"
message2 = "19-9-13-15-4-1-12-9-19-21-9-19"
message3 = "12-9-18-9-19-1-12-15-4"

def to_letters(numbers, offset):

    astring = ""
    for number in numbers.split("-"):
        astring = astring + str(abc[int(number) - 1 + offset])

    return astring

# A == 1
m1 = to_letters(message1, 1) # JNBGVSJT
m2 = to_letters(message2, 1) # TJNPEBMJTVJT
m3 = to_letters(message3, 1) # MJSJTBMPE

# A == 0
m1 = to_letters(message1, 0) # IMAFURIS
m2 = to_letters(message2, 0) # SIMODALISUIS
m3 = to_letters(message3, 0) # LIRISALOD

def frequency(message):

    dictionary = {}
    for letter in message:
        if letter not in dictionary.keys():
            dictionary[letter] = dictionary.get(letter, 0) + 1
        else:
            dictionary[letter] += 1

    return dictionary

def sum_freqs (rd):

    main_dict = {}
    
    for dictionary in rd:
        for key in dictionary:
            
            main_dict[key] = 0
    
    for dictionary in rd:
        for key in dictionary:
            
            main_dict[key] = main_dict[key] + dictionary[key]

    return main_dict

a1 = [int(x) for x in sorted(message1.split("-"), key = lambda x: int(x))]
print(a1, sum(a1))

a2 = [int(x) for x in sorted(message2.split("-"), key = lambda x: int(x))]
print(a2, sum(a2))

a3 = [int(x) for x in sorted(message3.split("-"), key = lambda x: int(x))]
print(a3, sum(a3))

all_messages = [m1, m2, m3]
dicts = []
for message in all_messages:
    print(frequency(message))
    # {'I': 2, 'M': 1, 'A': 1, 'F': 1, 'U': 1, 'R': 1, 'S': 1}
    # {'S': 3, 'I': 3, 'M': 1, 'O': 1, 'D': 1, 'A': 1, 'L': 1, 'U': 1}
    # {'L': 2, 'I': 2, 'R': 1, 'S': 1, 'A': 1, 'O': 1, 'D': 1}
    dicts.append(frequency(message))

print("\nTotal sum: {}".format(sum_freqs(dicts)))
# Total sum: {'I': 7, 'M': 2, 'A': 3, 'F': 1, 'U': 2, 'R': 2, 'S': 5, 'O': 2, 'D': 2, 'L': 3}

all_numbers = [a1, a2, a3]
dicts_numbers = []
for numbers in all_numbers:
    print(frequency(numbers))
    # A == 0
    # {1: 1, 6: 1, 9: 2, 13: 1, 18: 1, 19: 1, 21: 1}
    # {1: 1, 4: 1, 9: 3, 12: 1, 13: 1, 15: 1, 19: 3, 21: 1}
    # {1: 1, 4: 1, 9: 2, 12: 2, 15: 1, 18: 1, 19: 1}

    dicts_numbers.append(frequency(numbers))

print("\nTotal sum: {}".format(sum_freqs(dicts_numbers)))
# Total sum: {1: 3, 6: 1, 9: 7, 13: 2, 18: 2, 19: 5, 21: 2, 4: 2, 12: 3, 15: 2}

def sort_numbers (message):

    solution = ""
    for number in sorted(message.split("-"), key = lambda y: int(y)):
        solution += number + "-"

    return solution[:len(solution)-1]

for message in [message1, message2, message3]:
    print(sort_numbers(message))
    # 1-6-9-9-13-18-19-21
    # 1-4-9-9-9-12-13-15-19-19-19-21
    # 1-4-9-9-12-12-15-18-19
