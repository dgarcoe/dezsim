class Villager :

    def __init__(self,env,dayCycle_pipe):
        self.env = env
        self.dayCycle_pipe = dayCycle_pipe
        self.action = env.process(self.run())

    def run(self):
        while True:
            msg = yield self.dayCycle_pipe.get()

            if msg == "DAY" :
                print("Villager awakens")
            elif msg == "NIGHT":
                print("Villager goes to sleep")
