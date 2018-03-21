import search


class HanoiProblem(search.Problem):
    def actions(self, state):
        actions = []

        if state["A"] == [4, 2, 1] and state["B"] == [] and state["C"] == [3]:
            if state["A"][-1] == 1:
                actions.append(("A", "B"))
                actions.append(("A", "C"))
            if state["C"][-1] == 3:
                actions.append(("C", "B"))
        elif state["A"] == [4, 2, 1] and state["B"] == [3] and state["C"] == []:
            if state["A"][-1] == 1:
                actions.append(("A", "B"))
                actions.append(("A", "C"))
            if state["B"][-1] == 3:
                actions.append(("A", "C"))
        elif state["A"] == [4, 2] and state["B"] == [] and state["C"] == [3, 1]:
            if state["A"][-1] == 2:
                actions.append(("A", "B"))
            if state["C"][-1] == 1:
                actions.append(("C", "B"))
        elif state["A"] == [4, 2] and state["B"] == [1] and state["C"] == [3]:
            if state["A"][-1] == 2:
                actions.append(("A", "C"))
            if state["B"][-1] == 1:
                actions.append(("B", "C"))
                actions.append(("B", "A"))
        elif state["A"] == [4, 2] and state["B"] == [3] and state["C"] == [1]:
            if state["A"][-1] == 2:
                actions.append(("A", "B"))
            if state["C"][-1] == 1:
                actions.append(("C", "B"))
                actions.append(("C", "A"))
        elif state["A"] == [4] and state["B"] == [3, 2, 1] and state["C"] == []:
            if state["A"][-1] == 4:
                actions.append(("A", "C"))
            if state["B"][-1] == 1:
                actions.append(("B", "A"))
                actions.append(("B", "C"))
        elif state["A"] == [4] and state["B"] == [] and state["C"] == [3, 2, 1]:
            if state["A"][-1] == 4:
                actions.append(("A", "B"))
            if state["C"][-1] == 1:
                actions.append(("C", "B"))
                actions.append(("C", "A"))
        elif state["A"] == [4, 3] and state["B"] == [] and state["C"] == [2, 1]:
            if state["A"][-1] == 3:
                actions.append(("A", "B"))
            if state["C"][-1] == 1:
                actions.append(("C", "B"))
                actions.append(("C", "A"))
        elif state["A"] == [4, 3] and state["B"] == [2, 1] and state["C"] == []:
            if state["A"][-1] == 3:
                actions.append(("A", "C"))
            if state["B"][-1] == 1:
                actions.append(("B", "C"))
                actions.append(("B", "A"))
        elif state["A"] == [4, 3, 2, 1] and state["B"] == [] and state["C"] == []:
            if state["A"][-1] == 1:
                actions.append(("A", "B"))
                actions.append(("A", "C"))


sample_input = {"A": [4, 2, 1], "B": [], "C": [3]}
sample_output = [("A", "B"), ("A", "C"), ("C", "B")]
