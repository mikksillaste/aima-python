import agents


def SimpleVacuumAgent():
    def program(percept):
        """Same as ReflexVacuumAgent, except if everything is clean, do NoOp."""
        print(percept)
        location, status = percept

        if status == 'Dirty':
            print('Suck')
            return 'Suck'
        elif location == agents.loc_A:
            print('Right')
            return 'Right'
        elif location == agents.loc_B:
            print('Left')
            return 'Left'

    return agents.Agent(program)


e = agents.TrivialVacuumEnvironment()
e.status = {agents.loc_A: "Dirty", agents.loc_B: "Dirty"}
simple_agent = SimpleVacuumAgent()
e.add_thing(simple_agent)
e.run(10)
print(simple_agent.performance)
