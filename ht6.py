import search
from collections import deque


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


def step_cost(node, action, next_state):
    return 1


################# kood parandamiseks ######################

def my_search(problem):
    puu_juur = search.Node(problem.initial)
    fringe = deque([puu_juur])
    # how to use deque ("double ended queue"):
    # fringe.append(x)  add x to the end
    # fringe.appendleft(x)  add x to the beginning
    # x = fringe.pop()  remove and return the last item
    # x = fringe.popleft()  remove and return the first item

    # (not quite) infinite loop
    # (quit after 10000 iterations)
    for iter in range(10000):
        if len(fringe) == 0:
            return None
        node = fringe[0]
        if problem.goal_test(node.state):
            return node
        for child_node in expand(node, problem):
            fringe.append(child_node)


def expand(node, problem):
    children = []
    for action in problem.actions(node.state):
        result = problem.result(node.state, action)
        # teeb s <- a new node ja State[s] <- result
        s = search.Node(result)
        s.parent = node
        s.action = action
        s.result = result
        s.path_cost = node.path_cost + step_cost(node, action, result)
        s.depth = node.depth + 1
        children.extend(node.state)
    return children


################# kood parandamiseks l6pp ######################


lihtne = (1, 2, 3, 7, 0, 5, 8, 4, 6)
keskmine = (0, 1, 5, 7, 3, 2, 8, 4, 6)
valmis = (1, 2, 3, 4, 5, 6, 7, 8, 0)
problem = EightPuzzle(lihtne, valmis)

node = my_search(problem)
if node is None:
    print("Not found")
else:
    print(node.solution())
