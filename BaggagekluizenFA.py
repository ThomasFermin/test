file = open("kluizen.txt")
print("Typ het nummer in van uw menukeuze: ")
menu=int(input("1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug\n5: Ik wil stoppen\n"))

def menu_input():
    choice = True
    while choice:
        if menu > 0 and menu < 5:
            return menu
        elif menu == 5:
            print("Het programma sluit nu af.")
            exit()
        else:
            print("\nDeze optie bestaat niet, toets alstublieft de juiste toets in\n")

def toon_aantal_kluizen_vrij():
    occupied = sum(1 for line in open('kluizen.txt'))
    free = 12 - occupied
    print("There are {} free lockers".format(free))

def nieuwe_kluis():



"""def kluis_openen():


def kluis_teruggeven():"""

menu_input()

if menu == 1:
    toon_aantal_kluizen_vrij()
elif menu == 2:
    nieuwe_kluis()
elif menu == 3:
    kluis_openen()
elif menu == 4:
    kluis_teruggeven()


file.close()