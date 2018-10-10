def namen():
    names = []
    name = input("Volgende naam: ")
    while True:
        if len(name) > 0:
            names.append(name)
            name = input("Volgende naam: ")
        else:
            break
    counter = {x:names.count(x) for x in names}
    for key, value in counter.items():
        print("Er zijn {} studenten met de naam {}".format(value, key))

namen()