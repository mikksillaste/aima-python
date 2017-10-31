from games import minimax_decision

X = 1
O = -1


def actions(state):
    for i in range(9):
        if state[i] is None:
            yield i


def result(a, state):
    newstate = state.copy()
    tomove = state[9]
    newstate[a] = tomove
    newstate[9] = -tomove
    return newstate


def successors(state):
    for a in actions(state):
        s = result(a, state)
        yield (a, s)


def terminal_test(state):
    acts = list(actions(state))
    if not acts:
        return True
    value = utility(state)
    if value != 0:
        return True
    return False


def utility(state):
    triples = [(0, 1, 2),
               (3, 4, 5),
               (6, 7, 8),
               (0, 3, 6),
               (1, 4, 7),
               (2, 5, 8),
               (0, 4, 8),
               (6, 4, 2)]
    for a, b, c in triples:
        if state[a] is None: continue
        if (state[a] == state[b] and
                    state[b] == state[c]):
            if state[a] == MYSIDE:
                return 1
            else:
                return -1
    return 0


algus = [X, O, X,
         O, None, O,
         None, None, None,
         X]
MYSIDE = X

print(minimax_decision(algus))
