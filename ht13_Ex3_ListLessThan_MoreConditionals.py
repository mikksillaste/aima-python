number = int(input("Sisesta number: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for element in a:
    if element < number:
        new_list.append(element)

print(new_list)