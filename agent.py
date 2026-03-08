import random

def agent_decision():
    load = random.randint(1, 100)

    if load < 50:
        return "private", load
    else:
        return "public", load