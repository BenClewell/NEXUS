import time
import random
import sys
import os
import pyfiglet
import pyfiglet.fonts

from random import sample, shuffle, choice
from random import randint

import sfx


class P1:
    # hacking minigame
    #
    #
    #
    #
    # Player Chances to find the nexus key
    chances = 5  # you have five chances to enter nodes
    low_keys = 3
    high_keys = 3  # you can make three low guesses, and three high guesses.
    #
    #
    #
    firstchance = True  # to track if this is the player's first move
    extra_chance = True  # has the user burnt their bonus 'close' chance?
    #
    #
    #
    guess = ""  # placeholder for player guess value
    guess_list = []
    sonar = False  # begin the game with no use of sonar
    sonar_list = []  # store information about a player's game history

    # USING PYFIGLET TO CREATE COOL TEXT TITLES:
    ascii_sonar_status = pyfiglet.figlet_format(
        "SONAR", font="digital"
    )  # sonar title
    ascii_jam_online = pyfiglet.figlet_format(
        "JAMMER   ONLINE", font="bubble"
    )  # init jammer
    #
    #
    #
    #
    #
    # ESTABLISHING THE DEFENSE RANGE, and LOCATION OF THE NEXUS KEY
    barrier_low = random.randint(25, 50)
    barrier_high = random.randint(50, 75)
    # sets the low and high defense range parameters.
    barrier_inside = random.randint(1, 2)
    # sets 50-50 chance for whether number is in thres or outside
    if barrier_inside == 2:
        entry_key = random.randint(barrier_low, barrier_high)
        # between the two barrier params
    if barrier_inside == 1:
        # outside the two barrier params
        low_high = random.randint(1, 2)
        # if outside, is it lower or higher?
        if low_high == 1:
            entry_key = random.randint(1, barrier_low)
            # it's lower, between one and the low thres
        if low_high == 2:
            entry_key = random.randint(barrier_high, 100)
            # it's higher, between one and the high thres

    tripwire = False
    # has the user set off the defense range?
    collapse = random.randint(2, 2)
    # multiple ints can be passed to collapse for multiple results

    def make_guess():
        """user enters a node guess to find the key
        rejected if entry is too long, or not valid"""
        print(
            "----------------------------------------------\nENTER A NODE (between 1 and 100):\n"
        )
        try:
            valid = True
            P1.guess = int(input())
            if len(str(P1.guess)) > 3 or P1.guess > 100:
                valid = False
                print("This node is TOO HIGH.")
                print("PLEASE ENTER A VALID NODE.")
                P1.make_guess()
        except:
            valid = False
            print("I don't understand this node.")
            print("PLEASE ENTER A VALID NODE.")
            P1.make_guess()
        if valid == True and P1.guess != 0:
            ascii_nodeguess = pyfiglet.figlet_format("NODE  " + str(P1.guess))
            print(ascii_nodeguess)
        if P1.guess == 0:
            P1.hacker_history()

    def reduce_chance():
        P1.chances -= 1

    #
    #
    #

    def hacker_history():
        """provide history of choices"""
        helpmenu = True
        status_splash = True
        while helpmenu == True:
            while status_splash == True:

                ascii_intel = pyfiglet.figlet_format("HACKING HISTORY")
                print(ascii_intel)
                time.sleep(0.5)
                print("--------------------------")
                time.sleep(0.5)
                print("--------------------------" * 2)
                time.sleep(0.5)
                print("--------------------------" * 3)

                print("\nEntry Information:")
                if P1.guess_list == []:
                    print("NO ENTRIES COMMITTED YET")
                if P1.guess_list != []:
                    print("ENTRIES SO FAR: " + str(P1.guess_list))
                print(
                    "MAXIMUM ENTRIES REMAINING UNTIL SYSTEM LOCK: "
                    + str(P1.chances)
                )
                print("LOW ENTRIES REMAINING: " + str(P1.high_keys))
                print("HIGH ENTRIES REMAINING: " + str(P1.low_keys))

                print("\nJAMMER Information:")
                if P1.firstchance == True:
                    print("DEFENSE RANGE UNKNOWN. PROCEED WITH CAUTION.")
                if P1.firstchance == False:
                    print(
                        "DEFENSE RANGE: "
                        + str(barrier_low)
                        + " to "
                        + str(barrier_high)
                    )
                if P1.chances <= 2 and P1.barrier_inside == 2:
                    print("The NEXUS KEY is INSIDE the defense range.")
                elif P1.chances <= 2 and P1.barrier_inside == 1:
                    print("The NEXUS KEY is OUTSIDE the defense range.")
                else:
                    print(
                        "We do not know if the NEXUS KEY is in the defense range."
                    )

                print("\nSonar Information:")
                if P1.sonar == False:
                    print("SONAR OFFLINE")
                if P1.sonar == True:
                    print("SONAR ONLINE")
                    if P1.chances == 3:
                        print("ACCURACY: 30 NUMBER RANGE")
                    if P1.chances == 2:
                        print("ACCURACY: 20 NUMBER RANGE")
                    if P1.chances == 1:
                        print("ACCURACY: 10 NUMBER RANGE")
                if P1.sonar_list == []:
                    print("NO SONAR HISTORY")
                if P1.sonar_list != []:
                    print("SONAR HISTORY: " + str(sonar_list))

                time.sleep(2)
                print("\nReturning to hacking interface...")
                time.sleep(1)
                status_splash = False
                helpmenu = False

    def game():
        """the only called function, manages all other methods"""
        while P1.chances != 0:
            P1.make_guess()
            if P1.guess != 0:
                P1.guess_list.append(P1.guess)
            # Compare the user entered number
            # with the number to be guessed
            P1.reduce_chance()


P1.game()
