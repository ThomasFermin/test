import datetime
this_date= datetime.datetime.now()


def seizoen(maand):
    if maand == 12 or maand == 1 or maand == 2:
        print("Het is winter")
    elif maand == 3 or maand == 4 or maand == 5:
        print("Het is lente")
    elif maand == 6 or maand == 7 or maand == 8:
        print("Het is zomer")
    else:
        print("Het is herfst")


seizoen(this_date.strftime("%m"))