# kasutaja sisestab 3 numbrit
number1 = int(input("Sisesta esimene arv: "))
number2 = int(input("Sisesta teine arv: "))
number3 = int(input("Sisesta kolmas arv: "))


# funktsioon, mis tagastab kolmes sisestatud arvust suurima
def largest(number1, number2, number3):
    biggest = 0
    if number1 > biggest:
        biggest = number1
    if number2 > number1:
        biggest = number2
    if number3 > number2 and number3 > number1:
        biggest = number3

    return biggest


print(largest(number1, number2, number3))