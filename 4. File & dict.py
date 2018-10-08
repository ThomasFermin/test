ticker = {}
with open("tckr.txt") as x:
    for line in x:
        (key, val) = line.split(":")
        ticker[str(key)] = val


company = input("Enter a company name: ")
print("Ticker symbol: {}".format(ticker[company]))

#Ik kan niet vinden hoe ik de sleutel uit een dictionary kan krijgen op basis van de value.