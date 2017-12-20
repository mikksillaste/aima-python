number = int(input("Sisesta number: "))
check = int(input("Sisesta jagaja: "))


def paarisPaaritu(number):
    oddOrEven = number % 2
    if oddOrEven > 0:
        print("Paaritu")
    else:
        print("Paaris")


def multiple4(number):
    multiple_4 = number % 4
    if multiple_4 == 0:
        print("Is multiple 4")
    else:
        print("Not multiple 4")


def jagamine(number, check):
    jagatis = number % check
    if jagatis == 0:
        print("Jagub: " + str(check))
    else:
        print("Ei jagu: " + str(check))


paarisPaaritu(number)
multiple4(number)
jagamine(number, check)