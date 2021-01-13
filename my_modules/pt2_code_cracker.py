import random
from random import sample, shuffle, choice
from random import randint

import pyfiglet
import pyfiglet.fonts
import pygame
from pygame import mixer

import time

from my_modules import title_screen
from my_modules import sfx

import keyboard
import threading
import win32api
from importlib import reload
# allow the nexus timer to decrypt in the background

class P2:
'''house all methods and unify all global variables'''
too_many_presses = False #endgame, monitor enter presses (multithread)
enter_count = 0
time_is_up  = False #endgame, monitor timer (multithread)
too_slow = False #endgame, monitor speed
#
#
#
    def final_hack_success():
        sfx.play_mp3_once('/bgm/bgm_6.mp3')

        while P2.too_many_presses == False and P2.time_is_up == False and P2.too_slow == False:

            def final_challenge():
                global enter_count
                P1.enter_count = 0
                #
                global too_slow
                global time_is_up
                global too_many_presses
                #
                a = None
                print('DO NOT TOUCH YOUR KEYBOARD UNTIL IT IS TIME TO RESPOND')
                print("FIREWALL CHECK ENGAGED: EASY (.5 SECOND RESPONSE)")
                sfx.sonar.play()
                time.sleep(4)
                print("PREPARE TO RESPOND.")
                time.sleep(3)
                print("<<<TEST BEGINNING SOON>>>")
                time.sleep(random.randint(2, 5))
                if time_is_up == False:
                    ascii_respond = pyfiglet.figlet_format("RESPOND")
                    sfx.burst_sound()
                    print(ascii_respond)
                    tic = time.perf_counter()
                    a = input()
                    toc = time.perf_counter()
                    sfx.gentle_ui()
                    timeSpent = toc - tic
                    if timeSpent > 0.5:
                        print(
                            "RESPONSE TIME TOO SLOW. ("
                            + str(timeSpent)
                            + ") \nLOCKING SYSTEM."
                        )
                        too_slow = True
                        #
                    if timeSpent < 0.5:
                        time.sleep(2)
                        print(
                            "RESPONSE TIME SATISFACTORY. ("
                            + str(timeSpent)
                            + ") \nCONTINUING..."
                        )
                        final_challenge()
                else:
                    pass #time is up!

            global my_timer
            '''the final mission for decrypting the nexus key...'''
            def countdown():
                global my_timer
                global time_is_up
                my_timer = 55
                for x in range(55):
                    my_timer = my_timer -1
                    time.sleep(1)
                print("OUT OF TIME")
                time_is_up = True
                #
                #

            def monitor_enter_key():# 0x0D is enter
                '''track the number of enter presses'''
                global enter_count
                global too_many_presses
                enter_count = 0
                while my_timer > 0:
                    a = win32api.GetKeyState(0x0D)
                    if a < 0:
                        enter_count +=1
                        print(str(enter_count))
                        time.sleep(.5)
                    if enter_count == 2:
                        print('YOU HAVE PRESSED ENTER OUTSIDE A TEST')
                        too_many_presses = True



            countdown_thread = threading.Thread(target = countdown)
            countdown_thread.start()
            monitor_thread = threading.Thread(target = monitor_enter_key)
            monitor_thread.start()


            while my_timer > 0:
                time.sleep(1)
                final_challenge()
                time.sleep(1)
            print('You have finished.')
            time_is_up = True

        if too_slow == True:
            pygame.mixer.music.fadeout(4)
            return False
        if time_is_up == True:
            pygame.mixer.music.fadeout(4)
            return True
        if too_many_presses == True:
            return False

    def decode_key():

        digits = 3
        attempts = 10
        sfx.gentle_ui()
        sfx.success()
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
        print("When the system returns:        That means:\n")
        print(
            "MISALIGNED ACCESS TOKEN         An access token is correct, but positioned wrong."
        )
        print(
            "ALIGNED ACCESS TOKEN            An access token is correct and positioned right."
        )
        print(
            "NO ACCESS TOKENS                None of the access tokens entered are in the key."
        )
        print("\nThere are no repeated ACCESS TOKENS in the key.")

        # Create a random number.

        letters = sample("0123456789", digits)

        if letters[0] == "0":
            letters.reverse()

        number = "".join(letters)
        print(str(number))
        """for play testing purposes"""

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

        counter = 1
        # print(number)

        while True:
            sfx.gentle_ui()
            print("\nATTEMPT #" + str(counter) + "\n" + "-" * 20 + "\n\n")
            input_crack = input()

            if len(input_crack) != digits:
                time.sleep(1)
                sfx.gentle_ui()
                print("That's not the right number of ACCESS TOKENS in the key...")
                continue

            # Create the clues.

            clues = []

            for index in range(digits):
                if input_crack[index] == number[index]:
                    clues.append("ALIGNED ACCESS TOKEN DETECTED\n")
                elif input_crack[index] in number:
                    clues.append("MISALIGNED ACCESS TOKEN DETECTED\n")

            shuffle(clues)

            if len(clues) == 0:
                sfx.appear_blip()
                print("NO ACCESS TOKENS DETECTED")
            else:
                sfx.appear_blip()
                print(" ".join(clues))

            counter += 1

            if counter == 4:
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
            if counter == 5 or counter == 6:
                key_monitor = True
                print("FIREWALL CHECK ENGAGED: EASY (.5 SECOND RESPONSE)")
                sfx.sonar.play()
                time.sleep(4)
                print("PREPARE TO RESPOND.\nREMEMBER: PRESS 'ENTER' ONLY ONE TIME...")
                time.sleep(3)
                print("<<<TEST BEGINNING SOON>>>")
                time.sleep(random.randint(2, 5))
                ascii_respond = pyfiglet.figlet_format("RESPOND")
                sfx.burst_sound()
                print(ascii_respond)
                tic = time.perf_counter()
                a = input()
                toc = time.perf_counter()
                sfx.gentle_ui()
                cheat_check = input(
                    "RESPONSE RECORDED.\nTYPE 'submit' AND PRESS 'ENTER' TO COMMIT YOUR RESPONSE\n\n"
                )
                timeSpent = toc - tic
                if timeSpent > 0.5 or "submit" not in cheat_check.lower():
                    time.sleep(2)
                    if "submit" not in cheat_check.lower():
                        print(
                            "ERROR: CORRUPTED SUBMISSION.\n\nLOCKING SYSTEMS DUE TO FAILED RESPONSE SUBMISSION."
                        )
                    if timeSpent > 0.5:
                        print(
                            "RESPONSE TIME TOO SLOW. ("
                            + str(timeSpent)
                            + ") \nLOCKING SYSTEM."
                        )
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    sfx.fail_corrupt()
                    print(ascii_locked)
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    return False
                if timeSpent < 0.5 and "submit" in cheat_check.lower():
                    time.sleep(2)
                    print(
                        "RESPONSE TIME SATISFACTORY. ("
                        + str(timeSpent)
                        + ") \nYOU MAY PROCEED"
                    )
            if counter == 7 or counter == 8:
                key_monitor = True
                print("FIREWALL CHECK ENGAGED: MEDIUM (.4 SECOND RESPONSE)")
                sfx.sonar.play()
                time.sleep(4)
                print("PREPARE TO RESPOND\nREMEMBER: PRESS 'ENTER' ONLY ONE TIME...")
                time.sleep(3)
                print("<<<TEST BEGINNING SOON>>>")
                time.sleep(random.randint(2, 5))
                sfx.burst_sound()
                ascii_respond = pyfiglet.figlet_format("RESPOND")
                print(ascii_respond)
                tic = time.perf_counter()
                a = input()
                toc = time.perf_counter()
                sfx.gentle_ui()
                cheat_check = input(
                    "RESPONSE RECORDED.\nTYPE 'submit' AND PRESS 'ENTER' TO COMMIT YOUR RESPONSE\n\n"
                )
                timeSpent = toc - tic
                if timeSpent > 0.4 or "submit" not in cheat_check.lower():
                    time.sleep(2)
                    if "submit" not in cheat_check.lower():
                        print(
                            "ERROR: CORRUPTED SUBMISSION.\n\nLOCKING SYSTEMS DUE TO FAILED RESPONSE SUBMISSION."
                        )
                    if timeSpent > 0.4:
                        print(
                            "RESPONSE TIME TOO SLOW. ("
                            + str(timeSpent)
                            + ") \nLOCKING SYSTEM."
                        )
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    sfx.fail_corrupt()
                    print(ascii_locked)
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    return False
                if timeSpent < 0.4 and "submit" in cheat_check.lower():
                    time.sleep(2)
                    print(
                        "RESPONSE TIME SATISFACTORY. ("
                        + str(timeSpent)
                        + ") \nYOU MAY PROCEED"
                    )
            if counter == 9:
                key_monitor = True
                print("FIREWALL CHECK ENGAGED: HARD (.35 SECOND RESPONSE)")
                sfx.sonar.play()
                time.sleep(4)
                print("PREPARE TO RESPOND\nREMEMBER: PRESS 'ENTER' ONLY ONE TIME...")
                time.sleep(3)
                print("<<<TEST BEGINNING SOON>>>")
                time.sleep(random.randint(2, 5))
                ascii_respond = pyfiglet.figlet_format("RESPOND")
                sfx.burst_sound()
                print(ascii_respond)
                tic = time.perf_counter()
                a = input()
                toc = time.perf_counter()
                sfx.gentle_ui()
                cheat_check = input(
                    "RESPONSE RECORDED.\nTYPE 'submit' AND PRESS 'ENTER' TO COMMIT YOUR RESPONSE\n\n"
                )
                timeSpent = toc - tic
                if timeSpent > 0.35 or "submit" not in cheat_check.lower():
                    time.sleep(2)
                    if "submit" not in cheat_check.lower():
                        print(
                            "ERROR: CORRUPTED SUBMISSION.\n\nLOCKING SYSTEMS DUE TO FAILED RESPONSE SUBMISSION."
                        )
                    if timeSpent > 0.35:
                        print(
                            "RESPONSE TIME TOO SLOW. ("
                            + str(timeSpent)
                            + ") \nLOCKING SYSTEM."
                        )
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    sfx.fail_corrupt()
                    print(ascii_locked)
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    return False

                if timeSpent < 0.35 and "submit" in cheat_check.lower():
                    time.sleep(2)
                    print(
                        "RESPONSE TIME SATISFACTORY. ("
                        + str(timeSpent)
                        + ") \nYOU MAY PROCEED"
                    )
            if counter == 10 or counter == 11:
                key_monitor = True
                print("FIREWALL CHECK ENGAGED: VERY HARD (.3 SECOND RESPONSE)")
                sfx.sonar.play()
                time.sleep(4)
                print("PREPARE TO RESPOND\nREMEMBER: PRESS 'ENTER' ONLY ONE TIME...")
                time.sleep(3)
                print("<<<TEST BEGINNING SOON>>>")
                time.sleep(random.randint(2, 5))
                ascii_respond = pyfiglet.figlet_format("RESPOND")
                sfx.burst_sound()
                print(ascii_respond)
                tic = time.perf_counter()
                a = input()
                toc = time.perf_counter()
                sfx.gentle_ui()
                cheat_check = input(
                    "RESPONSE RECORDED.\nTYPE 'submit' AND PRESS 'ENTER' TO COMMIT YOUR RESPONSE\n\n"
                )
                timeSpent = toc - tic
                if timeSpent > 0.30 or "submit" not in cheat_check.lower():
                    time.sleep(2)
                    if "submit" not in cheat_check.lower():
                        print(
                            "ERROR: CORRUPTED SUBMISSION.\n\nLOCKING SYSTEMS DUE TO FAILED RESPONSE SUBMISSION."
                        )
                    if timeSpent > 0.3:
                        print(
                            "RESPONSE TIME TOO SLOW. ("
                            + str(timeSpent)
                            + ") \nLOCKING SYSTEM."
                        )
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    print(ascii_locked)
                    sfx.fail_corrupt()
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    return False
                if timeSpent < 0.30 and "submit" in cheat_check.lower():
                    time.sleep(2)
                    print(
                        "RESPONSE TIME SATISFACTORY. ("
                        + str(timeSpent)
                        + ") \nYOU MAY PROCEED"
                    )

            if input_crack == number:
                print("Wait a second...")
                sfx.gentle_ui()
                time.sleep(1)
                print("The NEXUS KEY is decrypting!")
                sfx.gentle_ui()
                time.sleep(1)
                sfx.fail_corrupt()
                print("You just need to protect against the firewall while it decrypts...")
                if final_hack_success():
                    pass
                else:
                    time.sleep(2)
                    ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
                    print(ascii_locked)
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    return False
                ascii_win = pyfiglet.figlet_format("KEY DECODED: YOU WIN")
                print(ascii_win)
                sfx.gentle_ui()
                time.sleep(2)
                print("Welcome... to the Nexus.")
                print("CONGRATULATIONS")
                time.sleep(5)
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
                print("THANK YOU FOR VISITING.")
                time.sleep(8)
                return False
