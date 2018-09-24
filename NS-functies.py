afstandKM=input("Wat is de afstand die u moet reizen in kilometers?: ")
weekendrit=input("Reist u in het weekend? Antwoord True voor Ja en antwoord False voor Nee")
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
    standard=standaardprijs(afstandKM)
    if int(leeftijd) < 12 or int(leeftijd) > 64:
        if weekendrit==True:
            print(standard * 0.65)
        else:
            print(standard * 0.70)
    elif weekendrit==True and int(leeftijd) > 12 and int(leeftijd) < 65:
        print(standard * 0.60)
    else:
        print(standard)
ritprijs(leeftijd, weekendrit, afstandKM)