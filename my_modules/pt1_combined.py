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

from my_modules import sfx


class P1:
    # hacking minigame
    hack_success = True
    hack_chances = 3
    fw_difficulty = 2000
    # how fast the 'enemy' firewall moves comparative to you, lower is faster
    fw_level = 0
    # inform the user what level firewall the AI is using.
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
    jam_reveal = False  # jammer has not been revealed
    barrier_low = random.randint(1, 50)
    barrier_high = random.randint(50, 100)
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
        sfx.gentle_ui()
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
            P1.make_guess()

    #
    #
    #

    def hacker_history():
        """provide history of choices"""
        status_splash = 0
        while status_splash == 0:
            sfx.gentle_ui()
            ascii_intel = pyfiglet.figlet_format("HACKING HISTORY")
            print(ascii_intel)
            time.sleep(0.5)
            sfx.gentle_ui()
            time.sleep(0.5)
            print("--------------------------")
            sfx.gentle_ui()
            time.sleep(0.5)
            print("--------------------------" * 2)
            sfx.gentle_ui()
            time.sleep(0.5)
            print("--------------------------" * 3)

            print("\nEntry Information:")
            if P1.guess_list == []:
                print("NO ENTRIES COMMITTED YET")
            if P1.guess_list != []:
                print("ENTRIES SO FAR: " + str(P1.guess_list))
            print("\nENTRIES REMAINING UNTIL SYSTEM LOCK: ")
            print("LOW ENTRIES REMAINING: " + str(P1.high_keys))
            print("HIGH ENTRIES REMAINING: " + str(P1.low_keys))

            print("\nJAMMER Information:")
            if P1.jam_reveal == False:
                print("JAMMER RANGE UNKNOWN. PROCEED WITH CAUTION.")
            if P1.jam_reveal == True:
                print(
                    "JAMMER RANGE: "
                    + str(P1.barrier_low)
                    + " to "
                    + str(P1.barrier_high)
                )
            if P1.chances <= 2 and P1.barrier_inside == 2:
                print("The NEXUS KEY is INSIDE the jammer range.")
            elif P1.chances <= 2 and P1.barrier_inside == 1:
                print("The NEXUS KEY is OUTSIDE the jammer range.")
            else:
                print(
                    "We do not know if the NEXUS KEY is in the jammer range."
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
                print("SONAR HISTORY: " + str(P1.sonar_list))

            time.sleep(2)
            print("\nReturning to hacking interface...")
            time.sleep(1)
            status_splash += 1

    def node_hacking_minigame():
        """triggered when hacking a node"""

        def get_equation():
            """
            Returns a math equation string as well as the answer
            """
            global operator
            operator = random.randint(1, 5)

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
            elif operator == 4:
                # multiplication
                hack_verb = random.choice(
                    (
                        "PREVENT",
                        "EXECUTE",
                        "AUTHENTICATE",
                        "ENCRYPT",
                        "DECRYPT",
                        "ANALYZE",
                        "REBUILD",
                        "CIRCUMVENT",
                        "TROUBLESHOOT",
                        "DESTABILIZE",
                        "PROTECT",
                        "QUANTIZE",
                        "INSTALL",
                        "DENY",
                        "PERMIT",
                        "RESTART",
                        "ACCESS",
                        "CONFIRM" "SECURE",
                        "MONITOR",
                        "RECALIBRATE",
                        "BOOT",
                        "HACK",
                        "UPLOAD",
                        "CROSS-REFERENCE",
                        "LOOK UP",
                        "INVESTIGATE",
                        "RESEARCH",
                        "UPDATE",
                        "REVERT",
                        "TRIANGULATE",
                        "COMPILE",
                        "PACKAGE",
                    )
                )
                hack_noun = random.choice(
                    (
                        "DDOS",
                        "FIREWALL",
                        "VPN",
                        "DOMAIN",
                        "IP 192.168.1.1",
                        "MOTHERBOARD",
                        "DARK WEB",
                        "NETWORK",
                        "METADATA",
                        "SECURITY KEY",
                        "BACKDOOR",
                        "DATABASE",
                        "TIP CALCULATOR",
                        "SAFETY NET",
                        "CLOUD SERVER",
                        "COOL ONE-LINER",
                        "COMPUTER JARGON",
                        "MICROSOFT WORD",
                        "HARD DRIVE",
                        "DRONE ARMY",
                        "BRUTE FORCE",
                        "BOTNET",
                        "VERIFICATION",
                        "NODE PASSWORD",
                        "HTTPS DOMAIN",
                        "IP ADDRESS",
                        "EXPLOIT",
                        "USER CREDENTIALS",
                        "MALWARE",
                        "PAYLOAD",
                        "CLOAKING",
                        "ROOTKIT",
                        "ENCRYPTION",
                        "PROTOCOL",
                        "WHITELIST",
                        "ANTIVIRUS",
                    )
                )
                answer = str(hack_verb + " " + hack_noun)
                return (
                    "SYSTEM// ISSUE COMMAND: '{} {}':".format(
                        hack_verb, hack_noun
                    ),
                    answer,
                )
            else:
                # addition with three numbers
                first_number = random.randint(1, 9)
                second_number = random.randint(1, 9)
                third_number = random.randint(1, 9)
                answer = first_number + second_number + third_number
                return (
                    "{} + {} + {} = ".format(
                        first_number, second_number, third_number
                    ),
                    answer,
                )

        def play(stdscr):
            # report back a true or false if the hack succeeded
            """
            Play function
            """
            stdscr.clear()
            sfx.alarm_loop(6)
            # Get window height & width
            height, width = stdscr.getmaxyx()
            title = "COUNTERMEASURES IN PROGRESS"

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

                    if key == 10:  # user presses enter, 10 is the enter button
                        if user_answer.upper().strip() == str(
                            actual_answer
                        ):  # correct answer
                            sfx.burst_sound()
                            # sound
                            stdscr.addstr(y, x, ">" * 25)
                            x = x + 25
                            stdscr.addstr(y, x, ">[~~]>")  # moves user forward
                            # TEN SPACES: "          "
                            (
                                problem,
                                actual_answer,
                            ) = get_equation()  # get new equation
                            stdscr.addstr(
                                start_y_problem,
                                start_x_problem,
                                "                                                            ",
                            )
                            stdscr.addstr(
                                start_y_problem, start_x_problem, problem
                            )  # overwrite old equation
                            stdscr.addstr(
                                start_y_problem,
                                start_x_problem + 60,
                                "                                                            ",
                            )
                            user_answer = ""

                        else:  # incorrect answer
                            user_answer = ""
                            if operator == 4:
                                stdscr.addstr(
                                    start_y_problem,
                                    start_x_problem + 60,
                                    "                                                            ",
                                )
                            else:
                                stdscr.addstr(
                                    start_y_problem,
                                    start_x_problem + 11,
                                    "           ",
                                )
                                enemy_x = enemy_x + 5

                            sfx.bad_sound_hack.play()

                            if alarm_limit == 1:
                                sfx.alarm_loop(random.randint(5, 5))
                                alarm_limit += 1

                    elif (
                        key == 127 or key == 8 or key == 263
                    ):  # user presses backspace
                        user_answer = user_answer[:-1]
                        if operator == 4:
                            stdscr.addstr(
                                start_y_problem,
                                start_x_problem + 60,
                                "                                                            ",
                            )
                        else:
                            stdscr.addstr(
                                start_y_problem,
                                start_x_problem + 11,
                                "           ",
                            )

                    elif key != -1:  # user adds character to their answer
                        user_answer = user_answer + str(chr(key))
                        # number shows user input start
                    if operator == 4:
                        stdscr.addstr(
                            start_y_problem, start_x_problem + 60, user_answer
                        )  # update user answer
                    else:
                        stdscr.addstr(
                            start_y_problem, start_x_problem + 11, user_answer
                        )  # update user answer

                finished = True

                if x >= x_finish - 4:  # check if user won or lost
                    winner = True

            stdscr.clear()

            if winner == True:
                title = "NODE ENTRY GAINED"
                subtitle = "[System] Security has been HEIGHTENED."
                pygame.mixer.stop()
                sfx.success()
                sfx.burst_sound()
                P1.hack_success = True
                P1.fw_difficulty -= 500
                # make the enemy move faster
                P1.fw_level += 1
                # increase the 'level difficulty' by one
                curses.endwin()

            else:
                sfx.fail_corrupt()
                title = "NODE ENTRY DENIED"
                subtitle = "[System] Security has been LOWERED."
                # nexus_main.num_denials -=1
                pygame.mixer.stop()
                sfx.burst_sound()
                sfx.fail_corrupt()
                P1.hack_success = False
                P1.fw_difficulty += 1000
                # make the enemy move slower
                P1.fw_level -= 2
                # reduce the 'level difficulty' by one
                P1.tripwire = True
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

            while k != curses.KEY_ENTER and k != 10 and k != 13:
                # repeat until user enters an option

                # Get window height & width
                height, width = stdscr.getmaxyx()

                # Decorate main menu
                title = "FIREWALL DETECTED"
                if P1.fw_level > 2:
                    subtitle1 = "INCREDIBLY HIGH SECURITY"
                if P1.fw_level == 2:
                    subtitle1 = "VERY HIGH SECURITY"
                if P1.fw_level == 1:
                    subtitle1 = "HIGH SECURITY"
                if P1.fw_level == 0:
                    subtitle1 = "INTERMEDIATE SECURITY"
                if P1.fw_level == -1:
                    subtitle1 = "LOW SECURITY"
                if P1.fw_level == -2:
                    subtitle1 = "VERY LOW SECURITY"
                if P1.fw_level < -2:
                    subtitle1 = "INCREDIBLY LOW SECURITY"
                subtitle2 = "PRESS 'ENTER' TO BEGIN HACK."
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

            if k == curses.KEY_ENTER or k == 10 or k == 13:
                play(stdscr)

        curses.wrapper(main)

    def assess_guess():
        P1.chances -= 1
        if P1.tripwire == False:
            if P1.guess < P1.entry_key:
                """if guess is lower than the nexus key"""
                P1.high_keys -= 1
                if P1.high_keys != 0:
                    sfx.appear_blip()
                    print(
                        "LOW ENTRY\n"
                        + "REMAINING CHANCES: "
                        + str(P1.high_keys)
                        + " LOW, "
                        + str(P1.low_keys)
                        + " HIGH"
                    )
                    time.sleep(0.5)
                    if P1.high_keys == 1:
                        sfx.appear_blip()
                        sfx.gentle_ui()
                        print(
                            "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                        )
                    time.sleep(1)
                    P1.guess_list.append("(LOW)")

            if P1.guess > P1.entry_key:
                """if guess is higher than the nexus key"""
                P1.low_keys -= 1
                if P1.low_keys != 0:
                    sfx.appear_blip()
                    print(
                        "HIGH ENTRY\n"
                        + "REMAINING CHANCES: "
                        + str(P1.high_keys)
                        + " LOW, "
                        + str(P1.low_keys)
                        + " HIGH"
                    )
                    time.sleep(0.5)
                    if P1.low_keys == 1:
                        sfx.appear_blip()
                        sfx.gentle_ui()

                        print(
                            "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                        )
                    time.sleep(1)
                    P1.guess_list.append("(HIGH)")

        if P1.tripwire == True:
            sfx.gentle_ui()
            """punishment for landing in defense range"""
            print("JAMMED: NO NODE INFORMATION POSSIBLE")
            print("REDUCING GUESSES OF THE NODE TYPE YOU HAVE MORE OF")
            time.sleep(3)
            if P1.high_keys < P1.low_keys:
                P1.low_keys -= 1
                print("HIGH NODE GUESSES REDUCED BY 1")
            elif P1.high_keys > P1.low_keys:
                P1.high_keys -= 1
                print("LOW NODE GUESSES REDUCED BY 1")
            elif P1.high_keys == P1.low_keys:
                print("HIGH AND LOW NODES ARE EQUAL. DECIDING RANDOMLY...")
                time.sleep(1)
                coin_flip = random.randint(1, 2)
                if coin_flip == 1:
                    P1.high_keys -= 1
                    print("LOW NODE GUESSES REDUCED BY 1")
                if coin_flip == 2:
                    P1.low_keys -= 1
                    print("HIGH NODE GUESSES REDUCED BY 1")
            P1.guess_list.append("(JAMMED)")
            P1.tripwire = False
            print("LOW ENTRIES REMAINING: " + str(P1.high_keys))
            print("HIGH ENTRIES REMAINING: " + str(P1.low_keys))
        # Increase the value of chance by 1
        if P1.chances == 3:
            """disable defense protocol, tripmine"""
            time.sleep(1)
            sfx.gentle_ui()
            ascii_jam_offline = pyfiglet.figlet_format(
                "JAMMER   REVEALED", font="bubble"
            )
            print(ascii_jam_offline)
            time.sleep(1)
            sfx.appear_blip()
            P1.jam_reveal = True  # update jammer coordinates in hacker history
            print(
                "The JAMMER RANGE is covering "
                + str(P1.barrier_low)
                + " to "
                + str(P1.barrier_high)
                + ".\nThere is a 50% chance that the NEXUS KEY has appeared within this range."
            )

    def sonar_alerts():
        """provide sonar, and end game if too many low or high chances"""
        if P1.chances == 3:
            P1.sonar = True
            if P1.sonar == True and (
                ((P1.guess - 30) <= P1.entry_key <= (P1.guess + 30))
                and (0 < P1.guess < 101)
            ):
                time.sleep(1)
                print(" ")
                print(P1.ascii_sonar_status)
                sfx.sonar.play()
                print("NEXUS KEY WITHIN 30 NODES")
                P1.sonar_list.append("KEY WITHIN 30 NODES OF " + str(P1.guess))
            else:
                time.sleep(1)
                print(" ")
                print(P1.ascii_sonar_status)
                sfx.sonar.play()
                print("NEXUS KEY FURTHER THAN 30 NODES AWAY")
                P1.sonar_list.append(
                    "KEY MORE THAN 30 NODES FROM  " + str(P1.guess)
                )

        if P1.chances == 2:
            if P1.sonar == True and (
                ((P1.guess - 20) <= P1.entry_key <= (P1.guess + 20))
                and (0 < P1.guess < 101)
            ):
                time.sleep(1)
                print(" ")
                print(P1.ascii_sonar_status)
                sfx.sonar.play()
                print("NEXUS KEY WITHIN 20 NODES")
                P1.sonar_list.append("KEY WITHIN 20 NODES OF " + str(P1.guess))
            else:
                time.sleep(1)
                print(" ")
                print(P1.ascii_sonar_status)
                sfx.sonar.play()
                print("NEXUS KEY FURTHER THAN 20 NODES AWAY")
                P1.sonar_list.append(
                    "KEY MORE THAN 20 NODES FROM " + str(P1.guess)
                )

        if P1.chances == 2:
            if P1.low_keys != 0 and P1.high_keys != 0:
                time.sleep(1)
                print("\n\nI just confirmed where the NEXUS KEY is situated.")
                time.sleep(1)
                if P1.barrier_inside == 2:
                    print("It's inside the JAMMER RANGE!")
                if P1.barrier_inside == 1:
                    print("It's outside the JAMMER RANGE!")

        if P1.chances == 1:
            if P1.low_keys != 0 and P1.high_keys != 0:
                print(
                    "\nFINAL NODE ENTRY REACHED. LOCKING SYSTEM UPON NEXT FAILURE TO LOCATE NEXUS KEY.\n"
                )
                if P1.sonar == True and (
                    ((P1.guess - 10) <= P1.entry_key <= (P1.guess + 10))
                    and (0 < P1.guess < 101)
                ):
                    P1.sonar10 = True
                    time.sleep(1)
                    print(" ")
                    print(P1.ascii_sonar_status)
                    sfx.sonar.play()
                    print("NEXUS KEY WITHIN 10 NODES")
                    P1.sonar_list.append(
                        "KEY WITHIN 10 NODES OF " + str(P1.guess)
                    )
                else:
                    time.sleep(1)
                    print(" ")
                    print(P1.ascii_sonar_status)
                    sfx.sonar.play()
                    print("NEXUS KEY FURTHER THAN 10 NODES AWAY")
                    P1.sonar_list.append(
                        "KEY MORE THAN 10 NODES FROM " + str(P1.guess)
                    )

        if P1.high_keys == 0 or P1.low_keys == 0:
            P1.chances = 0

    def game():
        """the only called function, manages all other methods"""
        print(P1.entry_key)
        while P1.chances != 0 and P1.guess != P1.entry_key:
            P1.tripwire = False
            # make sure the tripwire starts with a false status, only started by failing hack
            P1.make_guess()
            # user input, and then add to guess list
            if P1.guess != 0:
                # only run if you aren't doing hacker history
                P1.guess_list.append(P1.guess)
                # Compare the user entered number
                # with the number to be guessed

                sfx.click.play()
                # play sfx
                #
                #
                # do hacker minigame if you're in defense range
                if P1.guess != P1.entry_key:
                    if P1.barrier_low < P1.guess < P1.barrier_high:

                        ascii_jammer = pyfiglet.figlet_format(
                            "JAMMER TRIGGERED", font="bubble"
                        )
                        print(ascii_jammer)
                        sfx.appear_blip()
                        print(
                            "\n\nENTRY DETECTED IN JAMMER RANGE. ENGAGING COUNTERMEASURES\n\n"
                        )
                        sfx.hack_node()
                        time.sleep(3)
                        P1.node_hacking_minigame()
                        if P1.hack_success == False:
                            # reduce hack chances by one.
                            print(
                                "NODE INFORMATION JAMMED."
                                + str(P1.hack_chances)
                            )
                    else:
                        sfx.appear_blip()
                        print("JAMMER NOT ACTIVE ON THIS NODE")

                # CONDITIONAL EVENTS BASED ON WHAT CHANCE YOU ARE AT
                # for testing, distable tripwire
                P1.assess_guess()
                # is the guess high or low?
                # reduce chances, or apply jammer stuff
                P1.sonar_alerts()
                # run sonar and assess chances
        #
        #
        # END GAME CONDITIONS
        if P1.guess == P1.entry_key:
            sfx.appear_blip()
            print("NEXUS KEY LOCATED.")
            time.sleep(2)
            sfx.gentle_ui()
            print("EXTRACTING DATA")
            time.sleep(1)
            sfx.gentle_ui()
            ascii_win = pyfiglet.figlet_format("KEY ACQUIRED")
            print(ascii_win)
            time.sleep(5)
            print("Excellent job.")
            time.sleep(2)
            return True
            # move forward

        if P1.extra_chance == True:
            if (
                P1.chances == 0
                and ((P1.guess - 2) <= P1.entry_key <= (P1.guess + 2))
                and (P1.guess != P1.entry_key)
            ):
                sfx.appear_blip()
                print(
                    "The system is falling apart... but it seems like you're so close to the NEXUS KEY that the system is hesitating to kick you out-- It must not want to delete the NEXUS KEY's node by accident.\nIt looks like we have time for one more chance!"
                )
                print("SYSTEM LOCK DELAYED. RECALIBRATING...")
                sfx.alarm_loop(4)
                time.sleep(1)
                print(P1.ascii_sonar_status)
                print("NEXUS KEY WITHIN 2 NODES")
                P1.sonar_list.append("KEY WITHIN 2 NODES OF " + str(P1.guess))
                time.sleep(1)
                print("Let's finish this...")
                P1.make_guess()
                pygame.mixer.stop()

        if P1.guess == P1.entry_key:
            sfx.appear_blip()
            print("NEXUS KEY LOCATED.")
            time.sleep(2)
            sfx.gentle_ui()
            print("EXTRACTING DATA")
            time.sleep(1)
            sfx.gentle_ui()
            ascii_win = pyfiglet.figlet_format("KEY ACQUIRED")
            print(ascii_win)
            time.sleep(5)
            print("Excellent job.")
            time.sleep(2)
            return True
            # move forward

        if (P1.chances == 0) and (P1.guess != P1.entry_key):
            """kill the game if guesses run out"""
            if P1.high_keys == 0:
                print("LOCKING SYSTEM: LOW ENTRY OVERLOAD")
            if P1.low_keys == 0:
                print("LOCKING SYSTEM: HIGH ENTRY OVERLOAD")
            if P1.chances == 0:
                print("MAXIMUM NODE ENTRIES REACHED")
            print(
                "\n\n Denying Nexus entry.\n\nRELEASING KEY CODE: ",
                P1.entry_key,
            )
            time.sleep(6)
            ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
            print(ascii_locked)
            print("THANK YOU FOR VISITING.")
            time.sleep(8)
            return False
            # go back to title screen
