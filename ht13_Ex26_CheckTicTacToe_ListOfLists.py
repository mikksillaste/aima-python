def checkGrid(grid):
    # ridade kontroll
    for x in range(0, 3):
        row = {grid[x][0], grid[x][1], grid[x][2]}
        if len(row) == 1 and grid[x][0] != 0:
            return grid[x][0]
    # tulpade kontroll
    for x in range(0, 3):
        column = {grid[0][x], grid[1][x], grid[2][x]}
        if len(column) == 1 and grid[0][x] != 0:
            return grid[0][x]
    # diagonaalode kontroll

# game state on antud list of listina. mõned tests seisundid. 0-on tyhi, 1-player1, 2-player2
winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]