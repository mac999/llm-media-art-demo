import random
from psonic import *
from threading import Thread, Condition
from random import choice

set_server_parameter_from_log("127.0.0.1")


def random_riff(condition):
    use_synth(PROPHET)
    sc = scale(E3, MINOR)
    while True:
        s = random.choice([0.125,0.25,0.5])
        with condition:
            condition.wait() #Wait for message
        for i in range(8):
            r = random.choice([0.125, 0.25, 1, 2])
            n = random.choice(sc)
            co = random.randint(30,100)
            play(n, release = r, cutoff = co)
            sleep(s)

def drums(condition):
    while True:
        with condition:
            condition.notifyAll() #Message to threads
        for i in range(16):
            r = random.randrange(1,10)
            sample(DRUM_BASS_HARD, rate=r)
            sleep(0.125)

condition = Condition()
random_riff_thread = Thread(name='consumer1', target=random_riff, args=(condition,))
drums_thread = Thread(name='producer', target=drums, args=(condition,))

random_riff_thread.start()
drums_thread.start()

input("Press Enter to continue...")