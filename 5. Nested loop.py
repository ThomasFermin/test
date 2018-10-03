def tables():
    for x in range (1, 11):
        print("Table for {}".format(x))
        for y in range (1, 11):
            print(x * y, end=" ")
        print()

tables()