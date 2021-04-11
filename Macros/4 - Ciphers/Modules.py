# Modules that can be modified or added as needed. Support file for the construction of macros.

class coordinates:

    def default():
        N = "N 41"
        W = "W 008"
        return N, W

    def personalize():
        print("soon")

class ciphers:  

    def morse():
        print("soon")

    def binary():
        print("soon")

    def nato():
        def to_nato(words):
    
            dictionary = {
                            'A' : 'Alfa' ,
                            'B' : 'Bravo' ,
                            'C' : 'Charlie' ,
                            'D' : 'Delta' ,
                            'E' : 'Echo' ,
                            'F' : 'Foxtrot' ,
                            'G' : 'Golf' ,
                            'H' : 'Hotel' ,
                            'I' : 'India' ,
                            'J' : 'Juliett' ,
                            'K' : 'Kilo' ,
                            'L' : 'Lima' ,
                            'M' : 'Mike' ,
                            'N' : 'November' ,
                            'O' : 'Oscar' ,
                            'P' : 'Papa' ,
                            'Q' : 'Quebec' ,
                            'R' : 'Romeo' ,
                            'S' : 'Sierra' ,
                            'T' : 'Tango' ,
                            'U' : 'Uniform' ,
                            'V' : 'Victor' ,
                            'W' : 'Whiskey' ,
                            'X' : 'Xray' ,
                            'Y' : 'Yankee' ,
                            'Z' : 'Zulu' ,
                        }
            
            ponctuation = ['.', '?', '!']
            solution = ""

            for char in words:
                if char.upper() in dictionary.keys():
                    solution += dictionary[char.upper()] + " "
                elif char in ponctuation:
                    solution += char + " "
                else:
                    continue
            
            return solution.strip()