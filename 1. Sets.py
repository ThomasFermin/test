bruin = {"Boxtel", "Best", "Eindhoven", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}
groen = {"Boxtel", "Best", "Eindhoven", "Geldrop", "Heeze", "Weert"}
print("Dit zijn de stations die alleen op het bruine traject voorkomen: {}".format(bruin.intersection(groen)))
print("De treinstations die wel op het bruine traject voorkomen en niet op het groene traject zijn: {}".format(bruin.difference(groen)))
print("Dit zijn alle stations die op het plaatje voorkomen: {}".format(bruin.union(groen)))