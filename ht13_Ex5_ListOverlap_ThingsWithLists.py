import random

# random lists
a = random.sample(range(99), 25)
b = random.sample(range(99), 25)

commonElements = []

# vaatan kas element on mõlemas listis
for element in a:
    if element in b and element not in commonElements:
        commonElements.append(element)

print(a)
print(b)
print("Minu: " + str(commonElements))

# sama asi yhe reaga
c = [x for x in set(a) if x in set(b)]

print("Ühe reaga: " + str(c))    