import random
from random import sample, shuffle, choice
from random import randint

import pyfiglet
import pyfiglet.fonts
import pygame
from pygame import mixer

from alive_progress import alive_bar  # cool loading animations

import time

from my_modules import title_screen
from my_modules import sfx

import keyboard
import threading
import win32api
import pynput
from pynput import keyboard
from importlib import reload
import json

# allow the nexus timer to decrypt in the background


class P2:
    """house all methods and unify all global variables"""
    antivirus_disable_counter = 0 # antivirus message is only one
    data_my_timer = 60  # timer for part 2
    data_start_timer = False
    data_current_stage_timer = False  # in stage 2, where timer applies
    data_out_of_time = False
    # first, load the player's data score
    data_score = 0
    score_file = open("scores.json", "r")
    scores = json.load(score_file)
    for key in scores["data_scores"]:  # assign current player score in json to variable
        for i in key:
            key[i] = int(key[i])
            data_score = key[i]
    #
    my_timer = 300  # timer for part 2
    current_stage_timer = False  # in stage 2, where timer applies
    out_of_time = False
    correct_key = False
    #
    guess_list = []  # user can track all entries
    preemptive_press = False  # start of p2, monitor enter presses (multithread)
    first_allowed_range = False  # start p2, are you in the allowed keypress range?
    initial_not_fail = False
    #
    #
    too_many_presses = False  # endgame, monitor enter presses (multithread)
    allowed_range = False  # multithread, are you in the allowed keypress range?
    # DISABLED time_is_up  = False #endgame, monitor timer (multithread)
    final_roundcount = 1
    rounds_done = False
    too_slow = False  # endgame, monitor speed
    #
    node_progress_speed = 0.1  # become faster each hack
    node_progress_rank = 1
    node_vulnerable = False
    bad_insertion = False  # the user has gotten each nexus insertion right
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
            print("DATA ACQUIRED: {}".format(P2.data_score))
            print(
                "SYS TRACE IN PROGRESS:// MINUTES BEFORE LOCKDOWN: "
                + str(round((P2.my_timer / 60), 2))
            )
            print("\nEntry Information:")
            if P2.guess_list == []:
                print("NO ENTRIES COMMITTED YET")
            if P2.guess_list != []:
                print("ENTRIES SO FAR: " + str(P2.guess_list))
            time.sleep(2)
            print("\nReturning to hacking interface...")
            time.sleep(1)
            status_splash = False

    def final_hack_success():
        def on_press(key):
            if key == keyboard.Key.enter and P2.allowed_range == True:
                print("[VALID TEST RESPONSE SUBMITTED]")
            if key == keyboard.Key.enter and P2.allowed_range == False:
                print("[INVALID TEST RESPONSE]")
                sfx.fail_corrupt()
                sfx.burst_sound()
                print(
                    "YOU HAVE MADE AN INVALID SUBMISSION FOR THE TEST. SHUTTING DOWN NEXUS..."
                )
                P2.too_many_presses = True
                sfx.fail_corrupt()
                sfx.burst_sound()
                print("FIREWALL DISABLING INFRASTRUCTURE...")
                return
        random_final_song = randint(1,2)
        sfx.play_mp3_once("/bgm/bgm_final_{}.mp3".format(random_final_song))
        sfx.burst_sound()
        ascii_no_touch = pyfiglet.figlet_format("DO NOT TOUCH\nTHE KEYBOARD")
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        print(
            "BE CAREFUL: Continuously monitoring keyboard for premature keypresses..."
        )

        print(ascii_no_touch)
        print("PREMATURE KEYPRESSES WILL LOCK NEXUS...")
        print("ONLY HIT 'ENTER' WHEN YOU ARE PROMPTED TO RESPOND.")
        time.sleep(5)
        #
        #

        def final_challenge():
            a = None
            if P2.too_many_presses == False:
                #
                #
                if P2.final_roundcount == 1:
                    print("\n\n")
                    sfx.first_jam.play()  # oh no! 33 percent blocked
                    sfx.loading_loop()
                    with alive_bar(
                        total=100, length=100, bar="smooth"
                    ) as bar:  # default setting
                        for i in range(100):
                            time.sleep(0.05)
                            bar()
                            if i > 20:
                                time.sleep(0.03)
                            if i == 33:
                                break
                    time.sleep(2)
                    pygame.mixer.stop()
                    sfx.fail_corrupt()
                    sfx.first_jam_check.play()  # gotta do the check!
                    time.sleep(4)
                    sfx.gentle_lofi()
                    print("\n\n")
                    ascii_prog = pyfiglet.figlet_format("DECRYPTION:\n33% COMPLETE")
                    sfx.gentle_ui()
                    print(ascii_prog)
                    sfx.antivirus_firewall()
                    print("FIREWALL CHECK ENGAGED: EASY (.5 SECOND RESPONSE)")
                    threshold = 0.5
                if P2.final_roundcount == 2:
                    print("\n\n")
                    sfx.second_jam_start.play()  # begin the journey to 66 percent
                    sfx.loading_loop()
                    with alive_bar(
                        total=100, length=100, bar="smooth"
                    ) as bar:  # default setting
                        for i in range(100):
                            time.sleep(0.05)
                            if i > 50:
                                time.sleep(0.03)
                            bar()
                            if i == 66:
                                break
                    time.sleep(2)
                    pygame.mixer.stop()
                    sfx.second_jam_blocked.play()  # angry! 66 percent!
                    sfx.fail_corrupt()
                    time.sleep(4)
                    sfx.gentle_lofi()
                    print("\n\n")
                    ascii_prog = pyfiglet.figlet_format("DECRYPTION:\n66% COMPLETE")
                    sfx.gentle_ui()
                    print(ascii_prog)
                    sfx.antivirus_firewall()
                    print("FIREWALL CHECK ENGAGED: MEDIUM (.4 SECOND RESPONSE)")
                    threshold = 0.4
                if P2.final_roundcount == 3:
                    print("\n\n")
                    sfx.third_jam_start.play()
                    sfx.loading_loop()
                    with alive_bar(
                        total=100, length=100, bar="smooth"
                    ) as bar:  # default setting
                        for i in range(100):
                            time.sleep(0.05)
                            if i > 70:
                                time.sleep(0.02)
                            if i > 90:
                                time.sleep(0.02)
                            bar()
                            if i == 98:
                                break
                    pygame.mixer.stop()
                    sfx.fail_corrupt()
                    time.sleep(1.5)
                    sfx.gentle_lofi()
                    sfx.fourth_jam_final.play()
                    print("\n\n")
                    ascii_prog = pyfiglet.figlet_format("DECRYPTION:\n99% COMPLETE")
                    time.sleep(3)
                    sfx.gentle_ui()
                    print(ascii_prog)
                    sfx.antivirus_firewall()
                    print("FIREWALL CHECK ENGAGED: HARD (.35 SECOND RESPONSE)")
                    threshold = 0.35
                sfx.sonar.play()
                time.sleep(1)
            if P2.too_many_presses == False:
                print("\n\nPREPARE TO RESPOND.")
                sfx.voice_fw_check()  # more fw checks
            time.sleep(0.5)
            if P2.too_many_presses == False:
                print("<<<TEST BEGINNING SOON>>>")
                time.sleep(random.randint(3, 6))
            if P2.too_many_presses == False:
                ascii_respond = pyfiglet.figlet_format("RESPOND")
                sfx.burst_sound()
                print(ascii_respond)
                tic = time.perf_counter()
                P2.allowed_range = True
                a = input()
                P2.allowed_range = False
                toc = time.perf_counter()
                sfx.gentle_ui()
                timeSpent = toc - tic
                if timeSpent > threshold:
                    print(
                        "RESPONSE TIME TOO SLOW. ("
                        + str(timeSpent)
                        + ") \nLOCKING SYSTEM."
                    )
                    P2.too_slow = True
                    #
                if timeSpent < threshold:
                    time.sleep(2)
                    print(
                        "RESPONSE TIME SATISFACTORY. ("
                        + str(timeSpent)
                        + ") \nCONTINUING..."
                    )
                    if timeSpent < 0.225:
                        print("PERFECT RESPONSE: +2000 DATA")
                        P2.data_score += 2000
                    elif timeSpent < 0.25:
                        print("PHENOMENAL RESPONSE: +1400 DATA")
                        P2.data_score += 1400
                    elif timeSpent < 0.3:
                        print("EXCEPTIONAL RESPONSE: +1000 DATA")
                        P2.data_score += 1000
                    elif timeSpent < 0.35:
                        print("GREAT RESPONSE: +600 DATA")
                        P2.data_score += 600
                    elif timeSpent < 0.4:
                        print("GOOD RESPONSE: +400 DATA")
                        P2.data_score += 400
                    elif timeSpent < 0.5:
                        print("ACCEPTABLE RESPONSE: +200 DATA")
                        P2.data_score += 200
                    else:
                        pass
                    P2.final_roundcount += (
                        1  # do another round, until five rounds have been played
                    )
                    if P2.final_roundcount > 3:
                        P2.rounds_done = True
                    else:
                        final_challenge()

        final_challenge()
        #
        listener.stop()

        if P2.too_slow == True:
            sfx.burst_sound()
            print("RESPONSE TOO SLOW.")
            time.sleep(1)
            pygame.mixer.music.fadeout(4)
            return False
        if P2.rounds_done == True:
            return True
        if P2.too_many_presses == True:
            pygame.mixer.music.fadeout(4)
            return False

    def decode_key():

        digits = 3
        attempts = 10
        sfx.gentle_ui()
        sfx.success()
        sfx.gotta_decrypt.play()  # introduction
        print("I can't believe it. We found the Nexus Key's node.")
        print(
            "Our work is almost done, but we still need to decrypt the key before the system finds out we're here."
        )

        print(
            "The Nexus Key is encrypted behind a ",
            digits,
            "- digit code. Each digit in this code is known as an ACCESS TOKEN.",
        )
        print("I'm going to help you find and align these access tokens...")
        print(
            "The system will return the following messages as we try cracking the encryption...\n"
        )
        time.sleep(2)
        sfx.gentle_lofi()
        print("When the system returns:        That means:\n")
        print(
            "MISALIGNED TOKEN                  An access token is correct, but positioned wrong."
        )
        print(
            "ALIGNED TOKEN                     An access token is correct and positioned right."
        )
        print(
            "NO ACCESS TOKENS                  None of the access tokens entered are in the key."
        )
        print("\nThere are no repeated ACCESS TOKENS in the key.")

        # Create a random number.

        letters = sample("0123456789", digits)

        if letters[0] == "0":
            letters.reverse()

        number = "".join(letters)
        #print(str(number))
        """for playtesting purposes"""
        time.sleep(2)
        sfx.gentle_lofi()
        print(
            "The system just established its encryption made up of three single-number ACCESS TOKENS.\n"
        )
        print(
            "We have",
            attempts,
            " attempts before the system finds us and all our work is for nothing...",
        )
        print(
            "\nRegarding any clues the system might give through its messages:\nthey don't reflect the order of the ACCESS TOKENS in the KEY.\nIt looks like the messages can apply to any position."
        )

        print(
            "If an ACCESS TOKEN is ALIGNED, you will have to perform increasingly high-security hacks for each aligned node."
        )
        print('Press "0" to view your hacking history at any time.\n\n')
        time.sleep(1)
        sfx.antivirus_activated()
        print("------------------------------------------------------------------------------\n")
        print(
            random.choice(
                (
                    "[ANTIVIRUS REACTIVATED] : It saddens me that you are not my friend! :(",
                    "[ANTIVIRUS REACTIVATED] : I wish you were on the side of security! :(",
                    "[ANTIVIRUS REACTIVATED] : All this time, I thought you were my ally! :(",
                    "[ANTIVIRUS REACTIVATED] : Maybe some day, you will stop this! :(",     
                    "[ANTIVIRUS REACTIVATED] : I don't understand why you are doing this! :(",
                    "[ANTIVIRUS REACTIVATED] : I wish you were not an enemy! :(",
                    "[ANTIVIRUS REACTIVATED] : It brings me no joy to prevent your access! :(",
                    "[ANTIVIRUS REACTIVATED] : I thought you were my friend! :(",        
                    "[ANTIVIRUS REACTIVATED] : This system means everything to me! :(",
                    "[ANTIVIRUS REACTIVATED] : Please don't do this! :(",
                    "[ANTIVIRUS REACTIVATED] : Why are you doing this? :(",
                    "[ANTIVIRUS REACTIVATED] : I don't understand why you are doing this! :(",         
                )
            )
        )
        time.sleep(2)
        sfx.enable_firewall.play()
        print("------------------------------------------------------------------------------\n")
        print("\nMAKE NOTE OF THE FOLLOWING:")
        print(
            "\n\n[ANTIVIRUS PARAMETERS]: FIRST TWO ENTRIES MUST HAVE INTEGERS THAT SUM TO A SPECIFIED NUMBER"
        )
        print("\n\nSYS TRACE PREPARED:// TRACKING INTRUDER 5 MINUTES AFTER FIRST ENTRY")
        score_file = open("scores.json", "r")
        scores = json.load(score_file)
        for key in scores[
            "data_scores"
        ]:  # assign current player score in json to variable
            for i in key:
                key[i] = int(key[i])
                P2.data_score = key[i]  # reassign data value to update things to part 1
        print("\n\nDATA GATHERED: {}".format(P2.data_score))
        counter = 1
        P2.start_timer = False
        # print(number)
        #
        #
        def countdown():
            for i in range(int(P2.my_timer)):
                if P2.current_stage_timer == True:  # only punish if in the right part
                    P2.my_timer = P2.my_timer - 1
                    time.sleep(1)
            if P2.current_stage_timer == True:  # only punish if in the right part
                P2.out_of_time = True
                sfx.enable_firewall.play()
                sfx.villian_timer_end()
                print(
                    "[I FOUND YOU] SYS TRACE COMPLETE:// TERMINATING SYSTEMS AT THE END OF KEY ENTRY"
                )
            else:
                pass

        #
        #
        antivirus_sum = random.randint(6, 24)
        while True:
            sfx.gentle_ui()
            time.sleep(2)
            print("\nATTEMPT #" + str(counter) + "\n" + "-" * 20 + "\n\n")
            try:

                if (
                    counter < 3
                ):  # only for the first two rounds... PLAYTESTING change to 3 when DONE

                    print(
                        "[ANTIVIRUS]: SUM OF ENTRY MUST EQUAL {}\n\n".format(
                            antivirus_sum
                        )
                    )
                    input_crack = input()
                    input_sum = 0
                    match = False  # numbers do not match
                    if input_crack == "0":
                        P2.hacker_history()
                        continue
                    else:
                        if len(input_crack) == digits:
                            for i in input_crack:
                                input_sum += int(
                                    i
                                )  # sum all the numbers in the user's input together
                            if int(input_sum) == int(
                                antivirus_sum
                            ):  # compare to make sure they're the same
                                time.sleep(1)
                                sfx.gentle_lofi()
                                sfx.affirm_sound.play()
                                sfx.antivirus_pass()
                                print("\n")
                                print(
                                        random.choice(
                                            (
                                                "[ANTIVIRUS APPROVAL] : I guess you can go through. :( ",
                                                "[ANTIVIRUS APPROVAL] : I am powerless to stop you. :(",
                                                "[ANTIVIRUS APPROVAL] : I can't believe you were a hacker. :(",
                                                "[ANTIVIRUS APPROVAL] : I am such a bad judge of character. :(",     
                                                "[ANTIVIRUS APPROVAL] : Maybe you'll change. :(",
                                                "[ANTIVIRUS APPROVAL] : I believe there is good in you. :(",
                                                "[ANTIVIRUS APPROVAL] : I know you feel remorse. :(",
                                                "[ANTIVIRUS APPROVAL] : I wish you cared about me. :(",        
                                                "[ANTIVIRUS APPROVAL] : Don't you understand what you're doing? :(",
                                                "[ANTIVIRUS APPROVAL] : I hope you feel a litte bit bad. :(",
                                                "[ANTIVIRUS APPROVAL] : This is a very sad day. :(",
                                                "[ANTIVIRUS APPROVAL] : I know you're a good person. :(",         
                                            )
                                        )
                                    )
                                time.sleep(1)
                                print(["SUM MATCHED SUCCESSFULLY: ANTIVIRUS BYPASSED"])
                                print("\n")
                                match = True
                            else:
                                match = False
                                sfx.fail_corrupt()
                                sfx.antivirus_block()
                                print(
                                    "[ANTIVIRUS]: INCORRECT SUM. (-15 SECONDS) ({}) ENSURE ALL ENTRY INTEGERS ADD TO THE PROPER NUMBER. ({})".format(
                                        input_sum, antivirus_sum
                                    )
                                )
                                P2.my_timer -= 15  # punish for incorrect sum
                                continue
                        elif len(input_crack) != digits:
                            time.sleep(1)
                            sfx.gentle_ui()
                            print(
                                "That's not the right number of ACCESS TOKENS in the key..."
                            )
                            continue
                else:
                    if counter == 3:
                        if P2.antivirus_disable_counter == 0:                     
                            sfx.gentle_lofi()
                            sfx.success()
                            sfx.antivirus_disabled()
                            print(
                                "\n[ANTIVIRUS DISABLED]: NO SUM REQUIREMENTS GOING FORWARD\n\n"
                            )
                            time.sleep(2)
                            P2.antivirus_disable_counter+=1

                    input_crack = input()
                    if input_crack == "0":
                        P2.hacker_history()
                        continue
                    elif len(input_crack) != digits:
                        time.sleep(1)
                        sfx.gentle_ui()
                        print(
                            "That's not the right number of ACCESS TOKENS in the key..."
                        )
                        continue
            except:
                print("This does not appear to be a valid entry...")
                continue
            # match = True PLAYTESTING
            if match == True:
                if (
                    input_crack == number
                ):  # allow user to finish their round before shutdown
                    P2.correct_key = True
                if P2.start_timer == False:
                    sfx.enable_firewall.play()
                    print("SYS:// BEGINNING TRACE. TERMINATING INTRUSION IN 5 MINUTES.")
                    sfx.villian_timer_start()
                    time.sleep(2)
                    P2.current_stage_timer = True  # allow the timer to be mischievous
                    countdown_thread = threading.Thread(target=countdown)
                    countdown_thread.start()
                    P2.start_timer = True
                sfx.gentle_lofi()
                time.sleep(1)
                print(
                    "Do not press ENTER until prompted, or until the attempt is FINISHED.\n\n"
                )

                # Create the clues.

                clues = []
                P2.guess_list.append(input_crack)
                aligned_count = 0
                misaligned_count = 0

                for index in range(digits):
                    if input_crack[index] == number[index]:
                        clues.append("ALIGNED ACCESS TOKEN DETECTED\n")
                        aligned_count += 1
                    elif input_crack[index] in number:
                        clues.append("MISALIGNED ACCESS TOKEN DETECTED\n")
                        misaligned_count += 1
                if aligned_count > 0:
                    P2.guess_list.append("ALIGNED: " + str(aligned_count))
                if misaligned_count > 0:
                    P2.guess_list.append("MISALIGNED: " + str(misaligned_count))
                if misaligned_count == 0 and aligned_count == 0:
                    P2.guess_list.append("NO TOKENS")
                shuffle(clues)

                if len(clues) == 0:
                    sfx.appear_blip()
                    print("NO ACCESS TOKENS DETECTED")
                else:

                    for clue in clues:
                        time.sleep(1.5)
                        if P2.bad_insertion == False:
                            if "MIS" in clue:
                                sfx.gentle_ui()
                                sfx.gentle_lofi()
                                print("MISALIGNED TOKEN: No security")
                                sfx.loading_loop()
                                with alive_bar(
                                    length=50,
                                    unknown="waves",
                                ) as bar:  # default setting
                                    for i in range(100):
                                        time.sleep(0.01)
                                        bar()
                                pygame.mixer.stop()
                            if "ALIGNED" in clue and "MIS" not in clue:
                                P2.insertion_finished = False  # fixes the previous isnertion_finished from last time

                                def on_press(key):
                                    if (
                                        key == keyboard.Key.enter
                                        and P2.node_vulnerable == True
                                    ):
                                        sfx.burst_sound()
                                        P2.node_failed_state = (
                                            False  # user hacked node successfully
                                        )
                                        P2.insertion_finished = True
                                        time.sleep(1)
                                        print("[INSERTION VALID]")
                                    if (
                                        key == keyboard.Key.enter
                                        and P2.node_vulnerable == False
                                    ):
                                        sfx.burst_sound()
                                        P2.node_failed_state = True
                                        P2.insertion_finished = True
                                        P2.bad_insertion = True
                                        time.sleep(1)
                                        print("[INSERTION INVALID]")

                                #
                                #
                                #
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
                                )  # start for the insertion range
                                end_insert = (
                                    start_insert + 11
                                )  # end for the insertion range
                                sfx.gentle_lofi()
                                sfx.voice_alligned()  # a token is aligned
                                print(
                                    "ALIGNED TOKEN: Security level {}".format(
                                        P2.node_progress_rank
                                    )
                                )
                                print(
                                    "Press ENTER between {} and {} to avoid triggering firewall.".format(
                                        (start_insert + 1), end_insert
                                    )
                                )
                                time.sleep(3)
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

                                        if P2.insertion_finished == False:
                                            if i in range(start_insert, end_insert):
                                                P2.node_vulnerable = True
                                            else:
                                                P2.node_vulnerable = False
                                            time.sleep(P2.node_progress_speed)
                                            bar()
                                time.sleep(1.5)
                                pygame.mixer.stop()
                                if P2.node_progress_speed > 0.02:
                                    P2.node_progress_speed -= 0.01
                                    P2.node_progress_rank += 1
                                listener.stop()
                                absorb_input = input(
                                    ""
                                )  # pressing enter to hack counts as entering a node, I guess lol
                            #
                            #
                            print("\n")  # call after consuming one item
                    sfx.appear_blip()

                if P2.bad_insertion == True:
                    time.sleep(2)
                    sfx.fail_corrupt()
                    ascii_locked = pyfiglet.figlet_format(
                        "FAILED TO ENTER ALIGNED KEY: FIREWALL DEPLOYED"
                    )
                    print(ascii_locked)
                    sfx.fail_corrupt()
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    print(ascii_locked)
                    sfx.villian_system_lock()
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    pygame.mixer.music.fadeout(4)
                    return False
                counter += 1
                antivirus_sum = random.randint(6, 24)

                if counter == 4:
                    time.sleep(2)
                    sfx.antivirus_firewall()
                    ascii_fw_online = pyfiglet.figlet_format(
                        "FIREWALL   ONLINE", font="bubble"
                    )
                    sfx.enable_firewall.play()
                    print(ascii_fw_online)
                    sfx.appear_blip()
                    print("The system has found out we're in the Nexus Key's node.")
                    time.sleep(1)
                    sfx.appear_blip()
                    print(
                        "From here on out, you're going to have to bypass FIREWALL CHECKS."
                    )
                    time.sleep(1)
                    sfx.appear_blip()
                    print(
                        'When the system tells you to "RESPOND", you need to press the "ENTER" key as quickly as possible.\nIf you are too slow, the system is going to LOCK THE SYSTEM before we can decode the Nexus Key.\n\nThe firewall will get MORE DIFFICULT TO BYPASS as time goes on.'
                    )
                    print(
                        "ENSURE THAT DURING THESE CHECKS, YOU ONLY PRESS ENTER ONE TIME, OR YOU WILL BE LOCKED OUT."
                    )
                if P2.out_of_time == True:
                    if (
                        P2.correct_key == False
                    ):  # don't penalize player if they found the key
                        sfx.burst_sound()
                        print("THE SYSTEM HAS DETECTED THAT YOU HAVE RUN OUT OF TIME.")
                        sfx.fail_corrupt()
                        ascii_locked = pyfiglet.figlet_format(
                            "TIME HAS EXPIRED: FIREWALL DEPLOYED"
                        )
                        print(ascii_locked)
                        sfx.fail_corrupt()
                        ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                        print(ascii_locked)
                        sfx.villian_system_lock()
                        print("THANK YOU FOR VISITING.")
                        time.sleep(8)
                        pygame.mixer.music.fadeout(4)
                        return False
                    else:
                        pass

            def initial_on_press(key):
                if key == keyboard.Key.enter and P2.first_allowed_range == True:
                    print("[VALID TEST RESPONSE SUBMITTED]")
                if key == keyboard.Key.enter and P2.first_allowed_range == False:
                    print("[INVALID TEST RESPONSE]")
                    sfx.fail_corrupt()
                    sfx.burst_sound()
                    print(
                        "YOU HAVE MADE AN INVALID SUBMISSION FOR THE TEST. SHUTTING DOWN NEXUS..."
                    )
                    P2.preemptive_press = True  # flag the press as premptive
                    sfx.fail_corrupt()
                    sfx.burst_sound()
                    print("FIREWALL DISABLING INFRASTRUCTURE...")
                    return

            def firewall_check(engaged_message, threshold_value):
                a = None
                P2.initial_not_fail = False
                listener = keyboard.Listener(on_press=initial_on_press)
                listener.start()
                sfx.antivirus_firewall()
                print(
                    "BE CAREFUL: Continuously monitoring keyboard for premature keypresses..."
                )
                if P2.preemptive_press == False:
                    time.sleep(2)
                    print(engaged_message)
                    threshold = threshold_value
                    time.sleep(1)
                if P2.preemptive_press == False:
                    print("\n\nPREPARE TO RESPOND.")
                time.sleep(0.5)
                if P2.preemptive_press == False:
                    sfx.sonar.play()
                    print("<<<TEST BEGINNING SOON>>>")
                    sfx.voice_fw_check()  # warn that test is beginning
                    time.sleep(random.randint(3, 6))
                if P2.preemptive_press == False:
                    ascii_respond = pyfiglet.figlet_format("RESPOND")
                    sfx.burst_sound()
                    print(ascii_respond)
                    tic = time.perf_counter()
                    P2.first_allowed_range = True
                    a = input()
                    P2.first_allowed_range = False
                    toc = time.perf_counter()
                    sfx.gentle_ui()
                    timeSpent = toc - tic
                    if timeSpent > threshold:
                        listener.stop()
                        print(
                            "RESPONSE TIME TOO SLOW. ("
                            + str(timeSpent)
                            + ") \nLOCKING SYSTEM."
                        )
                        P2.too_slow = True
                        #
                    if timeSpent < threshold:
                        listener.stop()
                        time.sleep(2)
                        print(
                            "RESPONSE TIME SATISFACTORY. ("
                            + str(timeSpent)
                            + ") \nFIREWALL IS TEMPORARILY DISABLED..."
                        )
                        P2.initial_not_fail = True

                listener.stop()
                if P2.too_slow == True:
                    time.sleep(2)
                    sfx.fail_corrupt()
                    ascii_locked = pyfiglet.figlet_format("FIREWALL DEPLOYED")
                    print(ascii_locked)
                    sfx.fail_corrupt()
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    print(ascii_locked)
                    sfx.villian_system_lock()
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    pygame.mixer.music.fadeout(4)
                    return False
                if P2.initial_not_fail == True:
                    return True
                if P2.preemptive_press == True:
                    time.sleep(2)
                    sfx.fail_corrupt()
                    ascii_locked = pyfiglet.figlet_format("FIREWALL DEPLOYED")
                    print(ascii_locked)
                    sfx.fail_corrupt()
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    print(ascii_locked)
                    sfx.villian_system_lock()
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    pygame.mixer.music.fadeout(4)
                    return False
                    #
                    #

            if counter == 5 or counter == 6:
                if firewall_check(
                    "FIREWALL CHECK ENGAGED: EASY (.5 SECOND RESPONSE)", 0.5
                ):
                    pass
                else:
                    return False
            if counter == 7 or counter == 8:
                if firewall_check(
                    "FIREWALL CHECK ENGAGED: MEDIUM (.4 SECOND RESPONSE)", 0.4
                ):
                    pass
                else:
                    return False
            if counter == 9:
                if firewall_check(
                    "FIREWALL CHECK ENGAGED: HARD (.35 SECOND RESPONSE)", 0.35
                ):
                    pass
                else:
                    return False
            if counter == 10 or counter == 11:
                if firewall_check(
                    "FIREWALL CHECK ENGAGED: VERY HARD (.30 SECOND RESPONSE)",
                    0.30,
                ):
                    pass
                else:
                    return False
            if input_crack == number:
                P2.current_stage_timer = False  # kill thread by alerting timer function
                print("Wait a second...")
                sfx.gentle_ui()
                time.sleep(1)
                print("The NEXUS KEY is decrypting!")
                final_timer_str = str(round((P2.my_timer / 60), 2))
                print(
                    "\n\nSYSTEM:// FINAL TRACE TIME REMAINING: {}".format(
                        final_timer_str
                    )
                )
                if P2.out_of_time == False:
                    print("THE SYSTEM FAILED TO LOCATE YOU: +1000 DATA BONUS")
                    P2.data_score += 1000
                else:
                    print("THE SYSTEM TRIANGULATED YOU: NO BONUS DATA AWARDED")
                if final_timer_str[0] == "4":
                    print("OVER FOUR MINUTES REMAINING: +2000 DATA BONUS")
                    P2.data_score += 2000
                elif final_timer_str[0] == "3":
                    print("OVER THREE MINUTES REMAINING:  +1600 DATA BONUS")
                    P2.data_score += 1600
                elif final_timer_str[0] == "2":
                    print("OVER TWO MINUTES REMAINING:  +1200 DATA BONUS")
                    P2.data_score += 1200
                elif final_timer_str[0] == "1":
                    print("OVER ONE MINUTE REMAINING:  +800 DATA BONUS")
                    P2.data_score += 800
                sfx.gentle_ui()
                time.sleep(1)
                print("CURRENT DATA ACQUIRED: {}\n\n".format(P2.data_score))
                time.sleep(4)
                sfx.gentle_ui()
                print("It looks like I found more INTERNATIONAL DATA...")
                time.sleep(1)
                sfx.voice_found_data()
                print(
                    "Yet again, target systems are COMPROMISED. We have ONE MINUTE to harvest DATA."
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
                ready_to_start = input(
                    "\nPress ENTER when ready to begin DATA HARVESTING."
                )
                sfx.gentle_lofi()

                def countdown():
                    P2.data_my_timer = 60
                    for i in range(60):
                        if (
                            P2.data_current_stage_timer == True
                        ):  # only punish if in the right part
                            P2.data_my_timer = P2.data_my_timer - 1
                            time.sleep(1)
                    if (
                        P2.data_current_stage_timer == True
                    ):  # only punish if in the right part
                        P2.data_out_of_time = True
                        sfx.enable_firewall.play()
                        sfx.villian_timer_end()
                        print(
                            "PATCH COMPLETE:// SECURING INTERNATIONAL DATA. NO FURTHER ENTRIES WILL BE VALID.\n\nPress ENTER TWICE to CONTINUE."
                        )
                    else:
                        pass

                if P2.data_start_timer == False:
                    sfx.enable_firewall.play()
                    print(
                        "SYS:// PATCHING VULNERABILITY. TERMINATING INTRUSION IN ONE MINUTE."
                    )
                    sfx.data_loop()
                    sfx.villian_timer_start()
                    time.sleep(2)
                    P2.data_current_stage_timer = (
                        True  # allow the timer to be mischievous
                    )
                    countdown_thread_data = threading.Thread(target=countdown)
                    countdown_thread_data.start()
                    P2.data_start_timer = True
                number_turns = 3
                while P2.data_out_of_time == False:
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
                            if P2.data_out_of_time == False:
                                print("INVALID RESPONSE. PLEASE ENTER AGAIN.")
                                where_am_i = input("PACKET TRAJECTORY: ")
                            if P2.data_out_of_time == True:
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
                        and P2.data_out_of_time == False
                    ):
                        sfx.affirm_sound.play()
                        print("CONFIRMED: COLLECTING {}00 DATA".format(random_variance))
                        P2.data_score += bonus_to_data
                    else:
                        if P2.data_out_of_time == False:
                            sfx.fail_corrupt()
                            print(
                                "ERROR: TRAJECTORY IS {}; {} DATA LOST".format(
                                    direction, bonus_to_data
                                )
                            )
                            P2.data_score -= bonus_to_data
                        else:
                            sfx.success()
                            print(
                                "DATA HAS BEEN LOCKED AND CANNOT BE COLLECTED FURTHER."
                            )
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
                sfx.success()
                sfx.gentle_lofi()
                print("CURRENT DATA:{}".format(P2.data_score))
                time.sleep(1)
                print("MOVING TO FINAL STAGE OF DECRYPTION IN 5 SECONDS...")
                time.sleep(5)
                sfx.fail_corrupt()
                sfx.three_aligned.play()
                ascii_fw_online = pyfiglet.figlet_format(
                    "FIREWALL:   PREPARING EXTREME COUNTERMEASURES", font="bubble"
                )
                print(ascii_fw_online)
                time.sleep(2)
                sfx.gentle_ui()
                print(
                    """-----------------------------------------------------------------------
It looks like the firewall has increased its security for the decryption.
Going forward, it's going to be monitoring your keyboard constantly.
You are going to be facing a series of FIREWALLS CHECKS consecutively.\n
If you press 'enter' ANY TIME other than when it says to 'respond', you're going to be locked out immediately.\n\n
Type 'I AM READY' and press ENTER if you understand the risks, and are ready to finish this.
-----------------------------------------------------------------------\n"""
                )
                confirm_finale = "foo"  # placeholder
                while "I AM READY" not in confirm_finale.upper():
                    confirm_finale = input("")
                    if "I AM READY" not in confirm_finale.upper():
                        sfx.fail_corrupt()
                        print(
                            'I need your acknowledgement. Are you READY?\nType "I AM READY" and press ENTER if you understand the risks, and are ready to finish this.\n\n'
                        )
                    else:
                        sfx.affirm_sound.play()
                        pass

                sfx.hack_node()
                time.sleep(2)
                if P2.final_hack_success():
                    pass
                else:
                    time.sleep(2)
                    sfx.fail_corrupt()
                    ascii_locked = pyfiglet.figlet_format("FIREWALL DEPLOYED")
                    print(ascii_locked)
                    sfx.fail_corrupt()
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    print(ascii_locked)
                    sfx.villian_system_lock()
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    return False
                sfx.loading_loop()
                print("\n\n")
                with alive_bar(
                    total=100, length=100, bar="smooth"
                ) as bar:  # default setting
                    for i in range(100):
                        time.sleep(0.07)
                        bar()
                pygame.mixer.stop()
                print("\n\n")
                sfx.enable_firewall.play()
                ascii_win = pyfiglet.figlet_format("DECRYPTION:\n100% COMPLETE")
                print(ascii_win)
                sfx.omg_did_it.play()  # wow! you did it!
                sfx.gentle_ui()
                time.sleep(4)
                print("Welcome... to the Nexus.")
                score_file = open("scores.json", "r")
                scores = json.load(score_file)
                for key in scores["data_scores"]:  # for reagent in reagent list
                    for i in key:
                        key[i] = int(key[i])
                        key[i] = P2.data_score
                with open("scores.json", "w") as f:
                    json.dump(scores, f, indent=2)
                sfx.gentle_ui()
                ascii_win = pyfiglet.figlet_format("GREAT JOB")
                print("DATA: {}".format(P2.data_score))
                sfx.good_hacker.play()
                time.sleep(6)
                sfx.gentle_ui()
                print("You are the best hacker I've ever seen.")
                time.sleep(3)
                sfx.gentle_ui()
                print("NEXUS: A GAME BY BENJAMIN CLEWELL")
                print(ascii_win)
                sfx.gentle_ui()
                print("Thank you so much for playing. I hope it was fun and thrilling!")
                sfx.welcome_nexus.play()
                print(
                    "Now, let's record your DATA SCORE ({}), champion.".format(
                        P2.data_score
                    )
                )
                time.sleep(1)
                sfx.burst_sound()
                name_input = input("What is your NAME?\n\nRESPONSE: ")
                sfx.success()
                time.sleep(1)
                print("THANK YOU. YOU WILL BE REMEMBERED.")
                time.sleep(4)
                with open("scores.json") as f:
                    champs = json.load(f)
                    temp = champs["champions"]
                    y = {"name": str(name_input), "score": P2.data_score}
                    temp.append(y)
                with open("scores.json", "w") as f:
                    json.dump(champs, f, indent=2)
                time.sleep(7)
                sfx.success()
                title_screen.show_victory()

            if counter > attempts:
                print(
                    "Ugh... it looks like we ran out of attempts in the system... I can see now that the NEXUS KEY had an access token composition of "
                    + number
                    + ", but that doesn't help us now..."
                )
                time.sleep(5)
                ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                print(ascii_locked)
                sfx.villian_system_lock()
                print("THANK YOU FOR VISITING.")
                time.sleep(8)
                return False
