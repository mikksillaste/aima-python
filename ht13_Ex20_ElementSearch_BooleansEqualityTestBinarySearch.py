a = [5, 10, 15, 20, 25, 44, 111, 143]
# kasutaja sisestab numbri
userInputNumber = int(input("Sisesta number: "))


# funktsioon mis ütleb kas sisestatud number on listis või mitte
def searchNumber(initialList, userInput):
    for element in initialList:
        if element == userInput:
            return True

    return False


# sama, aga binary search
def searchNumberBinary(initialList, userInput):
    start_index = 1
    end_index = len(initialList) - 1

    while True:
        middle_index = (end_index + start_index) // 2 # need to make sure this is an int and also + rather than -

        # changed the following section
        if middle_index == start_index or middle_index == end_index:
            if initialList[middle_index] == userInput or initialList[end_index] == userInput:
                return True
            else:
                return False

        middle_element = initialList[middle_index]
        if middle_element == userInput:
            return True
        elif middle_element > userInput:
            end_index = middle_index
        else:
            start_index = middle_index


print(searchNumber(a, userInputNumber))
print(searchNumberBinary(a, userInputNumber))
