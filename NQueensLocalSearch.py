import search
import random


class HCNQueens(search.Problem):
    def __init__(self, N):
        self.N = N
        self.initial = [None] * N
        for i in range(N):
            self.initial[i] = random.randint(0, N - 1)

    def actions(self, state):
        acts = []
        for i in range(self.N):
            pos = state[i]
            for j in range(self.N):
                if j == pos: continue
                acts.append((i, j))
        return acts

    def result(self, state, action):
        i, j = action
        newstate = list(state)
        newstate[i] = j
        return newstate

    def conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal

    def value(self, state):
        h = 0
        for col in range(self.N - 1):
            row = state[col]
            for col2 in range(col + 1, self.N):
                row2 = state[col2]
                if self.conflict(row, col, row2, col2):
                    h += 1
        return h

    def hill_climbing(problem):
        current = problem.initial
        curr_value = problem.value(problem.initial)

        while True:
            max_value = 99999

            for action in problem.actions(current):
                neighbor = problem.result(current, action)
                neigh_value = problem.value(neighbor)
                if neigh_value < max_value:
                    max_neighbor = neighbor
                    max_value = neigh_value

            if max_value >= curr_value:
                break
            else:
                current = max_neighbor
                curr_value = max_value
                print(curr_value, current)

        return current


p = HCNQueens(36)
print(p.value(p.initial), p.initial)
# print(p.value([2,1,2,1]))
# print (p.actions(p.initial))
# print (p.result(p.initial,p.actions(p.initial)[0]))
print(search.hill_climbing(p))
