import search


class MiniSudoku(search.Problem):
    def actions(self, state):
        space = state.index(0)
        row = space // 4
        col = space % 4

        actions = []
        for i in space:
            if i == 0:
                

        return actions

    def result(self, state, action):
        newstate = list(state)

        return tuple(newstate)

    def goal_test(self, state):
        # blah asemel on lõppseisu tingimus
        if blah:
            return True

        return False

inistate = (2, 1, 0, 0,
            0, 3, 2, 0,
            0, 0, 0, 4,
            1, 0, 0, 0)
