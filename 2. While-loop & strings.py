woord = input("Geef een string van vier letters: ")
aantal = len(woord)

while True:
    if aantal != 4:
        print("{} heeft {} letters. Probeer opnieuw.".format(woord, aantal))
        woord = input("Geef een string van vier letters: ")
        aantal = len(woord)
    else:
        print("Inlezen van correcte string: {} is geslaagd".format(woord))
        break