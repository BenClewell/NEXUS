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

# sound effects forq system
from my_modules import hacking_minigame

# race game that can trigger when hacking a node
from my_modules import title_screen

# import the animations for the beginning and ending screens
from my_modules import hacker_info as info

# store important information about the user during gameplay, track health, etc.
from my_modules import message_random as msg

from my_modules import pt1_combined as pt1

# random quotes and stuff for gameplay
from my_modules import pt2_code_cracker as pt2

# import the second half of the game, decrypting nexus key!q
from importlib import reload

import curses  # make sure you can press enter after the reload


def run_game():

    """run nexus, and move modules between each other"""
    sfx.play_p1_bgm()
    # background music for gameplay

    title_screen.title_screen_show()
    # display the title screen, calling from title_screen.py module

    ascii_nexus = pyfiglet.figlet_format("THE    NEXUS")
    sfx.appear_blip()
    time.sleep(0.5)
    sfx.voice_introduction()
    print(ascii_nexus)
    if pt1.P1.game():
        os.system("cls" if os.name == "nt" else "clear")
        # clear the output in the terminal
        pass
    else:
        os.system("cls" if os.name == "nt" else "clear")
        reload(pt1)
        # clear all stuff from the first part
        run_game()
        # clear the output in the terminal
        # back to title

    ######PART 2: CRACKING THE NEXUS KEY#######################
    sfx.play_p2_bgm()
    # transition to the second part of the game, with new music
    ascii_nexus = pyfiglet.figlet_format("DECRYPT THE KEY")
    sfx.appear_blip()
    print(ascii_nexus)
    if pt2.P2.decode_key():
        pt2.P2.current_stage_timer = False  # kill thread by alerting timer function
        pass
    else:
        pt2.P2.current_stage_timer = False  # kill thread by alerting timer function
        os.system("cls" if os.name == "nt" else "clear")
        reload(pt2)
        reload(pt1)
        os.system("cls" if os.name == "nt" else "clear")
        run_game()
        # clear the output in the terminal
        # back to title


if __name__ == "__main__":
    keyboard.press_and_release("F11")
    time.sleep(2)
    run_game()