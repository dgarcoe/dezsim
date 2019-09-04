from Villager import Villager

class Parish:

    villagers = []

    def __init__(self,env,name, num_villagers,dayCycle_pipe):
        self.name = name
        for i in range(0,num_villagers):
            self.villagers.append(Villager(env,dayCycle_pipe))
