import time
import random
import sys
import os
import pyfiglet
import pyfiglet.fonts

# more specific for pyinstaller
import message_random as msg
from random import sample, shuffle, choice

from random import randint

import keyboard  # f11press

import sfx
import hacking_minigame
import title_screen

# audio

sfx.play_mp3("art_of_silence.mp3")
num_denials = 3

title_screen.title_screen_show()
#display the title screen, calling from title_screen.py module

ascii_nexus = pyfiglet.figlet_format("THE    NEXUS")
print(ascii_nexus)
