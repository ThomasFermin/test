invoer = ("5-9-7-1-7-8-3-2-4-8-7-9")
lst=invoer.split("-")
sort=sorted(lst)
lst_max=max(lst)
lst_min=min(lst)
aantal=len(lst)
int_lst = list(map(int, lst))
sum = 0
for i in int_lst:
    sum+=i
average = sum / aantal
print("Gesorteerde list van ints: {}".format(sort))
print("Grootste getal: {} en Kleinste getal: {}".format(lst_max, lst_min))
print("Aantal getallen: {} en Som van de getallen: {}".format(aantal, sum))
print("Gemiddelde: {}".format(average))