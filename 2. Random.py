import random

def monopolyworp():
    x = random.randrange(1, 7)
    y = random.randrange(1, 7)
    z = x + y
    if x != y:
        print("{} + {} = {}".format(x, y, z))
    elif x == y:
        print("{} + {} = {} (dubbel)".format(x, y, z))
        x = random.randrange(1, 7)
        y = random.randrange(1, 7)
        z = x + y
        if x != y:
            print("{} + {} = {}".format(x, y, z))
        elif x == y:
            print("{} + {} = {} (dubbel)".format(x, y, z))
            x = random.randrange(1, 7)
            y = random.randrange(1, 7)
            z = x + y
            if x != y:
                print("{} + {} = {}".format(x, y, z))
            elif x == y:
                print("{} + {} = {} (direct naar de gevangenis)".format(x, y, z))


monopolyworp()