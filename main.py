import simpy

from World import World
from Day import Day

world = None
day_duration=30
night_duration=30

def clock(env,tick):
    while True:
        print("Tick:",env.now)
        yield env.timeout(tick)

if __name__ == "__main__":

    env = simpy.rt.RealtimeEnvironment(factor=1)
    proc = env.process(clock(env,1))

    world = World()
    dayCycle = Day(env,day_duration,night_duration)

    env.run(until=proc)
