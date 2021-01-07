import time
import random
import sys
import os
import pyfiglet
import pyfiglet.fonts

# more specific for pyinstaller

from random import sample, shuffle, choice

# stochasicity
from random import randint

# resize the screen if desired
import keyboard  # f11press

# import all dependent modules
from my_modules import sfx

# sound effects for system
from my_modules import hacking_minigame

# race game that can trigger when hacking a node
from my_modules import title_screen

# import the animations for the beginning and ending screens
from my_modules import hacker_info as info

# store important information about the user during gameplay, track health, etc.
from my_modules import message_random as msg

# random quotes and stuff for gameplay
from my_modules import pt2_code_cracker as pt2

# import the second half of the game, decrypting nexus key!

sfx.play_mp3("art_of_silence.mp3")
# background music for gameplay
num_denials = 3

title_screen.title_screen_show()
# display the title screen, calling from title_screen.py module

ascii_nexus = pyfiglet.figlet_format("THE    NEXUS")
print(ascii_nexus)

######PART 2: CRACKING THE NEXUS KEY#######################
sfx.play_mp3("ErrorInTheCodeFULL.mp3")
# transition to the second part of the game, with new music
pt2.decode_key()
