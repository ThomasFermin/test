afstandKM=input("Wat is de afstand die u moet reizen in kilometers?: ")
weekendrit=bool(input("Reist u in het weekend? Antwoord 'Ja' of 'Nee' "))
def weekendreis():
    if weekendrit == ("Ja") or ("ja"):
        return weekendrit==True
    elif weekendrit == ("Nee") or ("nee"):
        return weekendrit==False
leeftijd=input("Wat is uw leeftijd?: ")

def standaardprijs(afstandKM):
    afstand=int(afstandKM)
    if afstand < 50 and afstand > 0:
        return afstand * 0.80
    elif afstand > 50:
        return afstand * 0.50 + 15
    else:
        afstand == 0
standaardprijs(afstandKM)

def ritprijs(leeftijd, weekendrit, afstandKM):
    weekendreis()
    standard=standaardprijs(afstandKM)
    if int(leeftijd) < 12 or int(leeftijd) > 64:
        if weekendrit==True:
            print("Uw ritprijs is " + str(standard * 0.65) + " euro.")
        else:
            print("Uw ritprijs is " + str(standard * 0.70) + " euro.")
    elif weekendrit==True and int(leeftijd) > 12 and int(leeftijd) < 65:
        print("Uw ritprijs is " + str(standard * 0.60) + " euro.")
    else:
        print("Uw ritprijs is " + str(standard) + " euro.")
ritprijs(leeftijd, weekendrit, afstandKM)