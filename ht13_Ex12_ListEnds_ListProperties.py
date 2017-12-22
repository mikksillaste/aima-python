a = [5, 10, 15, 20, 25]
b = [11, 15, 176, 555, 43]


# funktsioon mis teeb uue listi ainult esimesest ja viimasest arvust antud listis
def newList(list):
    newlist = [list[0], list[-1]]
    return newlist


print(newList(a))
print(newList(b))