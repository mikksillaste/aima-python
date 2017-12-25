a = [5, 10, 15, 20, 25, 5, 10, 44, 15, 111, 143]
# a = [1,2,3,4,3,2,1]


# funktsioon, mis teeb listist uue list, kus ei ole duplikaate
def newList(initialList):
    noDuplicatesList = []

    for element in initialList:
        if element not in noDuplicatesList:
            noDuplicatesList.append(element)

    return noDuplicatesList


# sama funktsioon kasutated set'i
def newListSet(initialList):
    return list(set(initialList))


print(newList(a))
print(newListSet(a))

