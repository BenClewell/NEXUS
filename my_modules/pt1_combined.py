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
import threading  # for the timer
from my_modules import sfx
import json  # read score information

# not yet ## from my_modules import help_guide


class P1:
    jammer_no_wrong = True
    distance_bonus = 0 # how far from jammer were you?
    score_file = open("scores.json", "r")
    scores = json.load(score_file)
    for key in scores["data_scores"]:  # for reagent in reagent list
        for i in key:
            key[i] = int(key[i])
            key[i] = 2000
    with open("scores.json", "w") as f:
        json.dump(scores, f, indent=2)
    is_even_reveal = False
    #
    my_timer = 30  # timer for part 2
    start_timer = False
    current_stage_timer = False  # in stage 2, where timer applies
    out_of_time = False
    #
    data_score = 2000  # STARTING DATA SCORE
    given_digits = 4
    # allowed_list = []  # playtest
    allowed_list = sample("0123456789", given_digits)
    #
    node_vulnerable = False  # prevent hacking outside of the specified range
    node_progress_rank = 1
    node_failed_state = False  # has the user failed the last node hack?
    node_progress_speed = 0.1  # become faster each hack
    insertion_finished = False
    entered_node = 0 # track what player has entered
    # hacking minigame
    hack_success = True
    hack_chances = 3
    with open("scores.json") as f:
        fw_speed = json.load(f)
        params = fw_speed["parameters"]
        sp_assign = params[0]['enemy_speed']
    fw_difficulty = int(sp_assign) # set firewall speed to parameter
    # how fast the 'enemy' firewall moves comparative to you, lower is faster
    # PLAYTEST print(fw_difficulty)
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
    barter_complete = False  # have you been offered even/odd information
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
            insert_middle = start_insert+6
            if key == keyboard.Key.enter and P1.node_vulnerable == True:
                sfx.burst_sound()
                P1.node_failed_state = False  # user hacked node successfully
                P1.insertion_finished = True
                time.sleep(1)
                if P1.entered_node == insert_middle:
                    print("[PERFECT INSERTION (+500 DATA)]")
                    P1.data_score += 500
                elif ((insert_middle + 1) == P1.entered_node) or ((insert_middle - 1) == P1.entered_node):
                    print("[PRECISE INSERTION (+250 DATA)]")
                    P1.data_score += 250
                elif ((insert_middle + 2) == P1.entered_node) or ((insert_middle - 2) == P1.entered_node):
                    print("[GOOD INSERTION (+150 DATA)]")
                    P1.data_score += 150
                else:
                    print("[VALID INSERTION (+100 DATA)]")
                    P1.data_score+=100
            if key == keyboard.Key.enter and P1.node_vulnerable == False:
                sfx.burst_sound()
                P1.node_failed_state = True
                P1.insertion_finished = True
                time.sleep(1)
                print("[INVALID TEST RESPONSE (-100 DATA)]")
                P1.data_score -= 100

        """user enters a node guess to find the key
        rejected if entry is too long, or not valid"""
        time.sleep(1)
        sfx.gentle_ui()
        print("\n\n---------------------------------------------------\n")
        if P1.allowed_list != []:
            print("<<ANTIVIRUS ACTIVE>>\nINSERTION POOL: {}".format(P1.allowed_list))
        if len(P1.allowed_list) == 1:
            print(
                "<<ANTIVIRUS SHUTTING DOWN>> ::: FINAL INTEGER FROM INSERTION POOL MAY BE PAIRED WITH ANY OTHER INTEGER"
            )
        if (
            P1.sonar == True
            and P1.special_sonar == True
            and P1.special_sonar_limit == 0
        ):
            print("[SPECIAL SONAR: EQUIPPED]\n\n")

        elif (
            P1.sonar == True
            and P1.special_sonar == False
            and P1.special_sonar_limit == 0
        ):
            print("[SPECIAL SONAR: INACTIVE]\n\n")
        else:
            print("\n\n")
        print("SYS:// ENTER NODE\n---------------------------------------------------")
        try:
            P1.guess_string = str(input("INPUT:  "))
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
                        increment_nonrepeat = (
                                0  # prevent repeat messages, see increment
                            )
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
                                sfx.antivirus_block()

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
                                if increment_nonrepeat == 0:
                                    sfx.antivirus_block()

                            else:
                                duplicates[char] = 1
                                #
                                #
                
                            if (
                                char not in P1.allowed_list
                                and dupes_caught == False
                                and len(P1.allowed_list) != 1
                            ):
                                valid = False
                                charpass = False
                                if increment_nonrepeat == 0:
                                    sfx.fail_corrupt()
                                if increment_nonrepeat == 0:
                                    print("[ANTIVIRUS]: FORBIDDEN ENTRY")
                                    print(
                                        "ERROR: You do not have PERMISSION to access those NODE INTEGERS."
                                        "\nPlease disable ANTIVIRUS to permit nodes outside of the INTEGER POOL."
                                    )
                                    sfx.antivirus_block()
                                    increment_nonrepeat += (
                                    1  # prevent message from repeating two times
                                )
                                else:
                                    pass
                
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
                                    if increment_nonrepeat == 0:
                                        sfx.antivirus_block()
                                    increment_nonrepeat += (
                                    1  # prevent message from repeating two times
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
                        

                            if P1.allowed_list == []:
                                sfx.antivirus_disabled()
                                time.sleep(0.5)
                                sfx.gentle_lofi('Quiet')
                                print("/ INTEGER POOL SATISFIED \\")
                                time.sleep(0.5)
                                print("[**[ANTIVIRUS DISABLED]**]")
                                time.sleep(2)
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
            if P1.allowed_list != []:
                time.sleep(.5)
                sfx.antivirus_pass()
                print(
                    random.choice(
                        (
                            "[ANTIVIRUS APPROVAL] : Valid Input! :)",
                            "[ANTIVIRUS APPROVAL] : Thank you for your compliance! :)",
                            "[ANTIVIRUS APPROVAL] : I knew I could trust you! :)",
                            "[ANTIVIRUS APPROVAL] : You're the best! :)",     
                            "[ANTIVIRUS APPROVAL] : You make my job worth doing! :)",
                            "[ANTIVIRUS APPROVAL] : This entry looks perfect! :)",
                            "[ANTIVIRUS APPROVAL] : I know you're one of the good ones! :)",
                            "[ANTIVIRUS APPROVAL] : Thanks for playing by the rules! :)",        
                            "[ANTIVIRUS APPROVAL] : Your entry looks great! :)",
                            "[ANTIVIRUS APPROVAL] : Beautiful entry! :)",
                            "[ANTIVIRUS APPROVAL] : Absolutely approved! :)",
                            "[ANTIVIRUS APPROVAL] : You're my best friend! :)",         
                        )
                    )
                )
                time.sleep(2)
                print("PERMISSION GRANTED. REMOVING ENTERED NODE FROM INSERTION POOL...\n")
                time.sleep(1)

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
            print('|| DATA LOCUS: {} ||'.format(end_insert-5))
            print(
                "\nPress ENTER between {} and {} to enter node.".format(
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
                        P1.entered_node = i+1 # know what node the player entered
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
                "ERROR: YOUR SPECIAL SONAR HAS BEEN DISABLED DUE TO OVEREXTENDED RANGE.\n"
                "YOU MAY RESTORE IT FOR 1500 DATA"
            )
            restore_ss = input(
                "\nREBOOT FUNCTIONALITY FOR 1500 DATA? (y/n)\n\nRESPONSE: "
            )
            while "y" not in restore_ss.lower() and "n" not in restore_ss.lower():
                sfx.gentle_lofi()
                restore_ss = input(
                    "\n\nREBOOT FUNCTIONALITY FOR 1500 DATA? (y/n)\n\nRESPONSE: "
                )
            if "y" in restore_ss.lower():
                P1.data_score -= 1500
                sfx.success()
                P1.special_sonar_limit -= 1
                print("SPECIAL SONAR ABILITY REBOOTED. (1500 DATA LOST)")
                P1.special_sonar = True
                print("(It has been automatically REACTIVATED. Press '101' to DISABLE.)")
            if "n" in restore_ss.lower():
                sfx.gentle_lofi()
                print("UNDERSTOOD. SPECIAL SONAR WILL REMAIN OFFLINE. (NO DATA LOST)")
            time.sleep(1)

    #
    #
    def hacker_history():
        """provide history of choices"""
        status_splash = True
        while status_splash == True:
            # playtest
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
            print("DATA ACQUIRED: {}".format(P1.data_score))
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
                    + str(P1.barrier_high -1 ) # reduce the high end of the jammer to inclusive 
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
                        "SPECIAL SONAR HAS BEEN DISABLED  (OVEREXTENDED RANGE)"
                        "\nIT MAY BE REBOOTED FOR 1500 DATA (ENTER 101 TO REBOOT)"
                    )
            if P1.sonar_list == []:
                print("NO SONAR HISTORY")
            if P1.sonar_list != []:
                print("SONAR HISTORY: " + str(P1.sonar_list))
            if P1.is_even_reveal == True:
                if P1.entry_key % 2 == 0:
                    print("\nTHE NEXUS KEY IS AN EVEN NUMBER")
                else:
                    print("\nTHE NEXUS KEY IS AN ODD NUMBER")

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
            P1.jammer_no_wrong = True # no answers wrong
            stdscr.clear()
            sfx.alarm_loop(6)
            sfx.villian_jammer_active()
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
                                P1.jammer_no_wrong = False
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
                title = "JAMMER ENTRY GAINED."
                subtitle = (
                    "[System] Security has been HEIGHTENED. Press ENTER to proceed."
                )
                pygame.mixer.stop()
                sfx.success()
                sfx.burst_sound()
                P1.hack_success = True
                if P1.fw_difficulty > 500:
                    P1.fw_difficulty -= 500  # can't go to zero
                # make the enemy move faster
                # increase the 'level difficulty' by one
                P1.distance_bonus = (x_finish-enemy_x)
                curses.endwin()

            else:
                sfx.fail_corrupt()
                title = "JAMMER ENTRY DENIED. 200 DATA LOST."
                subtitle = "[System] Security has been LOWERED. Press ENTER to proceed."
                # nexus_main.num_denials -=1
                pygame.mixer.stop()
                sfx.burst_sound()
                sfx.fail_corrupt()
                P1.hack_success = False
                P1.fw_difficulty += 1000
                # make the enemy move slower
                P1.fw_level -= 2
                P1.data_score -= 200
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
                print("NODE INFORMATION JAMMED\n*******************\n")
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
                print("\n************************\n")
            # Increase the value of chance by 1
        if P1.chances == 3:  # MOVED THIS BACK TO REVEAL NO MATTER WHAT
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
                + str(P1.barrier_high -1 )
                + ".\nThere is a 50% chance that the NEXUS KEY has appeared within this range."
            )

    def sonar_alerts():
        """provide sonar, and end game if too many low or high chances"""
        if P1.special_sonar == True and (P1.guess != P1.entry_key):
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
                print(
                    "SPECIAL SONAR OUT OF RANGE, AND IS NOW DISABLED. PRESS '101' TO TROUBLESHOOT."
                )
                sfx.fail_corrupt()

                P1.special_sonar_limit += 1  # make it impossible to resummon

        if P1.special_sonar == False:
            if P1.chances == 4:
                P1.sonar = True
                # enable special sonar
                time.sleep(2)
                sfx.enable_firewall.play()
                print("\n\n")
                ascii_special_unlocked = pyfiglet.figlet_format(
                    "SPECIAL SONAR ONLINE", font="digital"
                )
                print(ascii_special_unlocked)
                print(
                    "\nSPECIAL SONAR unlocked. (Type '101' to toggle ON/OFF)\nOut-of-range use will DISABLE Special Sonar."
                )
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
                    "\n[ANTIVIRUS] EXTRA INTEGER ADDED TO INSERTION POOL: {}".format(
                        added_number
                    )
                )
                P1.allowed_list.append(added_number)
            if P1.chances == 3 and P1.guess != P1.entry_key:
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
        if P1.chances == 1:
            if P1.low_keys != 0 and P1.high_keys != 0:
                print(
                    "\nFINAL NODE ENTRY REACHED. LOCKING SYSTEM UPON NEXT FAILURE TO LOCATE NEXUS KEY.\n"
                )

            if P1.barter_complete == False:
                barter_even_odd = input(
                    "[SYSTEM NEGOTIATION]:\nLOSE 500 DATA TO LEARN IF NEXUS NODE IS EVEN OR ODD? (y/n)\n\n RESPONSE: "
                )
                while (
                    "n" not in barter_even_odd.lower()
                    and "y" not in barter_even_odd.lower()
                ):
                    print("YOU MUST REPLY TO THE OFFER.")
                    sfx.fail_corrupt()
                    barter_even_odd = input(
                        "LOSE 500 DATA TO LEARN IF NEXUS NODE IS EVEN OR ODD? (y/n)\n\nRESPONSE: "
                    )
                if "y" in barter_even_odd:
                    P1.is_even_reveal = True
                    time.sleep(1)
                    sfx.affirm_sound.play()
                    P1.data_score -= 500
                    sfx.affirm_sound.play()
                    if P1.entry_key % 2 == 0:
                        print("THE NEXUS KEY IS EVEN (500 DATA LOST)")
                    else:
                        print("THE NEXUS KEY IS ODD.")
                    time.sleep(2)
                if "n" in barter_even_odd:
                    time.sleep(1)
                    sfx.affirm_sound.play()
                    print("OFFER RESCINDED. (DATA RETAINED)")
                    time.sleep(2)
                P1.barter_complete = True
        if P1.chances == 2:
            if P1.low_keys != 0 and P1.high_keys != 0 and P1.guess!=P1.entry_key:
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
        #print(P1.entry_key)  # for playtesting
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

        time.sleep(1.5)
        sfx.gentle_lofi()
        print(
            "For now, the ANTIVIRUS will prevent us from going outside of the INTEGER POOL."
        )
        print(
            "Construct your NODE ENTRIES using these available integers. The ANTIVIRUS will be weakened as you construct VALID NODES.\n\n"
        )
        time.sleep(1.5)
        print("------------------------------------------------------------------")
        time.sleep(1.5)
        sfx.gentle_lofi('Quiet')
        print("------------------------------------------------------------------")
        time.sleep(1.5)
        sfx.gentle_lofi('Quiet')
        print("------------------------------------------------------------------\n")
        sfx.antivirus_activated()
        print(
            random.choice(
                (
                    "[ANTIVIRUS ONLINE] : I look forward to defending the NEXUS! :)",
                    "[ANTIVIRUS ONLINE] : I'm so glad I can trust you! :)",
                    "[ANTIVIRUS ONLINE] : I hope you consider us friends! :)",
                    "[ANTIVIRUS ONLINE] : I will perform my job well! :)",
                    "[ANTIVIRUS ONLINE] : I will protect our systems! :)",     
                    "[ANTIVIRUS ONLINE] : I promise to keep us safe! :)",
                    "[ANTIVIRUS ONLINE] : I will always protect you! :)",
                    "[ANTIVIRUS ONLINE] : Always doing my best to keep us secure! :)",
                    "[ANTIVIRUS ONLINE] : I love doing my part! :)",        
                    "[ANTIVIRUS ONLINE] : A safe system is a happy system! :)",
                    "[ANTIVIRUS ONLINE] : I love keeping our NEXUS in good hands! :)",
                    "[ANTIVIRUS ONLINE] : Hello there! I will keep you safe. :)",
                    "[ANTIVIRUS ONLINE] : Greetings! I hope you are well! :)",         
                )
            )
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
                            sfx.villian_jammerland()
                            sfx.appear_blip()
                            print(
                                "\n\nENTRY DETECTED IN JAMMER RANGE. ENGAGING COUNTERMEASURES\n\n"
                            )
                            sfx.hack_node()
                            time.sleep(3)
                            P1.node_hacking_minigame()
                            if P1.hack_success == False:
                                # reduce hack chances by one.
                                pass
                            else:
                                time.sleep(1)
                                sfx.gentle_ui()
                                print("\n")
                                print('JAMMER EVADED!')
                                if P1.fw_level == 0:
                                    print('INTERMEDIATE SECURITY DEFEATED: +150 DATA')
                                    P1.data_score+=150
                                elif P1.fw_level == 1:
                                    print('HIGH SECURITY DEFEATED: +200 DATA')
                                    P1.data_score+=200
                                elif P1.fw_level == 2:
                                    print('VERY HIGH SECURITY DEFEATED: +250 DATA')
                                    P1.data_score+=250
                                elif P1.fw_level > 2:
                                    print('INCREDIBLY HIGH SECURITY DEFEATED: +250 DATA')
                                    P1.data_score+=300
                                elif P1.fw_level <0:
                                    print('LOWER LEVEL SECURITY DEFEATED: +100 DATA')
                                    P1.data_score+=100
                                time.sleep(1)
                                sfx.gentle_lofi()
                                if P1.jammer_no_wrong ==True:
                                    print('ALL ANSWERS CORRECT: +50 DATA')
                                    P1.data_score+=50
                                print('DOMINANCE BONUS: +{} DATA\n'.format(P1.distance_bonus*2))
                                P1.data_score+=(P1.distance_bonus*2)
                                P1.fw_level += 1
                        else:
                            time.sleep(1.5)  # let other threads finish
                            sfx.appear_blip()
                            print("JAMMER NOT ACTIVE ON THIS NODE (+100 DATA)")
                            P1.data_score +=100
                    if P1.node_failed_state == True:
                        """if the node if failed"""
                        P1.chances -= 1
                        time.sleep(1.5)  # let the other thread finish first
                        sfx.gentle_ui()
                        sfx.voice_node_fail()  # reassure player
                        """punishment for landing in defense range"""
                        print("NODE INFORMATION JAMMED\n*******************\n")
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
                        print("\n***********************\n")
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
                sfx.villian_system_lock()
                print("THANK YOU FOR VISITING.")
                time.sleep(8)
                return False
            sfx.gentle_ui()
            print("\n")
            time.sleep(1)
            sfx.gentle_ui()
            ascii_win = pyfiglet.figlet_format("KEY ACQUIRED")
            print(ascii_win)
            sfx.voice_nexus_found()  # voice line found key!
            time.sleep(5)
            print("Excellent job.")
            time.sleep(1)
            sfx.voice_found_data()
            print(
                "Before we move forward, target systems are COMPROMISED. We have THIRTY SECONDS to harvest DATA."
            )
            time.sleep(3)
            sfx.gentle_ui()
            sfx.gentle_ui()
            ascii_breach = pyfiglet.figlet_format("DATA BREACH")
            print(ascii_breach)
            print(
                "Data is transmitted globally USING CARDINAL DIRECTIONS: North, East, South, and West."
                "\nI will provide a LEDGER of where a data packet has moved.\nYou must respond with N, E, S, or W to triangulate each data packet.\n\n"
                "RIGHT TURNS move CLOCKWISE around the compass.\nLEFT TURNS move COUNTERCLOCKWISE.\nFinally, REVERSE MOVEMENTS move you OPPOSITE on the compass.\n\n"
                "LOST DATA will SUBTRACT the total value of the FAILED TARGET. So be careful."
            )
            ready_to_start = input("\nPress ENTER when ready to begin DATA HARVESTING.")
            sfx.gentle_lofi()

            def countdown():
                P1.my_timer = 30
                for i in range(30):
                    if (
                        P1.current_stage_timer == True
                    ):  # only punish if in the right part
                        P1.my_timer = P1.my_timer - 1
                        time.sleep(1)
                if P1.current_stage_timer == True:  # only punish if in the right part
                    P1.out_of_time = True
                    sfx.enable_firewall.play()
                    sfx.villian_timer_end()
                    print(
                        "PATCH COMPLETE:// SECURING INTERNATIONAL DATA. NO FURTHER ENTRIES WILL BE VALID.\n\nPress ENTER TWICE to CONTINUE."
                    )
                else:
                    pass

            if P1.start_timer == False:
                sfx.enable_firewall.play()
                print(
                    "SYS:// PATCHING VULNERABILITY. TERMINATING INTRUSION IN 30 SECONDS."
                )
                sfx.data_loop()
                sfx.villian_timer_start()
                time.sleep(2)
                P1.current_stage_timer = True  # allow the timer to be mischievous
                countdown_thread = threading.Thread(target=countdown)
                countdown_thread.start()
                P1.start_timer = True
            number_turns = 3
            while P1.out_of_time == False:
                chosen_direction = randint(1, 4)
                if chosen_direction == 1:
                    direction = "NORTH"
                elif chosen_direction == 2:
                    direction = "EAST"
                elif chosen_direction == 3:
                    direction = "SOUTH"
                elif chosen_direction == 4:
                    direction = "WEST"
                else:
                    pass
                sfx.burst_sound()
                random_variance = number_turns + randint(-2, 2)
                print("\nDATA PACKET ({}00)\n".format(random_variance))
                print("--ORIENTED {}--".format(direction))
                deplete = random_variance  # lower number as we go
                turn_list = []
                while deplete > 0:
                    if number_turns < 4:
                        turn = randint(0, 1)
                    if number_turns > 3:
                        turn = randint(0, 2)
                    if turn == 0:
                        turn_list.append("LEFT")
                        chosen_direction -= 1
                        if chosen_direction == 0:
                            chosen_direction = 4  # reset to west

                    elif turn == 1:
                        turn_list.append("RIGHT")
                        chosen_direction += 1
                        if chosen_direction == 5:
                            chosen_direction = 1  # reset to north
                    else:
                        turn_list.append("REVERSED")
                        chosen_direction += 2
                        if chosen_direction == 5:
                            chosen_direction = 1
                        if chosen_direction == 6:
                            chosen_direction = 2

                    deplete -= 1
                if chosen_direction == 1:
                    direction = "NORTH"
                elif chosen_direction == 2:
                    direction = "EAST"
                elif chosen_direction == 3:
                    direction = "SOUTH"
                elif chosen_direction == 4:
                    direction = "WEST"
                else:
                    pass
                print("LOG: {}".format(turn_list))
                where_am_i = input("PACKET TRAJECTORY: ")
                #
                acceptable_trajectory = False
                while (
                    acceptable_trajectory == False
                ):  # keep in loop until valid response
                    if where_am_i == "":  # catch blank entries
                        acceptable_trajectory = False
                        sfx.fail_corrupt()  # bad sound
                        if P1.out_of_time == False:
                            print("INVALID RESPONSE. PLEASE ENTER AGAIN.")
                            where_am_i = input("PACKET TRAJECTORY: ")
                        if P1.out_of_time == True:
                            where_am_i = input("")
                            where_am_i = "e"

                    if where_am_i != "":
                        if (
                            where_am_i[0].lower() != "n"
                            and where_am_i[0].lower() != "e"
                            and where_am_i[0].lower() != "s"
                            and where_am_i[0].lower() != "w"
                        ):
                            print(where_am_i[0])
                            acceptable_trajectory = False
                            sfx.fail_corrupt()  # bad sound
                            print("INVALID RESPONSE. PLEASE ENTER AGAIN.")
                            where_am_i = input("PACKET TRAJECTORY: ")
                        else:
                            acceptable_trajectory = True
                bonus_to_data = random_variance * 100
                if (
                    where_am_i[0].lower() == direction[0].lower()
                    and P1.out_of_time == False
                ):
                    sfx.affirm_sound.play()
                    print("CONFIRMED: COLLECTING {}00 DATA".format(random_variance))
                    P1.data_score += bonus_to_data
                else:
                    if P1.out_of_time == False:
                        sfx.fail_corrupt()
                        print(
                            "ERROR: TRAJECTORY IS {}; {} DATA LOST".format(
                                direction, bonus_to_data
                            )
                        )
                        P1.data_score -= bonus_to_data
                    else:
                        sfx.success()
                        print("DATA HAS BEEN LOCKED AND CANNOT BE COLLECTED FURTHER.")
                number_turns += 1
                time.sleep(1)
            time.sleep(1)
            pygame.mixer.stop()
            time.sleep(1)
            ascii_breachpatch = pyfiglet.figlet_format("BREACH CONTAINED")
            print(ascii_breachpatch)
            sfx.voice_done_data()
            print("DATA BREACH HAS BEEN HALTED. COMITTING DATA...")
            time.sleep(2)
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
            efficiency_bonus = P1.chances * 500
            P1.data_score += efficiency_bonus
            print("LOCATIONAL EFFICIENCY BONUS: {}".format(efficiency_bonus))
            sfx.success()
            sfx.gentle_lofi()
            print("CURRENT DATA:{}".format(P1.data_score))
            score_file = open("scores.json", "r")
            scores = json.load(score_file)
            for key in scores["data_scores"]:  # for reagent in reagent list
                for i in key:
                    key[i] = int(key[i])
                    key[i] = P1.data_score
            with open("scores.json", "w") as f:
                json.dump(scores, f, indent=2)
            time.sleep(1)
            print("ENTERING THE NEXUS NODE IN TEN SECONDS...")
            time.sleep(10)

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
                sfx.villian_system_lock()
                print("THANK YOU FOR VISITING.")
                time.sleep(8)
                return False
            time.sleep(1)
            sfx.voice_found_data()
            print(
                "Before we move forward, target systems are COMPROMISED. We have THIRTY SECONDS to harvest DATA."
            )
            time.sleep(3)
            sfx.gentle_ui()
            ascii_breach = pyfiglet.figlet_format("DATA BREACH")
            print(ascii_breach)
            print(
                "Data is transmitted globally USING CARDINAL DIRECTIONS: North, East, South, and West."
                "\nI will provide a LEDGER of where a data packet has moved.\nYou must respond with N, E, S, or W to triangulate each data packet.\n\n"
                "RIGHT TURNS move CLOCKWISE around the compass.\nLEFT TURNS move COUNTERCLOCKWISE.\nFinally, REVERSE MOVEMENTS move you OPPOSITE on the compass.\n\n"
                "LOST DATA will SUBTRACT the total value of the FAILED TARGET. So be careful."
            )
            ready_to_start = input("\nPress ENTER when ready to begin DATA HARVESTING.")
            sfx.gentle_lofi()

            def countdown():
                P1.my_timer = 30
                for i in range(30):
                    if (
                        P1.current_stage_timer == True
                    ):  # only punish if in the right part
                        P1.my_timer = P1.my_timer - 1
                        time.sleep(1)
                if P1.current_stage_timer == True:  # only punish if in the right part
                    P1.out_of_time = True
                    sfx.enable_firewall.play()
                    sfx.villian_timer_end()
                    print(
                        "PATCH COMPLETE:// SECURING INTERNATIONAL DATA. NO FURTHER ENTRIES WILL BE VALID.\n\nPress ENTER TWICE to CONTINUE."
                    )
                else:
                    pass

            if P1.start_timer == False:
                sfx.enable_firewall.play()
                print(
                    "SYS:// PATCHING VULNERABILITY. TERMINATING INTRUSION IN 30 SECONDS."
                )
                sfx.data_loop()
                sfx.villian_timer_start()
                time.sleep(2)
                P1.current_stage_timer = True  # allow the timer to be mischievous
                countdown_thread = threading.Thread(target=countdown)
                countdown_thread.start()
                P1.start_timer = True
            number_turns = 3
            while P1.out_of_time == False:
                chosen_direction = randint(1, 4)
                if chosen_direction == 1:
                    direction = "NORTH"
                elif chosen_direction == 2:
                    direction = "EAST"
                elif chosen_direction == 3:
                    direction = "SOUTH"
                elif chosen_direction == 4:
                    direction = "WEST"
                else:
                    pass
                sfx.burst_sound()
                random_variance = number_turns + randint(-2, 2)
                print("\nDATA PACKET ({}00)\n".format(random_variance))
                print("--ORIENTED {}--".format(direction))
                deplete = random_variance  # lower number as we go
                turn_list = []
                while deplete > 0:
                    if number_turns < 4:
                        turn = randint(0, 1)
                    if number_turns > 3:
                        turn = randint(0, 2)
                    if turn == 0:
                        turn_list.append("LEFT")
                        chosen_direction -= 1
                        if chosen_direction == 0:
                            chosen_direction = 4  # reset to west

                    elif turn == 1:
                        turn_list.append("RIGHT")
                        chosen_direction += 1
                        if chosen_direction == 5:
                            chosen_direction = 1  # reset to north
                    else:
                        turn_list.append("REVERSED")
                        chosen_direction += 2
                        if chosen_direction == 5:
                            chosen_direction = 1
                        if chosen_direction == 6:
                            chosen_direction = 2

                    deplete -= 1
                if chosen_direction == 1:
                    direction = "NORTH"
                elif chosen_direction == 2:
                    direction = "EAST"
                elif chosen_direction == 3:
                    direction = "SOUTH"
                elif chosen_direction == 4:
                    direction = "WEST"
                else:
                    pass
                print("LOG: {}".format(turn_list))
                where_am_i = input("PACKET TRAJECTORY: ")
                #
                acceptable_trajectory = False
                while (
                    acceptable_trajectory == False
                ):  # keep in loop until valid response
                    if where_am_i == "":  # catch blank entries
                        acceptable_trajectory = False
                        sfx.fail_corrupt()  # bad sound
                        if P1.out_of_time == False:
                            print("INVALID RESPONSE. PLEASE ENTER AGAIN.")
                            where_am_i = input("PACKET TRAJECTORY: ")
                        if P1.out_of_time == True:
                            where_am_i = input("")
                            where_am_i = "e"
                    if where_am_i != "":
                        if (
                            where_am_i[0].lower() != "n"
                            and where_am_i[0].lower() != "e"
                            and where_am_i[0].lower() != "s"
                            and where_am_i[0].lower() != "w"
                        ):
                            print(where_am_i[0])
                            acceptable_trajectory = False
                            sfx.fail_corrupt()  # bad sound
                            print("INVALID RESPONSE. PLEASE ENTER AGAIN.")
                            where_am_i = input("PACKET TRAJECTORY: ")
                        else:
                            acceptable_trajectory = True
                bonus_to_data = random_variance * 100
                if (
                    where_am_i[0].lower() == direction[0].lower()
                    and P1.out_of_time == False
                ):
                    sfx.affirm_sound.play()
                    print("CONFIRMED: COLLECTING {}00 DATA".format(random_variance))
                    P1.data_score += bonus_to_data
                else:
                    if P1.out_of_time == False:
                        sfx.fail_corrupt()
                        print(
                            "ERROR: TRAJECTORY IS {}; {} DATA LOST".format(
                                direction, bonus_to_data
                            )
                        )
                        P1.data_score -= bonus_to_data
                    else:
                        sfx.success()
                        print("DATA HAS BEEN LOCKED AND CANNOT BE COLLECTED FURTHER.")
                number_turns += 1
                time.sleep(1)
            time.sleep(1)
            pygame.mixer.stop()
            time.sleep(1)
            ascii_breachpatch = pyfiglet.figlet_format("BREACH CONTAINED")
            print(ascii_breachpatch)
            sfx.voice_done_data()
            print("DATA BREACH HAS BEEN HALTED. COMITTING DATA...")
            time.sleep(2)
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
            efficiency_bonus = P1.chances * 100
            P1.data_score += efficiency_bonus
            print("LOCATIONAL EFFICIENCY BONUS: {}".format(efficiency_bonus))
            sfx.success()
            time.sleep(1)
            sfx.gentle_lofi()
            print("CURRENT DATA:{}".format(P1.data_score))
            score_file = open("scores.json", "r")
            scores = json.load(score_file)
            for key in scores["data_scores"]:  # for reagent in reagent list
                for i in key:
                    key[i] = int(key[i])
                    key[i] = P1.data_score
            with open("scores.json", "w") as f:
                json.dump(scores, f, indent=2)
            time.sleep(1)
            print("ENTERING THE NEXUS NODE IN TEN SECONDS...")
            time.sleep(10)
            return True

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
            sfx.villian_system_lock()
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
