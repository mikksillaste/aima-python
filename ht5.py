import search


class EightPuzzle(search.Problem):
    def actions(self, state):
        space = state.index(0)
        row = space // 3
        col = space % 3

        act = []
        if row == 0:
            act.append(state[space + 3])
        elif row == 1:
            act.append(state[space + 3])
            act.append(state[space - 3])
        elif row == 2:
            act.append(state[space - 3])
        if col == 0:
            act.append(state[space + 1])
        elif col == 1:
            act.append(state[space + 1])
            act.append(state[space - 1])
        elif col == 2:
            act.append(state[space - 1])
        return act

    def result(self, state, action):
        newstate = list(state)
        klotsi_idx = newstate.index(action)
        space = newstate.index(0)
        newstate[space] = action
        newstate[klotsi_idx] = 0
        return tuple(newstate)

    def h1(self, node):
        h = 0
        for i in range(9):
            if node.state[i] != 0:
                if node.state[i] != self.goal[i]:
                    h += 1
        return h

    def h2(self, node):
        rightpos = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
        }
        h = 0
        for i in range(9):
            if node.state[i] != 0:
                row = i // 3
                col = i % 3
                goal_row, goal_col = rightpos[node.state[i]]
                h += abs(row - goal_row)
                h += abs(col - goal_col)
        return h


def astar_h1(problem):
    return search.astar_search(problem, problem.h1)


def astar_h2(problem):
    return search.astar_search(problem, problem.h2)


def greedy_h1(problem):
    return search.greedy_best_first_graph_search(problem, problem.h1)


inistate = (1, 2, 3, 7, 0, 5, 8, 4, 6)
test1 = (1, 4, 3, 8, 6, 2, 7, 0, 5)
test2 = (2, 1, 8, 0, 4, 3, 7, 6, 5)
test3 = (2, 1, 8, 4, 6, 3, 0, 7, 5)
test4 = (5, 7, 6, 4, 0, 8, 3, 2, 1)
test5 = (0, 1, 5, 7, 3, 2, 8, 4, 6)

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# problem = EightPuzzle(inistate, goal)
problem = EightPuzzle(test5, goal)
problem2 = EightPuzzle(test4, goal)

# print(problem.actions(goal))
# print(problem.result(inistate, 7))

# asi = search.breadth_first_tree_search(problem)
# asi = search.breadth_first_search(problem)
# asi = search.astar_search(problem, problem.h2)
#asi = greedy_h1(problem)
#print(asi.solution())
# print(asi.path())

search.compare_searchers([problem], None, [search.iterative_deepening_search, greedy_h1, astar_h1, astar_h2])
