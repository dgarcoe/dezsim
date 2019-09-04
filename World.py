from Parish import Parish

class World:

    parish_names = [{"name":"Ansemil", "villagers":10},{"name":"Breixa","villagers":30}]
    parishes = []

    def __init__(self,env,dayCycle_pipe):

        for parish in self.parish_names:
            self.parishes.append(Parish(env,parish["name"],parish["villagers"],dayCycle_pipe))
