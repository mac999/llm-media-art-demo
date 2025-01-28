import pytest
from psonic import *

set_server_parameter_from_log("127.0.0.1")
run("play 60")

play(72)
sleep(1)
play(75)
sleep(1)
play(79) 

play(72)
sleep(1)
play(75)
sleep(1)
play(79) 

play(C5)
sleep(0.5)
play(D5)
sleep(0.5)
play(G5) 

play(Fs5)
sleep(0.5)
play(Eb5)

