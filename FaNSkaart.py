def inlezen_beginstation(stations):
    print("De stations in dit traject zijn: {}\n{}".format(stations[0:8], stations[9:]))
    while True:
        start = input("Noem uw beginstation: ")
        if start in stations:
            return start
        else:
            print("Deze trein komt niet in {}.".format(start))

def inlezen_eindstation(stations, beginstation):
    while True:
        end = input("Noem uw eindstation: ")
        if end in stations:
            startindex = stations.index(beginstation) + 1
            endindex = stations.index(end) + 1
            if endindex > startindex:
                return end
            else:
                print("Het eindstation dat u heeft ingevoerd ligt voor het beginstation. probeer opniew.")
        else:
            print("Deze trein komt niet in {}.".format(end))

def omroepen_reis(stations, beginstation, eindstation):
    startindex = stations.index(beginstation) + 1
    endindex = stations.index(eindstation) + 1
    dif = endindex - startindex
    prijs = dif * 5
    sindex = int(startindex)
    eindex = int(endindex) - 1
    print("Het beginstation '{}' is het {}e station in het traject.".format(beginstation, startindex))
    print("Het eindstation '{}' is het {}e station in het traject.".format(eindstation, endindex))
    print("De afstand bedraagt {} station(s).".format(dif))
    print("De prijs van het kaartje is {} euro.".format(prijs))
    tussenstations = stations[sindex:eindex]
    print("Jij stapt in de trein in: {}.\n - {} -\nJij stapt uit in: {}.".format(beginstation, tussenstations, eindstation))

stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk" , "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "'s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)