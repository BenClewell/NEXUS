import time
import random
import sys
import os
import pyfiglet
import pyfiglet.fonts
import json
# more specific for pyinstaller

from random import sample, shuffle, choice

# stochasicity
from random import randint

# resize the screen if desired
import keyboard  # f11press

# import all dependent modules
from my_modules import sfx

# sound effects forq system

from my_modules import title_screen

# import the animations for the beginning and ending screens


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
    with open("scores.json") as f:
        champs = json.load(f)
        temp = champs["champions"]
    champs_sorted = sorted(temp, key = lambda k: k['score'], reverse= True)
    champs_unique = []
    for entry in champs_sorted: # take list of top-to-bottom scores and look at each entry
        value = entry['name'] # just the players' names
        if value not in str(champs_unique): # if the player name isn't in the string of sorted players, add them
            champs_unique.append(entry)
        else:
            pass # if the player isn't in the string, don't add them. now you only have unique players.
    champ_iterator = 1
    print('\nTOP FIVE SYSTEM ADMINISTRATORS')
    print('********************************')
    for champ in champs_unique[0:5]:
        if champ_iterator == 1:
            print('1) NEXUS CHAMPION: {} (DATA: {})'.format(champ['name'], champ['score']))
        elif champ_iterator == 2:
            print('2) CHIEF OF SECURITY: {} (DATA: {})'.format(champ['name'], champ['score']))
        elif champ_iterator == 3:
            print('3) INTRUSION ANALYST: {} (DATA: {})'.format(champ['name'], champ['score']))
        elif champ_iterator == 4:
            print('4) MALWARE ENGINEER: {} (DATA: {})'.format(champ['name'], champ['score']))
        else:
            print('5) ENCRYPTION DEVELOPER: {} (DATA: {})'.format(champ['name'], champ['score']))
        champ_iterator +=1
    print('********************************\n\n')
    # PLAYTEST
    # if pt2.P2.decode_key():
    #    pass
    # PLAYTEST
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