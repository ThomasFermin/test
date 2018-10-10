naam = input("Wat is uw naam? ")
begin = input("Wat is het gewenste beginstation?: ")
eind = input("Wat is het gewenste eindstation?: ")
code1 = (naam + begin + eind)

def code(invoerstring):
    return_string = str()
    for letter in invoerstring:
        return_string += chr(ord(letter) + 3)
    return return_string


print(code(code1))