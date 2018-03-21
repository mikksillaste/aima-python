import search
import random

example_array = [-2, 0, 0, -3, 4, -1, 2, 1, -5, 0, 0, -1, 0]
#example_array = [0, 0, 0, 0, 0, -1, 2, -1, 0, 0, 0, 0, 0]
example_inistate = [example_array, 0, len(example_array)]

# example valid output
# [0, 0, -3, 4, -1, 2, 1, -5, 0, 0, -1, 0]  suboptimal
# [4, −1, 2, 1]                             optimal


class MaxSubarrayProblem(search.Problem):
    def value(self, state):
        array, start, end = state
        return sum(array[start:end])

    def actions(self, state):
        # action is picking new start or end
        my_actions = []
        array, start, end = state
        l = len(array)
        if start > 0:
            my_actions.append((start - 1, end))
        if end < l:
            my_actions.append((start, end + 1))
        # these maintain the invariant that start < end
        if start < end - 1:
            my_actions.append((start + 1, end))
        if end > start + 1:
            my_actions.append((start, end - 1))
        return my_actions

    def result(self, state, action):
        array, start, end = state
        newstart, newend = action
        return (array, newstart, newend)

    def neighbors(self, state):
        my_neighbors = []
        for action in self.actions(state):
            my_neighbors.append(self.result(state, action))
        return my_neighbors

def hill_climbing(problem):
    current = problem.initial
    while True:
        # find highest-valued successor
        neighbors = problem.neighbors(current)
        best_neighbor = neighbors[0]
        for next_neighbor in neighbors[1:]:
            if problem.value(next_neighbor) > problem.value(best_neighbor):
                best_neighbor = next_neighbor

        if problem.value(best_neighbor) <= problem.value(current):
            array, start, end = current
            return array[start:end] # solution state as normal array

        current = best_neighbor

#def hill_climbing2(problem):
    # siia oma täiendatud versioon vastavalt ülesande tekstile


example_problem = MaxSubarrayProblem(example_inistate)

print(hill_climbing(example_problem))
#print(hill_climbing2(example_problem))
