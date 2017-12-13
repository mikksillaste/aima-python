import datetime

name = input("Sisesta oma nimi: ")
age = int(input("Sisesta oma vanus: "))
messageCopies = int(input("Sisesta mitu korda prindib: "))

currentYear = datetime.datetime.now().year
yearWhen100 = str((currentYear - age)+100)
print(messageCopies * ("Aasta, millal saad 100: " + yearWhen100 + "\n"))
