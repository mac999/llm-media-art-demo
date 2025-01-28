from psonic import *
import time
from threading import Thread, Condition

set_server_parameter_from_log("127.0.0.1")

def play_music(condition):
	while True:
		with condition:
			condition.notifyAll() # Message to threads      

		beat = 0.33

		melody = [
			E5, E5, F5, G5, G5, F5, E5, D5, C5, C5, D5, E5, E5, D5, D5,
			E5, E5, F5, G5, G5, F5, E5, D5, C5, C5, D5, E5, D5, C5, C5
		]

		# Drum beat pattern
		def play_beat():
			sample(DRUM_HEAVY_KICK, amp=1.5)  # Strong kick drum
			sample(ELEC_CHIME, amp=1.2)  # Electric guitar sample
			sample(BD_ZOME, amp=1.5)
			sleep(beat / 2)

			sample(DRUM_CYMBAL_CLOSED, amp=1.2)  # Closed cymbal
			sample(ELEC_CHIME, amp=0.6)  
			sample(BD_ZOME, amp=0.6)
			sleep(beat / 2)

			sample(DRUM_SNARE_HARD, amp=1.3)  # Strong snare
			sample(ELEC_CHIME, amp=1.2)   
			sample(BD_ZOME, amp=1.3)
			sleep(beat / 2)
			
			sample(DRUM_CYMBAL_CLOSED, amp=1.2)
			sample(ELEC_CHIME, amp=0.6)  
			sample(BD_ZOME, amp=0.6)
			sleep(beat / 2)

		# Melody, Beat Channel Play 
		for note in melody:
			play(note, amp=1.0) # , release=0.2)  # Melody
			play_beat()  # Beat Pattern


condition = Condition()
music_thread = Thread(name='producer', target=play_music, args=(condition,))
music_thread.start()

input("Press Enter to continue...")