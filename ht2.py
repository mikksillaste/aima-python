import search


class EightPuzzle(search.Problem):
    def actions(self, state):
        space = state.index(0)
        row = space // 3
        col = space % 3

        actions = []
        if row == 0:
            actions.append(state[space + 3])
        elif row == 1:
            actions.append(state[space + 3])
            actions.append(state[space - 3])
        elif row == 2:
            actions.append(state[space - 3])

        if col == 0:
            actions.append(state[space + 1])
        elif col == 1:
            actions.append(state[space + 1])
            actions.append(state[space - 1])
        elif col == 2:
            actions.append(state[space - 1])

        return actions

    def result(self, state, action):
        newstate = list(state)

        klotsi_idx = newstate.index(action)
        space = newstate.index(0)
        newstate[space] = action
        newstate[klotsi_idx] = 0

        return tuple(newstate)

inistate = (1, 2, 3, 7, 0, 5, 8, 4, 6)

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

problem = EightPuzzle(inistate, goal)
#print(problem.actions(goal))
#print(problem.result(inistate, 4))

asi = search.breadth_first_tree_search(problem)
print(asi.solution())
print(asi.path())