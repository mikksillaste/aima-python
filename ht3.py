import search


class MiniSudoku(search.Problem):
    def actions(self, state):
        n = -1

        actions = []
        for i in state:
            n += 1
            y = n // 4
            x = n % 4

            if i == 0:

        return actions

    def result(self, state, action):
        newstate = list(state)

        return tuple(newstate)

    def goal_test(self, state):
        # blah asemel on lõppseisu tingimus
        if len(state[0:4]) == len(set(state[0:4])) and sum(state[4:8]) == len(set(state[4:8]))  and sum(state[8:12]) == len(set(state[8:12])) and sum(state[12:16]) == len(set(state[12:16])):
            return True
        else:
            return False

inistate = (2, 1, 0, 0,
            0, 3, 2, 0,
            0, 0, 0, 4,
            1, 0, 0, 0)
