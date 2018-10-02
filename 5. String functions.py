def gemiddelde():
    zin = input("Typ een willekeurige zin: ")
    aantal = len(zin.split())
    letters = len(zin) - zin.count(" ")
    gem = letters / aantal
    print("Het gemiddelde aantal letters per woord is {} letters".format(gem))


gemiddelde()