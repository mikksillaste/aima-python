number = int(input("Sisesta number: "))

# teeb listi 1 kuni sisestatud number
numberRange = list(range(1, number+1))

# uus list jagajate jaoks
divisorList = []

# arvutab jagajad ja paneb jagajate listi
for element in numberRange:
    jagatis = number % element
    if jagatis == 0:
        divisorList.append(element)

print(divisorList)
