print("Typ het nummer in van uw menukeuze: ")
menu=int(input("1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4:Ik wil stoppen\n"))

def menu_input():
    choice = True
    while choice:
        if menu > 0 and menu < 4:
            return menu
        elif menu == 4:
            print("Het programma sluit nu af.")
            exit()
        else:
            print("\nDeze optie bestaat niet, toets alstublieft de juiste toets in\n")

def toon_aantal_kluizen_vrij():
    file = open("kluizen.txt")
    occupied = file.readlines()
    free = 12 - len(occupied)
    file.close()
    print("Er zijn {} lege kluizen".format(free))

def nieuwe_kluis():
    file = open("kluizen.txt", "r+")
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in file:
        kluisnummer = i.split(";")[0]
        if int(kluisnummer) in list:
            list.remove(int(kluisnummer))
    if len(list) > 0:
        code = input("Voer een code in: ")
        file.write(str(list[0]) + ";" + code + "\n")
        print("Uw kluisnummer = " + str(list[0]))
    else:
        print("Er zijn geen kluizen meer beschikbaar!")
    file.close()

def kluis_openen():
    file = open("kluizen.txt", "r")
    kluis = input("Voer uw kluisnummer in: ")
    code = input("Voer uw kluiscode in: ")
    kluiscombinatie = (kluis + ";" + code)
    kluizen = []
    for i in file:
        i =i.replace("\n", "")
        kluizen.append(i)
    if kluiscombinatie in kluizen:
        print("Uw kluis is open!")
    elif kluiscombinate not in kluizen:
        print("Uw heeft een verkeerde combinatie ingevoerd")
    file.close()


menu_input()

if menu == 1:
    toon_aantal_kluizen_vrij()
elif menu == 2:
    nieuwe_kluis()
elif menu == 3:
    kluis_openen()