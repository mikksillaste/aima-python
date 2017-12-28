# horisontaalsed jooned, kokku n tükki
def print_horiz_line():
    print(" ---" * board_size)


# vertikaalsed jooned, kokku n+1 tükki
def print_vert_line():
    print("|   " * (board_size + 1))


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    # kasutaja sisestus, mis suurus mängu lauda tahab n x n
    board_size = int(input("What size of game board? "))

# kasutades funktsioone ja kasutaja sisestust prindib vastava mängulaua
    for index in range(board_size):
        print_horiz_line()
        print_vert_line()
    print_horiz_line()