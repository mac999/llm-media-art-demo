from psonic import *

set_server_parameter_from_log("127.0.0.1")

# ELECTRIC SOUNDS
'''
sample(ELEC_TRIANGLE)
sleep(1)
sample(ELEC_SNARE)
sleep(1)
sample(ELEC_LO_SNARE)
sleep(1)
sample(ELEC_HI_SNARE)
sleep(1)
sample(ELEC_MID_SNARE)
sleep(1)
sample(ELEC_CYMBAL)
sleep(1)
sample(ELEC_SOFT_KICK)
sleep(1)
sample(ELEC_FILT_SNARE)
sleep(1)
sample(ELEC_FUZZ_TOM)
sleep(1)
sample(ELEC_CHIME)
sleep(1)
sample(ELEC_BONG)
sleep(1)
sample(ELEC_TWANG)
sleep(1)
sample(ELEC_WOOD)
sleep(1)
sample(ELEC_POP)
sleep(1)
sample(ELEC_BEEP)
sleep(1)
sample(ELEC_BLIP)
sleep(1)
sample(ELEC_BLIP2)
sleep(1)
sample(ELEC_PING)
sleep(1)
sample(ELEC_BELL)
sleep(1)
sample(ELEC_FLIP)
sleep(1)
sample(ELEC_TICK)
sleep(1)
sample(ELEC_HOLLOW_KICK)
sleep(1)
sample(ELEC_TWIP)
sleep(1)
sample(ELEC_PLIP)
sleep(1)
sample(ELEC_BLUP)
'''

# SOUNDS FEATURING GUITARS
'''
sample(GUIT_HARMONICS)
sleep(1)
sample(GUIT_E_FIFTHS)
sleep(1)
sample(GUIT_E_SLIDE)
sleep(1)
sample(GUIT_HARMONICS)
'''

# MISCELLANEOUS SOUNDS
'''
sample(MISC_BURP)
'''

# PERCUSSIVE SOUNDS
'''
sample(PERC_BELL)
'''

# AMBIENT SOUNDS
'''
sample(AMBI_SOFT_BUZZ)
sleep(1)
sample(AMBI_SWOOSH)
sleep(1)
sample(AMBI_DRONE)
sleep(1)
sample(AMBI_GLASS_HUM)
sleep(1)
sample(AMBI_GLASS_RUB)
sleep(1)
sample(AMBI_HAUNTED_HUM)
sleep(1)
sample(AMBI_PIANO)
sleep(1)
sample(AMBI_LUNAR_LAND)
sleep(1)
sample(AMBI_DARK_WOOSH)
sleep(1)
sample(AMBI_CHOIR)
'''

# BASS SOUNDS
'''
sample(BASS_HIT_C)
sleep(1)
sample(BASS_HARD_C)
sleep(1)
sample(BASS_THICK_C)
sleep(1)
sample(BASS_DROP_C)
sleep(1)
sample(BASS_WOODSY_C)
sleep(1)
sample(BASS_VOXY_C)
sleep(1)
sample(BASS_VOXY_HIT_C)
sleep(1)
sample(BASS_DNB_F)
'''

# BASS DRUMS
sleep(1)
sample(BD_ADA)
sleep(1)
sample(BD_PURE)
sleep(1)
sample(BD_808)
sleep(1)
sample(BD_ZUM)
sleep(1)
sample(BD_GAS)
sleep(1)
sample(BD_SONE)
sleep(1)
sample(BD_HAUS)
sleep(1)
sample(BD_ZOME)
sleep(1)
sample(BD_BOOM)
sleep(1)
sample(BD_KLUB)
sleep(1)
sample(BD_FAT)
sleep(1)
sample(BD_TEK)
sleep(1)

for i in range(10):
    sample(BD_TEK)
    sleep(1)

# SOUNDS FOR LOOPING
sample(LOOP_AMEN, rate=1.0)
sample(LOOP_AMEN_FULL)
sample(LOOP_COMPUS)
sample(LOOP_INDUSTRIAL)
sample(LOOP_SAFARI)
sample(LOOP_TABLA)