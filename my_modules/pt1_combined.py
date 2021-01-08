import time
import random
import sys
import os
import pyfiglet
import pyfiglet.fonts
import curses
import pygame
from pygame import mixer

from random import sample, shuffle, choice
from random import randint

import sfx


class P1:
    # hacking minigame
    hack_success = True
    hack_chances = 3
    fw_difficulty = 2000
    # how fast the 'enemy' firewall moves comparative to you, lower is faster
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
        print("\n----------------------------------------------\n")

        if P1.tripwire == False:
            if P1.guess < P1.entry_key:
                """if guess is lower than the nexus key"""
                P1.high_keys -= 1
                if P1.high_keys != 0:
                    print(
                        "LOW NODE ENTRY DETECTED: "
                        + str(P1.high_keys)
                        + " LOW ENTRIES UNTIL SYSTEM LOCK"
                    )
                    time.sleep(0.5)
                    if P1.high_keys == 1:
                        print(
                            "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                        )
                    time.sleep(1)
                    P1.guess_list.append("(LOW)")

            else:
                """if guess is higher than the nexus key"""
                P1.low_keys -= 1
                if P1.low_keys != 0:
                    print(
                        "HIGH NODE ENTRY DETECTED: "
                        + str(P1.low_keys)
                        + " HIGH ENTRIES UNTIL SYSTEM LOCK"
                    )
                    time.sleep(0.5)
                    if P1.low_keys == 1:
                        print(
                            "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                        )
                    time.sleep(1)
                    P1.guess_list.append("(HIGH)")

        if P1.tripwire == True:
            """punishment for landing in defense range"""
            P1.high_keys -= 1
            P1.low_keys -= 1
            print("JAMMED: NO NODE INFORMATION POSSIBLE")
            print("LOW NODE GUESSES REDUCED BY 1")
            print("HIGH NODE GUESSES REDUCED BY 1")
            P1.guess_list.append("(JAMMED)")
            P1.tripwire = False

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

    def node_hacking_minigame():
        """triggered when hacking a node"""

        def get_equation():
            """
            Returns a math equation string as well as the answer
            """

            operator = random.randint(1, 4)

            if operator == 1:
                # addition
                first_number = random.randint(10, 30)
                second_number = random.randint(10, 30)
                answer = first_number + second_number
                return "{} + {} =".format(first_number, second_number), answer

            elif operator == 2:
                # subtraction
                first_number = random.randint(30, 50)
                second_number = random.randint(10, 20)
                answer = first_number - second_number
                return "{} - {} =".format(first_number, second_number), answer
            elif operator == 3:
                # multiplication
                first_number = random.randint(3, 12)
                second_number = random.randint(3, 12)
                answer = first_number * second_number
                return "{} * {} =".format(first_number, second_number), answer
            else:
                # addition with three numbers
                first_number = random.randint(1, 9)
                second_number = random.randint(1, 9)
                third_number = random.randint(1, 9)
                answer = first_number + second_number + third_number
                return (
                    "{} + {} + {} =".format(
                        first_number, second_number, third_number
                    ),
                    answer,
                )

        def play(stdscr):
            global hack_success
            # report back a true or false if the hack succeeded
            """
            Play function
            """

            stdscr.clear()
            sfx.alarm_loop(6)
            # Get window height & width
            height, width = stdscr.getmaxyx()
            title = "NODE COUNTERMEASURES IN PROGRESS"

            # get various x,y coordinates according to user's window size
            start_x_title = int(
                (width // 2) - (len(title) // 2) - len(title) % 2
            )
            start_y_title = int((height // 4) - 2)

            start_x_problem = int((width // 2) - 4)
            start_y_problem = int((3 * height // 4))

            enemy_x = int(width // 8)
            enemy_y = int((height // 2) - 1)

            x = int(width // 8)
            y = int((height // 2) + 1)

            x_finish = int((width // 8) * 7)

            finished = False

            winner = False

            while finished == False:  # iterate until user finishes game
                stdscr.addstr(start_y_title, start_x_title, title)

                stdscr.addstr(enemy_y + -2, x_finish - 3, "NODE")
                stdscr.addstr(enemy_y + -1, x_finish, "|")
                stdscr.addstr(enemy_y, x_finish, "|")
                stdscr.addstr(enemy_y + 1, x_finish, "|")
                stdscr.addstr(enemy_y + 2, x_finish, "|")
                stdscr.addstr(enemy_y + 3, x_finish, "|")

                # get initial equation
                problem, actual_answer = get_equation()

                stdscr.addstr(start_y_problem, start_x_problem, problem)

                counter = 1

                stdscr.nodelay(
                    True
                )  # make sure it doesnt stop to get a character

                user_answer = ""
                alarm_limit = 1

                while enemy_x < x_finish - 4 and x < x_finish - 4:

                    key = stdscr.getch()

                    stdscr.addstr(enemy_y, enemy_x, ">[XX]>")

                    stdscr.addstr(y, x, ">[~~]>")

                    # the number after counter mod increases enemy speed
                    if counter % P1.fw_difficulty == 0:
                        enemy_x = enemy_x + 1

                    counter = counter + 1

                    stdscr.refresh()

                    if key == 10:  # user presses enter
                        if user_answer == str(actual_answer):  # correct answer
                            sfx.burst_sound()
                            # sound
                            stdscr.addstr(y, x, ">" * 25)
                            x = x + 25
                            stdscr.addstr(y, x, ">[~~]>")  # moves user forward

                            (
                                problem,
                                actual_answer,
                            ) = get_equation()  # get new equation
                            stdscr.addstr(
                                start_y_problem, start_x_problem, "          "
                            )
                            stdscr.addstr(
                                start_y_problem, start_x_problem, problem
                            )  # overwrite old equation
                            stdscr.addstr(
                                start_y_problem,
                                start_x_problem + 10,
                                "          ",
                            )
                            user_answer = ""

                        else:  # incorrect answer
                            user_answer = ""
                            stdscr.addstr(
                                start_y_problem,
                                start_x_problem + 10,
                                "          ",
                            )
                            enemy_x = enemy_x + 5
                            sfx.bad_sound_hack.play()

                            if alarm_limit == 1:
                                sfx.alarm_loop(random.randint(1, 5))
                                alarm_limit += 1

                    elif key == 127:  # user presses backspace
                        user_answer = user_answer[:-1]
                        stdscr.addstr(
                            start_y_problem, start_x_problem + 10, "          "
                        )

                    elif key != -1:  # user adds character to their answer
                        user_answer = user_answer + str(chr(key))

                    stdscr.addstr(
                        start_y_problem, start_x_problem + 10, user_answer
                    )  # update user answer

                finished = True

                if x >= x_finish - 4:  # check if user won or lost
                    winner = True

            stdscr.clear()

            if winner == True:
                title = "NODE ENTRY GAINED"
                subtitle = "Press any key to unlock contents."
                pygame.mixer.stop()
                P1.hack_success = True
                curses.endwin()

            else:
                title = "NODE ENTRY DENIED"
                subtitle = "Press any key to return to hacking interface."
                # nexus_main.num_denials -=1
                pygame.mixer.stop()
                P1.hack_success = False
                curses.endwin()

            height, width = stdscr.getmaxyx()

            stdscr.addstr(
                int((height // 2) - 2) - 1,
                int((width // 2) - (len(title) // 2) - len(title) % 2),
                title,
            )
            stdscr.addstr(
                int((height // 2) - 2) + 2,
                int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2),
                subtitle,
            )

            stdscr.nodelay(False)  # pause until user enters a character

            stdscr.getch()

            # curses.wrapper(main)  # back to main function

        def main(stdscr):

            k = 0  # user input

            # clear and refresh
            stdscr.clear()
            stdscr.refresh()

            while k not in [
                ord("q"),
            ]:  # repeat until user enters an option

                # Get window height & width
                height, width = stdscr.getmaxyx()

                # Decorate main menu
                title = "FIREWALL DETECTED"
                subtitle1 = ""
                subtitle2 = "PRESS Q TO BEGIN HACK."
                pygame.mixer.unpause()

                start_x_title = int(
                    (width // 2) - (len(title) // 2) - len(title) % 2
                )
                start_x_subtitle = int(
                    (width // 2) - (len(subtitle1) // 2) - len(subtitle1) % 2
                )
                start_y = int((height // 2) - 2)

                stdscr.addstr(start_y - 1, start_x_title, title)
                stdscr.addstr(start_y + 3, start_x_subtitle, subtitle1)
                stdscr.addstr(start_y + 4, start_x_subtitle, subtitle2)

                # Wait for next input
                k = stdscr.getch()

            if k == ord("q"):
                play(stdscr)

        curses.wrapper(main)

    def assess_guess():
        if P1.tripwire == False:
            if P1.guess < P1.entry_key:
                """if guess is lower than the nexus key"""
                P1.high_keys -= 1
                if P1.high_keys != 0:
                    print(
                        "LOW ENTRY\n"
                        + "REMAINING CHANCES: "
                        + str(P1.high_keys)
                        + " LOW, "
                        + str(P1.low_keys)
                        + "HIGH"
                    )
                    time.sleep(0.5)
                    if P1.high_keys == 1:
                        print(
                            "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                        )
                    time.sleep(1)
                    P1.guess_list.append("(LOW)")

            else:
                """if guess is higher than the nexus key"""
                P1.low_keys -= 1
                if P1.low_keys != 0:
                    print(
                        "HIGH ENTRY\n"
                        + "REMAINING CHANCES: "
                        + str(P1.low_keys)
                        + " LOW, "
                        + str(P1.high_keys)
                        + "HIGH"
                    )
                    time.sleep(0.5)
                    if P1.low_keys == 1:
                        print(
                            "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                        )
                    time.sleep(1)
                    P1.guess_list.append("(HIGH)")

        if P1.tripwire == True:
            """punishment for landing in defense range"""
            P1.high_keys -= 1
            P1.low_keys -= 1
            print("JAMMED: NO NODE INFORMATION POSSIBLE")
            print("LOW NODE GUESSES REDUCED BY 1")
            print("HIGH NODE GUESSES REDUCED BY 1")
            P1.guess_list.append("(JAMMED)")
            P1.tripwire = False

        # Increase the value of chance by 1
        if P1.firstchance == True and P1.chances == 5:
            """disable defense protocol, tripmine"""
            time.sleep(1)
            ascii_jam_offline = pyfiglet.figlet_format(
                "JAMMER   OFFLINE", font="bubble"
            )
            print(ascii_jam_offline)
            time.sleep(1)
            print(
                "The DEFENSE RANGE was covering "
                + str(P1.barrier_low)
                + " to "
                + str(P1.barrier_high)
                + ".\nYou should safely be able to access this range of nodes now.\nThere is a 50% chance that the NEXUS KEY is contained within this DEFENSE RANGE."
            )

        P1.chances -= 1
        P1.firstchance = False

    def game():
        """the only called function, manages all other methods"""
        while P1.chances != 0:
            P1.make_guess()
            if P1.guess != 0:
                P1.guess_list.append(P1.guess)
            # Compare the user entered number
            # with the number to be guessed

            sfx.click.play()
            # play sfx
            sfx.hack_node()
            minigame_chance = randint(1, 2)
            #
            #
            if minigame_chance == 1:
                P1.node_hacking_minigame()
                if P1.hack_success == False:
                    P1.hack_chances -= 1
                    # reduce hack chances by one.
                    print(
                        "It looks like you failed your hack. Your hack chances are at "
                        + str(P1.hack_chances)
                    )
            if minigame_chance == 2:
                print("NO FIREWALL DETECTED.")

            # CONDITIONAL EVENTS BASED ON WHAT CHANCE YOU ARE AT
            P1.tripwire = False
            # for testing, distable tripwire
            P1.assess_guess()
            # is the guess high or low?
            P1.reduce_chance()


P1.game()
