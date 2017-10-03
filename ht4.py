import search

class VacWorld(search.Problem):
    def actions(self, state):
        actions = []
        vac_loc = state["loc"]

        if state[vac_loc] == "Dirty":
            actions.append("Suck")
        if state[vac_loc] == "Clean":
            actions.append("NoOp")

        if vac_loc == "A":
            actions.append("Right")
        if vac_loc == "B":
            actions.append("Right")
            actions.append("Left")
        if vac_loc == "C":
            actions.append("Right")
            actions.append("Left")
        if vac_loc == "D":
            actions.append("Left")

        # if state["loc"] == "A":
        #     if state["A"] == "Dirty":
        #         actions.append("Suck")
        #         actions.append("Right")
        #     elif state["A"] == "Clean":
        #         actions.append("NoOp")
        #         actions.append("Right")
        # elif state["loc"] == "B":
        #     if state["B"] == "Dirty":
        #         actions.append("Suck")
        #         actions.append("Right")
        #         actions.append("Left")
        #     elif state["B"] == "Clean":
        #         actions.append("NoOp")
        #         actions.append("Right")
        #         actions.append("Left")
        # elif state["loc"] == "C":
        #     if state["C"] == "Dirty":
        #         actions.append("Suck")
        #         actions.append("Right")
        #         actions.append("Left")
        #     elif state["C"] == "Clean":
        #         actions.append("Right")
        #         actions.append("Left")
        #         actions.append("NoOp")
        # elif state["loc"] == "D":
        #     if state["D"] == "Dirty":
        #         actions.append("Suck")
        #         actions.append("Left")
        #     elif state["D"] == "Clean":
        #         actions.append("NoOp")
        #         actions.append("Left")

        return actions

    def result(self, state, action):
        newstate = state.copy()
        # action on yks nendest: "Left", "Right", "Suck", "NoOp"
        vac_loc = state["loc"]

        if action == "Suck":
            newstate[vac_loc] = "Clean"
        elif action == "Right":
            if newstate["loc"] == "A":
                newstate["loc"] == "B"
            if newstate["loc"] == "B":
                newstate["loc"] == "C"
            if newstate["loc"] == "C":
                newstate["loc"] == "D"
        elif action == "Left":
            if newstate["loc"] == "B":
                newstate["loc"] == "A"
            if newstate["loc"] == "C":
                newstate["loc"] == "B"
            if newstate["loc"] == "D":
                newstate["loc"] == "C"

        # if state["loc"] == "A":
        #     if action == "Suck":
        #         newstate["A"] == "Clean"
        #     elif action == "Right":
        #         newstate["loc"] == "B"
        # elif state["loc"] == "B":
        #     if action == "Suck":
        #         newstate["B"] == "Clean"
        #     elif action == "Right":
        #         newstate["loc"] == "C"
        #     elif action == "Left":
        #         newstate["loc"] == "A"
        # elif state["loc"] == "C":
        #     if action == "Suck":
        #         newstate["C"] == "Clean"
        #     elif action == "Right":
        #         newstate["loc"] == "D"
        #     elif action == "Left":
        #         newstate["loc"] == "B"
        # elif state["loc"] == "D":
        #     if action == "Suck":
        #         newstate["D"] == "Clean"
        #     elif action == "Left":
        #         newstate["loc"] == "C"

        return newstate

    def goal_test(self, state):

    # kui on kõik puhas siis return true
        if state["A"] == "Clean" and state["B"] == "Clean" and state["C"] == "Clean" and state["D"] == "Clean":
            return True
    # muidu false
        return False

#algoleku kirjeldus 1
algolek = {
    "A" : "Dirty",
    "B" : "Clean",
    "C" : "Clean",
    "D" : "Dirty",
    "loc" : "C"
}

#algoleku kirjeldus 2
#algolek = (1,0,0,1,2)

p=VacWorld(algolek)
#print(p.actions(olek))
asi = search.breadth_first_tree_search(p)
asi = search.iterative_deepening_search(p)
print(asi.solution())
