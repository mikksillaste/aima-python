import agents

clean_room_seen = False


def MyVacuumAgent():
    def program(percept):
        global clean_room_seen
        print(percept)
        location, status = percept
        # model[location] = status  # Update the model here
        # if model[loc_A] == model[loc_B] == 'Clean':
        #    return 'NoOp'
        if status == 'Dirty':
            print('Suck')
            clean_room_seen = True
            return 'Suck'
       # elif clean_room_seen:
       #     return "NoOp"
        elif location == agents.loc_A:
            print('Right')
            clean_room_seen = True
            return 'Right'
        elif location == agents.loc_B:
            print('Left')
            clean_room_seen = True
            return 'Left'

    return agents.Agent(program)


e = agents.TrivialVacuumEnvironment()
e.status = {agents.loc_A: "Dirty", agents.loc_B: "Dirty"}
# e.add_thing(agents.ModelBasedVacuumAgent())
agent1 = MyVacuumAgent()
agent2 = agents.ModelBasedVacuumAgent()
e.add_thing(agent1)

#print(e.status)
e.run(10)
# print(e.status)
print(agent1.performance)
