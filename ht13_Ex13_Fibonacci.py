# kasutaja sisestus
howMany = int(input("Mitu fibonacci numbrit prindib: "))


# funktsioon mis prindib nii mitu fibonacci numbrit kui kasutaja küsib
def fibonacciNumbers(howMany):
    i = 1
    fib = []
    if howMany == 0:
        fib = []
    elif howMany == 1:
        fib = [1]
    elif howMany == 2:
        fib = [1, 1]
    elif howMany > 2:
        fib = [1, 1]
        while i < (howMany - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1

    return fib


print(fibonacciNumbers(howMany))