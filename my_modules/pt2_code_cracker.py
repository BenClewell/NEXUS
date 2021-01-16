import random
from random import sample, shuffle, choice
from random import randint

import pyfiglet
import pyfiglet.fonts
import pygame
from pygame import mixer

from alive_progress import alive_bar # cool loading animations

import time

from my_modules import title_screen
from my_modules import sfx

import keyboard
import threading
import win32api
import pynput
from pynput import keyboard
from importlib import reload

# allow the nexus timer to decrypt in the background


class P2:
    """house all methods and unify all global variables"""

    preemptive_press = (
        False  # start of p2, monitor enter presses (multithread)
    )
    first_allowed_range = (
        False  # start p2, are you in the allowed keypress range?
    )
    initial_not_fail = False
    #
    #
    too_many_presses = False  # endgame, monitor enter presses (multithread)
    allowed_range = (
        False  # multithread, are you in the allowed keypress range?
    )
    # DISABLED time_is_up  = False #endgame, monitor timer (multithread)
    final_roundcount = 1
    rounds_done = False
    too_slow = False  # endgame, monitor speed
    #
    #
    #

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

        sfx.play_mp3_once("/bgm/bgm_6.mp3")
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
                time.sleep(2)
                if P2.final_roundcount == 1:
                    print("FIREWALL CHECK ENGAGED: EASY (.5 SECOND RESPONSE)")
                    ascii_prog = pyfiglet.figlet_format(
                        "DECRYPTION:\n33% COMPLETE"
                    )
                    sfx.gentle_ui()
                    print(ascii_prog)
                    threshold = 0.5
                if P2.final_roundcount == 2:
                    print(
                        "FIREWALL CHECK ENGAGED: MEDIUM (.4 SECOND RESPONSE)"
                    )
                    ascii_prog = pyfiglet.figlet_format(
                        "DECRYPTION:\n66% COMPLETE"
                    )
                    sfx.gentle_ui()
                    print(ascii_prog)
                    threshold = 0.4
                if P2.final_roundcount == 3:
                    ascii_prog = pyfiglet.figlet_format(
                        "DECRYPTION:\n99% COMPLETE"
                    )
                    sfx.gentle_ui()
                    print(ascii_prog)
                    print("FIREWALL CHECK ENGAGED: HARD (.35 SECOND RESPONSE)")
                    threshold = 0.35
                sfx.sonar.play()
                time.sleep(1)
            if P2.too_many_presses == False:
                print("\n\nPREPARE TO RESPOND.")
            time.sleep(0.5)
            if P2.too_many_presses == False:
                print("<<<TEST BEGINNING SOON>>>")
                time.sleep(random.randint(2, 5))
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
                    P2.final_roundcount += 1  # do another round, until five rounds have been played
                    if P2.final_roundcount > 3:
                        P2.rounds_done = True
                    else:
                        final_challenge()

        final_challenge()
        #
        listener.stop()

        if P2.too_slow == True:
            sfx.burst_sound()
            print('RESPONSE TOO SLOW.')
            time.sleep(1)
            pygame.mixer.music.fadeout(4)
            return False
        if P2.rounds_done == True:
            return True
        if P2.too_many_presses == True:
            pygame.mixer.music.fadeout(4)
            return False
        """
        def countdown():
            # multithreading timer. DISABLED FOR NOW, MIGHT IMPLEMENT LATER
            my_timer = 55
            for x in range(55):
                my_timer = my_timer -1
                time.sleep(1)
            print("OUT OF TIME")
            time_is_up = True
        countdown_thread = threading.Thread(target = countdown)
        countdown_thread.start()


        while my_timer > 0:
            time.sleep(1)
            final_challenge()
            time.sleep(1)
        print('You have finished.')
        time_is_up = True
        """
        #
        '''
        def monitor_enter_key():  # 0x0D is enter
            """track the number of enter presses"""
            P2.enter_count = 0
            while (
                P2.final_roundcount <= 3
                and P2.enter_count < 2
                and P2.too_many_presses == False
            ):
                a = win32api.GetKeyState(0x0D)
                if a < 0:
                    P2.enter_count += 1
                    time.sleep(1)
            while P2.final_roundcount <= 3:
                if P2.enter_count > 1:
                    print("YOU HAVE PRESSED ENTER OUTSIDE A TEST")
                    time.sleep(2)
                    print("REPORTING YOU TO THE NEXUS...")
                    P2.too_many_presses = True
                    return

        while (
            P2.too_many_presses == False
            and P2.too_slow == False
            and P2.rounds_done == False
        ):
        '''

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
                print(
                    "That's not the right number of ACCESS TOKENS in the key..."
                )
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
                for clue in clues:
                    if 'MIS' in clue:
                        sfx.gentle_ui()
                        with alive_bar(length=100, unknown='waves',) as bar:   # default setting
                            for i in range(100):
                                time.sleep(0.01)
                                bar()     
                    if 'ALIGNED' in clue and 'MIS' not in clue:
                        sfx.gentle_ui()
                        with alive_bar(total=100, length=50, bar='squares',) as bar:   # default setting
                            for i in range(100):
                                time.sleep(0.01)
                                bar()       
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
                print(
                    "The system has found out we're in the Nexus Key's node."
                )
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

            def initial_on_press(key):
                if (
                    key == keyboard.Key.enter
                    and P2.first_allowed_range == True
                ):
                    print("[VALID TEST RESPONSE SUBMITTED]")
                if (
                    key == keyboard.Key.enter
                    and P2.first_allowed_range == False
                ):
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
                    print("<<<TEST BEGINNING SOON>>>")
                    time.sleep(random.randint(2, 5))
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
                print("Wait a second...")
                sfx.gentle_ui()
                time.sleep(1)
                print("The NEXUS KEY is decrypting!")
                sfx.gentle_ui()
                time.sleep(1)
                sfx.gentle_ui()
                print(
                    "You just need to protect against the firewall while it decrypts..."
                )
                time.sleep(2)
                sfx.fail_corrupt()
                ascii_fw_online = pyfiglet.figlet_format(
                    "FIREWALL:   SECURITY   INCREASED", font="bubble"
                )
                time.sleep(2)
                sfx.gentle_ui()
                warning = input(
                    """-----------------------------------------------------------------------
It looks like the firewall has increased its security for the decryption.
Going forward, it's going to be monitoring your keyboard constantly.
You are going to be facing a series of FIREWALLS CHECKS consecutively.\n
If you press 'enter' ANY TIME other than when it says to 'respond', you're going to be locked out immediately.\n
Press ENTER one more time if you understand the risks, and are ready to finish this.
-----------------------------------------------------------------------"""
                )
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
                    print("THANK YOU FOR VISITING.")
                    time.sleep(8)
                    return False
                ascii_win = pyfiglet.figlet_format(
                    "DECRYPTION:\n100% COMPLETE"
                )
                print(ascii_win)
                sfx.gentle_ui()
                time.sleep(3)
                print("Welcome... to the Nexus.")
                sfx.gentle_ui()
                ascii_win = pyfiglet.figlet_format("GREAT JOB")
                time.sleep(6)
                sfx.gentle_ui()
                print("You are the best hacker I've ever seen.")
                time.sleep(7)
                sfx.gentle_ui()
                print("NEXUS: A GAME BY BENJAMIN CLEWELL")
                print(ascii_win)
                time.sleep(7)
                sfx.gentle_ui()
                print(
                    "Thank you so much for playing. I hope it was fun and thrilling!"
                )
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
