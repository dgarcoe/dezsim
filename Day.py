class Day:

    def __init__(self,env,day_duration,night_duration,dayCycle_pipe):
        self.env = env
        self.day_duration = day_duration
        self.night_duration = night_duration
        self.dayCycle_pipe = dayCycle_pipe
        self.action = env.process(self.run())

    def run(self):
        while True:
            print("A new day in the world of Gallaecia")
            yield self.env.timeout(self.day_duration)
            self.dayCycle_pipe.put("NIGHT")
            print("The night arrives")
            yield self.env.timeout(self.night_duration)
            self.dayCycle_pipe.put("DAY")
