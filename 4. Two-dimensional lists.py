studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    lst1 = []
    for i in studentencijfers:
        x=sum(i)
        lst1.append(x)
    s_total = list(map(int, lst1))
    for i in s_total:
        y = i/3
        antw.append(y)
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    ans = []
    lst1 = []
    for i in studentencijfers:
        x = sum(i)
        lst1.append(x)
    s_total = list(map(int, lst1))
    for i in s_total:
        y = i / 3
        ans.append(y)
    totaal=sum(ans)
    antw = totaal / len(studentencijfers)
    antw = int(antw)
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))