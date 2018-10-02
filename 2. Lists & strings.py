lst=[]
for i in range(10):
    x=str(input("Please enter a word: "))
    lst.append(x)
second_list=[]
for string in lst:
    if len(string) == 4:
        second_list.append(string)
    else:
        continue
print("De nieuw-gemaakte lijst met alle vier-letter strings is: {}".format(second_list))