# kasutaja sisestus
userInput = input("Sisesta sõna: ")
word = str(userInput)

# pöörab sõna ümber
reversedWord = word[::-1]

# võrdleb kas palindroom või mitte
if reversedWord == word:
    print("See söna on palindroom: " + reversedWord)
else:
    print("Ei ole palindroom: " + reversedWord)