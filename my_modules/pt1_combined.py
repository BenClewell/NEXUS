import time
import random
import sys
import os
import pyfiglet
import pyfiglet.fonts
import pygame
from pygame import mixer
from alive_progress import alive_bar  # cool loading animations
import pynput
from pynput import keyboard
import curses
from random import sample, shuffle, choice
from random import randint
import string  # generate random lets

from my_modules import sfx

# not yet ## from my_modules import help_guide


class P1:
    given_digits = 4
    allowed_list = sample("0123456789", given_digits)
    #
    node_vulnerable = False  # prevent hacking outside of the specified range
    node_progress_rank = 1
    node_failed_state = False  # has the user failed the last node hack?
    node_progress_speed = 0.1  # become faster each hack
    insertion_finished = False
    # hacking minigame
    hack_success = True
    hack_chances = 3
    fw_difficulty = 4000
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
    guess_string = ""  # text only
    guess_list = []
    sonar = False  # begin the game with no use of sonar
    sonar_list = []  # store information about a player's game history
    special_sonar = False  # give player the option to use SPECIAL SONAR
    special_sonar_limit = 0
    # USING PYFIGLET TO CREATE COOL TEXT TITLES:
    ascii_sonar_status = pyfiglet.figlet_format("SONAR", font="digital")  # sonar title
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
    barrier_high = random.randint(51, 100)
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
    tripwire_tracker = False  # if the player sets off tripwire on nexus key, kill them
    collapse = random.randint(2, 2)
    # multiple ints can be passed to collapse for multiple results

    def make_guess():
        P1.insertion_finished = False
        start_insert = (
            random.choice(
                (
                    10,
                    15,
                    20,
                    25,
                    30,
                    35,
                    40,
                    45,
                    50,
                    55,
                    60,
                    65,
                    70,
                    75,
                    80,
                    85,
                )
            )
            - 1
        )  # put the -1 there so you can be valid with first in range
        end_insert = (
            start_insert + 11
        )  # end for the insertion range, +11 instead of +10 so the range includes both end points
        """the area in which you can perform a node hack"""

        def on_press(key):
            if key == keyboard.Key.enter and P1.node_vulnerable == True:
                sfx.burst_sound()
                P1.node_failed_state = False  # user hacked node successfully
                P1.insertion_finished = True
                time.sleep(1)
                print("[INSERTION VALID]")
            if key == keyboard.Key.enter and P1.node_vulnerable == False:
                sfx.burst_sound()
                P1.node_failed_state = True
                P1.insertion_finished = True
                time.sleep(1)
                print("[INVALID TEST RESPONSE]")

        """user enters a node guess to find the key
        rejected if entry is too long, or not valid"""
        time.sleep(1)
        sfx.gentle_ui()
        print(
            "\n\n---------------------------------------------------\nENTER A NODE (between 1 and 100)\n"
        )
        if P1.allowed_list != []:
            print("[ANTIVIRUS ACTIVE]\nINSERTION POOL: {}".format(P1.allowed_list))
        if len(P1.allowed_list) == 1:
            print(
                "[ANTIVIRUS SHUTTING DOWN] ::: FINAL INTEGER FROM INSERTION POOL MAY BE PAIRED WITH ANY OTHER INTEGER"
            )
        if (
            P1.sonar == True
            and P1.special_sonar == True
            and P1.special_sonar_limit == 0
        ):
            print(
                "[SPECIAL SONAR: EQUIPPED]\n---------------------------------------------------\n"
            )
        elif (
            P1.sonar == True
            and P1.special_sonar == False
            and P1.special_sonar_limit == 0
        ):
            print(
                "[SPECIAL SONAR: INACTIVE]\n---------------------------------------------------\n"
            )
        else:
            print("---------------------------------------------------\n")
        try:
            P1.guess_string = str(input())
            P1.guess = int(P1.guess_string)
            if (len(str(P1.guess))) > 3 or int(P1.guess) > 101:
                valid = False
                print("This node is TOO HIGH.")
                print("PLEASE ENTER A VALID NODE.")

            else:
                if P1.guess != 0 and P1.guess < 101:  # barrier for special stuff
                    if P1.allowed_list != []:
                        duplicates = {}
                        charpass = True  # did character check pass
                        dupes_caught = False
                        string_guess = str(P1.guess)  # i guess this redundant lol
                        for char in P1.guess_string:
                            if (
                                char in P1.allowed_list
                                and len(P1.guess_string) == 1
                                and len(P1.allowed_list) != 1
                            ):
                                valid = False
                                charpass = False
                                sfx.fail_corrupt()
                                print("[ANTIVIRUS]: BLOCKED ACTION")
                                print(
                                    "ERROR: TWO NODES from the INTEGER POOL must be entered to BYPASS ANTIVIRUS"
                                    "\nPlease disable ANTIVIRUS to permit SINGLE-INTEGER ENTRIES"
                                )

                            if char in duplicates and len(P1.allowed_list) != 1:
                                valid = False
                                charpass = False
                                sfx.fail_corrupt()
                                print("[ANTIVIRUS]: BLOCKED ACTION")
                                print(
                                    "ERROR: NO DUPLICATE NODES are allowed to be used for your initial entries."
                                    "\nPlease disable ANTIVIRUS to permit DUPLICATE ENTRIES."
                                )
                                dupes_caught = True

                            else:
                                duplicates[char] = 1
                                #
                                #
                            increment_nonrepeat = (
                                0  # prevent repeat messages, see increment
                            )
                            if (
                                char not in P1.allowed_list
                                and dupes_caught == False
                                and len(P1.allowed_list) != 1
                            ):
                                valid = False
                                charpass = False
                                sfx.fail_corrupt()
                                if increment_nonrepeat == 0:
                                    print("[ANTIVIRUS]: FORBIDDEN ENTRY")
                                    print(
                                        "ERROR: You do not have PERMISSION to access those NODE INTEGERS."
                                        "\nPlease disable ANTIVIRUS to permit nodes outside of the INTEGER POOL."
                                    )
                                else:
                                    pass
                                increment_nonrepeat += (
                                    1  # prevent message from repeating two times
                                )
                            if len(P1.allowed_list) == 1:
                                valid = False
                                charpass = False
                                no_error = False

                                for number in P1.guess_string:
                                    for i in P1.allowed_list:
                                        if i == number:
                                            valid = True  # allow it to pass with any number combo
                                            charpass = True
                                            no_error = True  # don't show error message if stuff is good
                                if no_error == False:
                                    sfx.fail_corrupt()
                                    print(
                                        "[ANTIVIRUS]: FORBIDDEN ENTRY.\nONE INTEGER OF ENTRY MUST MATCH LAST REMAINING ITEM IN POOL"
                                    )

                        if charpass == True and dupes_caught == False:
                            valid = True
                            for number in P1.guess_string:
                                for i in P1.allowed_list:  # remove the used numbers
                                    # PLAYTEST print(
                                    #    "comparing guess int {} to list int {}".format(
                                    #        number, i
                                    #    )
                                    # )
                                    if i == number:
                                        # PLAYTEST print("removing list int {}".format(i))
                                        P1.allowed_list.remove(i)
                            sfx.affirm_sound.play()
                            print(
                                "[ANTIVIRUS]: PERMISSION GRANTED. REMOVING ENTERED NODE FROM INSERTION POOL..."
                            )
                            time.sleep(1)

                            if P1.allowed_list == []:
                                time.sleep(0.5)
                                sfx.gentle_lofi()
                                sfx.success()
                                print("/ INTEGER POOL SATISFIED \\")
                                time.sleep(0.5)
                                print("[**[ANTIVIRUS DISABLED]**]")
                                time.sleep(1.5)
                    else:
                        valid = True
                else:
                    valid = True

        except:
            valid = False
            print("I don't understand this node.")
            print("PLEASE ENTER A VALID NODE.")
            P1.make_guess()
        if valid == False:
            P1.make_guess()

        if valid == True and P1.guess != 0 and P1.guess < 101:
            ascii_nodeguess = pyfiglet.figlet_format("NODE  " + str(P1.guess))
            print(ascii_nodeguess)
            if (
                P1.guess == P1.entry_key
            ):  # alert user they have found the nexus key and alert them of the risks
                time.sleep(0.5)
                sfx.enable_firewall.play()
                sfx.found_node.play()  # you are on the node. be careful!
                print("\nALERT: NEXUS KEY HAS BEEN TARGETED")
                time.sleep(0.5)
                sfx.sonar.play()
                print(
                    "It looks like this node contains the NEXUS KEY. If you trigger the JAMMER now, we will not be able to get in.\nPlease be careful.\n\n"
                )
                time.sleep(2)
                print("GET READY.")
                sfx.burst_sound()
                time.sleep(3)
            sfx.burst_sound()
            print("Node security level {}".format(P1.node_progress_rank))
            print(
                "Press ENTER between {} and {} to hack node.".format(
                    (start_insert + 1), (end_insert)
                )
            )  # +1, to expand range
            time.sleep(1)
            sfx.voice_nodehack()
            time.sleep(2)
            sfx.hack_node()
            #
            listener = keyboard.Listener(on_press=on_press)
            listener.start()
            sfx.loading_loop()
            with alive_bar(
                total=100,
                length=50,
                bar="squares",
                spinner="dots_waves2",
                enrich_print=False,
            ) as bar:  # default setting
                for i in range(100):
                    if P1.insertion_finished == False:
                        if i in range(start_insert, end_insert):
                            P1.node_vulnerable = True
                        else:
                            P1.node_vulnerable = False
                        time.sleep(P1.node_progress_speed)
                        bar()
            time.sleep(1.5)
            pygame.mixer.stop()
            if P1.node_progress_speed > 0.02:
                P1.node_progress_speed -= 0.02
                P1.node_progress_rank += 2
            absorb_input = input(
                ""
            )  # pressing enter to hack counts as entering a node, I guess lol
            listener.stop()
            #
            #
            print("\n")  # call after consuming one item
        if P1.guess == 0:
            P1.hacker_history()
            P1.make_guess()
        if P1.guess == 101:
            P1.sonar_response()
            P1.make_guess()

    #
    #
    #
    def sonar_response():
        if P1.sonar == True and P1.special_sonar_limit == 0:
            if P1.special_sonar == False:
                sfx.gentle_lofi()
                time.sleep(1)
                sfx.sonar.play()
                print("SPECIAL SONAR IS NOW EQUIPPED FOR YOUR NEXT NODE ENTRY.\n\n\n\n")
                P1.special_sonar = True
                return

            if P1.special_sonar == True:
                sfx.gentle_lofi()
                time.sleep(1)
                sfx.sonar.play()
                print("SPECIAL SONAR IS NOW UNEQUIPPED.\n\n\n\n")
                P1.special_sonar = False
                return

        if P1.sonar == False:
            sfx.fail_corrupt()
            print(
                "SONAR has not been activated yet. Please try again once SONAR is online."
            )
            time.sleep(1)

        if P1.special_sonar_limit > 0:
            sfx.fail_corrupt()
            print(
                "ERROR: YOUR SPECIAL SONAR HAS BEEN DISABLED DUE TO OVEREXTENDED RANGE."
            )
            time.sleep(1)

    #
    #
    def hacker_history():
        """provide history of choices"""
        status_splash = True
        while status_splash == True:
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
            if (P1.high_keys == 0 and P1.low_keys == 1) or (
                P1.high_keys == 1 and P1.low_keys == 0
            ):
                print("ENTRY INFORMATION NOT AVAILABLE.")
            else:
                print("LOW ENTRIES REMAINING: " + str(P1.high_keys))
                print("HIGH ENTRIES REMAINING: " + str(P1.low_keys))
            if P1.allowed_list == []:
                print("SYS: ANTIVIRUS DISABLED. ALL NUMBERS AVAILABLE.")
            else:
                print(
                    "SYS: ANTIVIRUS ENABLED. MUST USE INTEGER POOL: {}".format(
                        P1.allowed_list
                    )
                )
            print("\nJAMMER Information:")
            if P1.jam_reveal == False:
                print("JAMMER RANGE UNKNOWN. PROCEED WITH CAUTION.")
            if P1.jam_reveal == True:
                print(
                    "JAMMER RANGE: "
                    + str(
                        P1.barrier_low + 1
                    )  # the +1 corrects the jammer range, since the lowest range point is outside jammer
                    + " to "
                    + str(P1.barrier_high)
                )
            if P1.chances <= 2 and P1.barrier_inside == 2:
                print("The NEXUS KEY is INSIDE the jammer range.")
            elif P1.chances <= 2 and P1.barrier_inside == 1:
                print("The NEXUS KEY is OUTSIDE the jammer range.")
            else:
                print("We do not know if the NEXUS KEY is in the jammer range.")

            print("\nSonar Information:")
            if P1.sonar == False:
                print("SONAR OFFLINE")
            if P1.sonar == True:
                print("SONAR ONLINE")
                if P1.chances == 4:
                    print("NEXT ACCURACY: 30 NUMBER RANGE")
                if P1.chances == 3:
                    print("NEXT ACCURACY: 20 NUMBER RANGE")
                if P1.chances == 2:
                    print("NEXT ACCURACY: 10 NUMBER RANGE")
                if P1.chances == 1:
                    print("NEXT ACCURACY: 2 NUMBER RANGE (IF POSSIBLE)")
            if P1.sonar == True:
                if P1.special_sonar == True and P1.special_sonar_limit == 0:
                    print("SPECIAL SONAR IS EQUIPPED ('101' to UNEQUIP)")
                if P1.special_sonar == False and P1.special_sonar_limit == 0:
                    print("SPECIAL SONAR IS INACTIVE ('101' to EQUIP).")
                if P1.special_sonar_limit > 0:
                    print(
                        "SPECIAL SONAR HAS BEEN DISABLED PERMANENTLY (OVEREXTENDED RANGE)"
                    )
            if P1.sonar_list == []:
                print("NO SONAR HISTORY")
            if P1.sonar_list != []:
                print("SONAR HISTORY: " + str(P1.sonar_list))

            time.sleep(2)
            print("\nReturning to hacking interface...")
            time.sleep(1)
            status_splash = False

    def node_hacking_minigame():
        """triggered when hacking a node"""

        def get_equation():
            """
            Returns a math equation string as well as the answer
            """
            global operator
            operator = random.randint(0, 6)
            if operator == 0:
                scrambled_letters = string.ascii_lowercase
                random_lets = random.sample(
                    scrambled_letters, k=4
                )  # make a string randomly
                answer_lets = ""
                answer_lets = answer_lets.join(
                    random_lets
                )  # what the user sees when questioned
                response_lets = sorted(random_lets)
                joined_respond = ""
                response_lets = joined_respond.join(
                    response_lets
                )  # what the user needs to type
                answer = str(response_lets).upper()  # user types to succeed
                return (
                    "ALPHABETIZE CODE: {}:".format(
                        answer_lets.upper()  # the string to rearrange
                    ),
                    answer,
                )
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
            elif operator == 5:
                # multiplication
                num_type_times = random.randint(10, 20)
                answer = str("I" * num_type_times)
                return (
                    "DDOS ATTACK//: INPUT 'I' {} TIMES:".format(num_type_times),
                    answer,
                )
            elif operator == 4:
                # multiplication
                hack_verb = random.choice(
                    (
                        "PREVENT",
                        "EXECUTE",
                        "AUTHENTICATE",
                        "ENCRYPT",
                        "DECRYPT",
                        "ANONYMIZE",
                        "ANALYZE",
                        "REBUILD",
                        "CIRCUMVENT",
                        "TROUBLESHOOT",
                        "DESTABILIZE",
                        "PROTECT",
                        "DEPLOY",
                        "IMPLEMENT",
                        "QUANTIZE",
                        "INSTALL",
                        "DENY",
                        "DOWNLOAD",
                        "PERMIT",
                        "RESTART",
                        "ACCESS",
                        "CONFIRM",
                        "SECURE",
                        "MONITOR",
                        "REPAIR",
                        "RECALIBRATE",
                        "BOOT",
                        "HACK",
                        "UPLOAD",
                        "REFERENCE",
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
                        "IP ADDRESS",
                        "MOTHERBOARD",
                        "DARK WEB",
                        "NETWORK",
                        "METADATA",
                        "SECURITY KEY",
                        "BACKDOOR",
                        "BLACKLIST",
                        "DATABASE",
                        "STATIC VARIABLES",
                        "SAFETY NET",
                        "CLOUD SERVER",
                        "COMPUTER JARGON",
                        "HARD DRIVE",
                        "LOCAL SERVER",
                        "REPOSITORY",
                        "DRONE ARMY",
                        "BRUTE FORCE",
                        "BOTNET",
                        "INSTALLER",
                        "VERIFICATION",
                        "NODE PASSWORD",
                        "HTTPS DOMAIN",
                        "EXPLOIT",
                        "USER CREDENTIALS",
                        "MALWARE",
                        "PAYLOAD",
                        "COMMAND LINE",
                        "OUTDATED SOFTWARE",
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
                    "INPUT_SYS_CMD//: '{} {}':".format(hack_verb, hack_noun),
                    answer,
                )
            else:
                # addition with three numbers
                first_number = random.randint(1, 9)
                second_number = random.randint(1, 9)
                third_number = random.randint(1, 9)
                answer = first_number + second_number + third_number
                return (
                    "{} + {} + {} = ".format(first_number, second_number, third_number),
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
            enemy_jump = 5

            # get various x,y coordinates according to user's window size
            start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
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

                stdscr.nodelay(True)  # make sure it doesnt stop to get a character

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
                            if operator == 4 or operator == 5 or operator == 0:
                                stdscr.addstr(
                                    start_y_problem,
                                    start_x_problem + 60,
                                    "                                                            ",
                                )
                            else:
                                stdscr.addstr(
                                    start_y_problem,
                                    start_x_problem + 12,
                                    "           ",
                                )
                            stdscr.addstr(enemy_y, enemy_x, "*" * enemy_jump)
                            enemy_x = enemy_x + int(enemy_jump)
                            enemy_jump += 5  # make the next wrong answer more punishing

                            sfx.bad_sound_hack.play()

                            if alarm_limit == 1:
                                sfx.alarm_loop(random.randint(5, 5))
                                alarm_limit += 1

                    elif key == 127 or key == 8 or key == 263:  # user presses backspace
                        user_answer = user_answer[:-1]
                        if operator == 4 or operator == 5 or operator == 0:
                            stdscr.addstr(
                                start_y_problem,
                                start_x_problem + 60,
                                "                                                            ",
                            )
                        else:
                            stdscr.addstr(
                                start_y_problem,
                                start_x_problem + 12,
                                "           ",
                            )

                    elif key != -1:  # user adds character to their answer
                        user_answer = user_answer + str(chr(key))
                        # number shows user input start
                    if operator == 4 or operator == 5 or operator == 0:
                        stdscr.addstr(
                            start_y_problem, start_x_problem + 60, user_answer
                        )  # update user answer
                    else:
                        stdscr.addstr(
                            start_y_problem, start_x_problem + 12, user_answer
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
                if P1.fw_difficulty > 500:
                    P1.fw_difficulty -= 500  # can't go to zero
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

                start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
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
        if (
            P1.node_failed_state == False
        ):  # only provide info if the node is hacked successfully
            time.sleep(1.5)  # finish other thread first
            if P1.tripwire == False:
                P1.chances -= 1
                if P1.guess < P1.entry_key:
                    """if guess is lower than the nexus key"""
                    P1.high_keys -= 1
                    if P1.high_keys != 0:
                        sfx.appear_blip()
                        sfx.voice_too_low()
                        print(
                            "LOW ENTRY\n"
                            + "REMAINING CHANCES: "
                            + str(P1.high_keys)
                            + " LOW, "
                            + str(P1.low_keys)
                            + " HIGH"
                        )
                        time.sleep(0.5)

                        time.sleep(1)
                        P1.guess_list.append("(LOW)")
                        if P1.high_keys == 1:
                            sfx.appear_blip()
                            sfx.gentle_ui()
                            sfx.voice_warning_low_entries()
                            print(
                                "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                            )
                if P1.guess > P1.entry_key:
                    """if guess is higher than the nexus key"""
                    P1.low_keys -= 1
                    if P1.low_keys != 0:
                        sfx.appear_blip()
                        sfx.voice_too_high()
                        print(
                            "HIGH ENTRY\n"
                            + "REMAINING CHANCES: "
                            + str(P1.high_keys)
                            + " LOW, "
                            + str(P1.low_keys)
                            + " HIGH"
                        )
                        time.sleep(0.5)
                        time.sleep(1)
                        if P1.low_keys == 1:
                            sfx.appear_blip()
                            sfx.gentle_ui()
                            sfx.voice_warning_high_entries()

                            print(
                                "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                            )
                        P1.guess_list.append("(HIGH)")

            if P1.tripwire == True:
                P1.chances -= 1
                time.sleep(1.5)  # let the other thread finish first
                sfx.gentle_ui()
                sfx.voice_node_fail()  # reassure player
                """punishment for landing in defense range"""
                print("JAMMED: NO NODE INFORMATION POSSIBLE")
                print("REDUCING GUESSES OF THE NODE TYPE YOU HAVE MORE OF")
                time.sleep(3)
                if P1.high_keys < P1.low_keys:
                    P1.low_keys -= 1
                    print("HIGH NODE GUESSES REDUCED BY 1")
                    if P1.low_keys == 1:
                        sfx.appear_blip()
                        sfx.gentle_ui()
                        time.sleep(1)
                        sfx.voice_warning_high_entries()
                        print(
                            "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                        )
                elif P1.high_keys > P1.low_keys:
                    P1.high_keys -= 1
                    print("LOW NODE GUESSES REDUCED BY 1")
                    if P1.high_keys == 1:
                        sfx.appear_blip()
                        sfx.gentle_ui()
                        time.sleep(1)
                        sfx.voice_warning_low_entries()
                        print(
                            "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                        )
                elif P1.high_keys == P1.low_keys:
                    print("HIGH AND LOW NODES ARE EQUAL. DECIDING RANDOMLY...")
                    time.sleep(1)
                    coin_flip = random.randint(1, 2)
                    if coin_flip == 1:
                        P1.high_keys -= 1
                        print("LOW NODE GUESSES REDUCED BY 1")
                        if P1.high_keys == 1:
                            sfx.appear_blip()
                            sfx.gentle_ui()
                            time.sleep(1)
                            sfx.voice_warning_low_entries()
                            print(
                                "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                            )
                    if coin_flip == 2:
                        P1.low_keys -= 1
                        print("HIGH NODE GUESSES REDUCED BY 1")
                        if P1.low_keys == 1:
                            sfx.appear_blip()
                            sfx.gentle_ui()
                            time.sleep(1)
                            sfx.voice_warning_high_entries()
                            print(
                                "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                            )
                P1.guess_list.append("(JAMMED)")
                P1.tripwire = False  # disa
                print("LOW ENTRIES REMAINING: " + str(P1.high_keys))
                print("HIGH ENTRIES REMAINING: " + str(P1.low_keys))
            # Increase the value of chance by 1
        if P1.chances == 3: #MOVED THIS BACK TO REVEAL NO MATTER WHAT
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
                + str(P1.barrier_low + 1)
                + " to "
                + str(P1.barrier_high)
                + ".\nThere is a 50% chance that the NEXUS KEY has appeared within this range."
            )

    def sonar_alerts():
        """provide sonar, and end game if too many low or high chances"""
        if P1.special_sonar == True:
            sfx.enable_firewall.play()
            print("\n")
            ascii_ss = pyfiglet.figlet_format("SPECIAL SONAR")
            print(ascii_ss)

            def correct_input():
                global input_sonar
                try:
                    input_sonar = int(
                        input(
                            "\nPlease enter a custom value for the RANGE you would like the SONAR to scan for.\n\nSONAR SCAN RANGE: "
                        )
                    )  # gotta be int
                    if input_sonar == 0:
                        # show hacker history if 0 is pressed
                        P1.hacker_history()
                        correct_input()
                except:
                    sfx.fail_corrupt()
                    time.sleep(1)
                    sfx.burst_sound()
                    print(
                        "\nThis appears to be an invalid SONAR RANGE. Please enter a valid number and try again."
                    )
                    correct_input()

            correct_input()
            if P1.sonar == True and (
                ((P1.guess - input_sonar) <= P1.entry_key <= (P1.guess + input_sonar))
                and (0 < P1.guess < 101)
            ):
                time.sleep(1)
                print(" ")
                print(P1.ascii_sonar_status)
                sfx.sonar.play()
                print("NEXUS KEY WITHIN " + str(input_sonar) + " NODES")
                P1.sonar_list.append(
                    "KEY WITHIN " + str(input_sonar) + " NODES OF " + str(P1.guess)
                )
                time.sleep(1)
                print("SPECIAL SONAR IN-RANGE, AND CAN STILL BE USED LATER.")
                sfx.gentle_lofi()
            else:
                time.sleep(1)
                print(" ")
                print(P1.ascii_sonar_status)
                sfx.sonar.play()
                print("NEXUS KEY FURTHER THAN " + str(input_sonar) + " NODES AWAY")
                P1.sonar_list.append(
                    "KEY MORE THAN "
                    + str(input_sonar)
                    + " NODES FROM  "
                    + str(P1.guess)
                )
                time.sleep(1)
                print("SPECIAL SONAR OUT OF RANGE, AND IS NOW PERMANENTLY DISABLED.")
                sfx.fail_corrupt()

                P1.special_sonar_limit += 1  # make it impossible to resummon

        if P1.special_sonar == False:
            if P1.chances == 4:
                P1.sonar = True
                # enable special sonar
                time.sleep(2)
                sfx.enable_firewall.play()
                print("\nSPECIAL SONAR unlocked. (Type '101' to toggle ON/OFF)\n")
                extra_digit = 1
                extra_motivation = 0
                for (
                    i
                ) in (
                    P1.allowed_list
                ):  # give extra number to compensate for one-directional stuff
                    extra_motivation += int(i)
                if extra_motivation / 2 <= 4.5:
                    extra_option = sample("56789", extra_digit)
                if extra_motivation / 2 > 4.5:
                    extra_option = sample("01234", extra_digit)
                for i in extra_option:
                    added_number = str(i)
                print(
                    "EXTRA INSERTION OPTION ADDED TO ANTIVIRUS: {}".format(added_number)
                )
                P1.allowed_list.append(added_number)
            if P1.chances == 3:
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
                    P1.sonar_list.append("KEY MORE THAN 20 NODES FROM " + str(P1.guess))
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
                        P1.sonar_list.append("KEY WITHIN 10 NODES OF " + str(P1.guess))
                    else:
                        time.sleep(1)
                        print(" ")
                        print(P1.ascii_sonar_status)
                        sfx.sonar.play()
                        print("NEXUS KEY FURTHER THAN 10 NODES AWAY")
                        P1.sonar_list.append(
                            "KEY MORE THAN 10 NODES FROM " + str(P1.guess)
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

        if P1.special_sonar_limit > 0:
            P1.special_sonar = False

        if P1.high_keys == 0 or P1.low_keys == 0:
            P1.chances = 0

    def game():
        """the only called function, manages all other methods"""
        # print(P1.entry_key)  # for playtesting
        print(
            random.choice(
                (
                    "We've got this.",
                    "I can't wait to perform today's decryption.",
                    "I'm excited to begin our hack.",
                    "This is going to be a piece of cake.",
                    "This time it's gonna work.",
                )
            )
        )
        print('Press "0" to view your HACKER HISTORY at any time.')
        print(
            "For now, the ANTIVIRUS will prevent us from going outside of the INTEGER POOL."
        )
        print(
            "Construct your NODE ENTRIES using these available integers. The ANTIVIRUS will be weakened as you construct VALID NODES.\n\n"
        )
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
                    if (
                        P1.node_failed_state == False
                    ):  # did not fail initial skill check for node
                        if (P1.barrier_low + 1) < P1.guess < P1.barrier_high:

                            ascii_jammer = pyfiglet.figlet_format(
                                "JAMMER ENGAGED", font="bubble"
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
                                print("NODE INFORMATION JAMMED.")
                        else:
                            time.sleep(1.5)  # let other threads finish
                            sfx.appear_blip()
                            print("JAMMER NOT ACTIVE ON THIS NODE")
                    if P1.node_failed_state == True:
                        """if the node if failed"""
                        P1.chances -= 1
                        time.sleep(1.5)  # let the other thread finish first
                        sfx.gentle_ui()
                        sfx.voice_node_fail()  # reassure player
                        """punishment for landing in defense range"""
                        print("JAMMED: NO NODE INFORMATION POSSIBLE")
                        print("REDUCING GUESSES OF THE NODE TYPE YOU HAVE MORE OF")
                        time.sleep(3)
                        if P1.high_keys < P1.low_keys:
                            P1.low_keys -= 1
                            print("HIGH NODE GUESSES REDUCED BY 1")
                            if P1.low_keys == 1:
                                sfx.appear_blip()
                                sfx.gentle_ui()
                                time.sleep(1)
                                sfx.voice_warning_high_entries()
                                print(
                                    "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                                )
                        elif P1.high_keys > P1.low_keys:
                            P1.high_keys -= 1
                            print("LOW NODE GUESSES REDUCED BY 1")
                            if P1.high_keys == 1:
                                sfx.appear_blip()
                                sfx.gentle_ui()
                                time.sleep(1)
                                sfx.voice_warning_low_entries()
                                print(
                                    "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                                )
                        elif P1.high_keys == P1.low_keys:
                            print("HIGH AND LOW NODES ARE EQUAL. DECIDING RANDOMLY...")
                            time.sleep(1)
                            coin_flip = random.randint(1, 2)
                            if coin_flip == 1:
                                P1.high_keys -= 1
                                print("LOW NODE GUESSES REDUCED BY 1")
                                if P1.high_keys == 1:
                                    sfx.appear_blip()
                                    sfx.gentle_ui()
                                    time.sleep(1)
                                    sfx.voice_warning_low_entries()
                                    print(
                                        "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                                    )
                            if coin_flip == 2:
                                P1.low_keys -= 1
                                print("HIGH NODE GUESSES REDUCED BY 1")
                                if P1.low_keys == 1:
                                    sfx.appear_blip()
                                    sfx.gentle_ui()
                                    time.sleep(1)
                                    sfx.voice_warning_high_entries()
                                    print(
                                        "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                                    )
                        P1.guess_list.append("(JAMMED)")
                        # P1.tripwire = False   # disabled so you can assess the guess
                        print("LOW ENTRIES REMAINING: " + str(P1.high_keys))
                        print("HIGH ENTRIES REMAINING: " + str(P1.low_keys))

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
            if P1.tripwire == True or P1.node_failed_state == True:
                sfx.fail_corrupt()  # failed one of the two states
                print(
                    "However, since you triggered the JAMMER, there is no way to get into the node."
                )
                time.sleep(1)
                sfx.burst_sound()
                print(
                    "The FIREWALL is locking us out. Next time, make sure to avoid triggering the JAMMER on the NEXUS NODE."
                )
                print(
                    "\n\n Denying Nexus entry due to JAMMER TRIGGER.\n\nRELEASING KEY CODE: ",
                    P1.entry_key,
                )
                time.sleep(6)
                sfx.fail_corrupt()
                ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                print(ascii_locked)
                print("THANK YOU FOR VISITING.")
                time.sleep(8)
                return False
            sfx.gentle_ui()
            sfx.hack_node()
            print("EXTRACTING DATA\n")
            with alive_bar(
                total=100,
                length=75,
                bar="smooth",
            ) as bar:  # default setting
                for i in range(100):
                    time.sleep(0.03)
                    bar()  # call after consuming one item
            print("\n")
            time.sleep(1)
            sfx.gentle_ui()
            ascii_win = pyfiglet.figlet_format("KEY ACQUIRED")
            print(ascii_win)
            sfx.voice_nexus_found()  # voice line found key!
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
                time.sleep(1)
                print(
                    "\n\nThe system is falling apart... but it seems like you're so close to the NEXUS KEY that the system is hesitating to kick you out--\nIt must not want to delete the NEXUS KEY's node by accident.\nIt looks like we have time for one more chance!"
                )
                print("\n\nSYSTEM LOCK DELAYED. RECALIBRATING...")
                sfx.alarm_loop(4)
                time.sleep(1)
                print(P1.ascii_sonar_status)
                print("EXTRA SONAR READING:")
                print("NEXUS KEY WITHIN 2 NODES")
                P1.sonar_list.append("KEY WITHIN 2 NODES OF " + str(P1.guess))
                time.sleep(1)
                if (P1.high_keys == 0 and P1.low_keys == 1) or (
                    P1.high_keys == 1 and P1.low_keys == 0
                ):
                    print(
                        "Since you had only ONE remaining high and low entry before this,\nwe have NO WAY of inferring which direction the NEXUS KEY is from here..."
                    )
                    P1.guess_list.append("UNKNOWN")
                if P1.high_keys == 0 and P1.low_keys > 1:
                    print(
                        "Since you ran out of LOW ENTRIES and had multiple high entries remaining,\nwe can infer the NEXUS KEY is HIGHER THAN "
                        + str(P1.guess)
                        + "."
                    )
                    P1.guess_list.append("LOW")
                if P1.high_keys > 1 and P1.low_keys == 0:
                    print(
                        "Since you ran out of HIGH ENTRIES and had multiple low entries remaining,\nwe can infer the NEXUS KEY is LOWER THAN "
                        + str(P1.guess)
                        + "."
                    )
                    P1.guess_list.append("HIGH")
                P1.make_guess()
                P1.extra_chance = False
                pygame.mixer.stop()

        if P1.guess == P1.entry_key:
            sfx.appear_blip()
            print("NEXUS KEY LOCATED.")
            if (
                P1.tripwire == True or P1.node_failed_state == True
            ):  # if failed, prevent access
                sfx.fail_corrupt()  # failed one of the two states
                print(
                    "However, since you triggered the JAMMER, there is no way to get into the node."
                )
                time.sleep(1)
                sfx.burst_sound()
                print(
                    "The FIREWALL is locking us out. Next time, make sure to avoid triggering the JAMMER on the NEXUS NODE."
                )
                print(
                    "\n\n Denying Nexus entry due to JAMMER TRIGGER.\n\nRELEASING KEY CODE: ",
                    P1.entry_key,
                )
                time.sleep(6)
                sfx.fail_corrupt()
                ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                print(ascii_locked)
                print("THANK YOU FOR VISITING.")
                time.sleep(8)
                return False
            time.sleep(2)
            with alive_bar(
                total=100,
                length=75,
                bar="smooth",
            ) as bar:  # default setting
                for i in range(100):
                    time.sleep(0.03)
                    bar()  # call after consuming one item
            print("\n")
            time.sleep(1)
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
            time.sleep(1)
            sfx.fail_corrupt()
            ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
            print(ascii_locked)
            print(
                "\n\n Denying Nexus entry.\n\nRELEASING KEY CODE: ",
                P1.entry_key,
            )
            time.sleep(6)
            sfx.fail_corrupt()
            print("THANK YOU FOR VISITING.")
            time.sleep(8)
            return False
            # go back to title screen
