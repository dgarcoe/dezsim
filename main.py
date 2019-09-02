import simpy

from World import World

world = None

def clock(env,tick):
    while True:
        print("Tick:",env.now)
        yield env.timeout(tick)

if __name__ == "__main__":

    env = simpy.rt.RealtimeEnvironment(factor=1)
    proc = env.process(clock(env,1))

    world = World()

    env.run(until=proc)
