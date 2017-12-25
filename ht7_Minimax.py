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


def minimax_decision(state):
    k = -100
    for a in actions(state):
        p = min_value(result(a, state))
        if p > k:
            k = p
            parim_action = a
    return parim_action


def max_value(state):
    if terminal_test(state):
        return utility(state)
    v = -10
    for (a, s) in successors(state):
        v = max(v, min_value(s))
    return v


def min_value(state):
    if terminal_test(state):
        return utility(state)
    v = 10
    for (a, s) in successors(state):
        v = min(v, max_value(s))
    return v


print(minimax_decision(algus))
