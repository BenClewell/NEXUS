import time
import random
import sys
import os
import pyfiglet
import pyfiglet.fonts

# more specific for pyinstaller

from random import sample, shuffle, choice

from random import randint
from asciimatics.screen import Screen
from asciimatics.renderers import Plasma, Rainbow, FigletText
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError


import keyboard  # f11press

from my_modules import sfx
from my_modules import hacking_minigame
from my_modules import message_random as msg

# audio

sfx.play_mp3("art_of_silence.mp3")
num_denials = 3


class PlasmaScene(Scene):
    """play the title card"""

    _comments = ["THE NEXUS", "PRESS Q"]

    def __init__(self, screen):
        self._screen = screen
        effects = [
            Print(
                screen,
                Plasma(screen.height, screen.width, screen.colours),
                0,
                speed=1,
                transparent=False,
            ),
        ]
        super(PlasmaScene, self).__init__(effects, 200, clear=False)

    def add_comment(self):

        msg = FigletText(("NEXUS"), font="big")
        creator = FigletText(("A game by Benjamin Clewell"), font="rectangles")
        self._effects.append(
            Print(
                self._screen,
                msg,
                (self._screen.height // 2) - 4,
                x=(self._screen.width - msg.max_width) // 2 + 1,
                colour=Screen.COLOUR_WHITE,
                stop_frame=30,
                speed=1,
            )
        )

        self._effects.append(
            Print(
                self._screen,
                creator,
                (self._screen.height // 2) + 5,
                x=(self._screen.width - msg.max_width) // 2 - 35,
                colour=Screen.COLOUR_WHITE,
                start_frame=5,
                stop_frame=30,
                speed=1,
            )
        )

        # Changes text to rainbow...

        self._effects.append(
            Print(
                self._screen,
                Rainbow(self._screen, msg),
                (self._screen.height // 2) - 4,
                x=(self._screen.width - msg.max_width) // 2,
                colour=Screen.COLOUR_BLACK,
                stop_frame=30,
                speed=1,
            )
        )

        # START INSTRUCTIONS

        msg = FigletText(
            ("PRESS   Q"),
            font="big",
        )
        self._effects.append(
            Print(
                self._screen,
                msg,
                (self._screen.height // 2) - 4,
                x=(self._screen.width - msg.max_width) // 2 + 1,
                colour=Screen.COLOUR_WHITE,
                start_frame=30,
                speed=1,
            )
        )

        # Changes text to rainbow...

        self._effects.append(
            Print(
                self._screen,
                Rainbow(self._screen, msg),
                (self._screen.height // 2) - 4,
                x=(self._screen.width - msg.max_width) // 2,
                colour=Screen.COLOUR_BLACK,
                start_frame=30,
                speed=1,
            )
        )

    def reset(self, old_scene=None, screen=None):
        super(PlasmaScene, self).reset(old_scene, screen)

        # Make sure that we only have the initial Effect and add a new cheesy
        # comment.
        self._effects = [self._effects[0]]
        self.add_comment()


def intro_plasma(screen):

    screen.play(
        [PlasmaScene(screen)],
        stop_on_resize=True,
    )


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(intro_plasma)
            sfx.click.play()
            sfx.startup.play()
            # force fullscreen keyboard.press_and_release('F11')
            break
        except ResizeScreenError:
            pass


ascii_nexus = pyfiglet.figlet_format("THE    NEXUS")
print(ascii_nexus)


def make_guess():
    try:
        global guess
        guess = int(input())
    except:
        print("INVALID NODE: Please try again.")
        make_guess()


def minigame_hack():
    global guess
    barrier_low = random.randint(25, 50)
    barrier_high = random.randint(50, 75)
    # sets the low and high defense paramters
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

    # view entry key, and the two defense ranges by enabling below
    # print(str(entry_key) + " " + str(barrier_low) + " " + str(barrier_high))

    # print("lol it's " + str(entry_key))
    """the above is for playtesting only"""
    # chances are 5 or 3
    chance_options = [5]
    chances = random.choice(chance_options)
    firstchance = True
    # is this their first time?
    extra_chance = True
    # has the user burnt their final chance?
    tripwire = False
    # has the user set off the defense range?
    collapse = random.randint(2, 2)
    # multiple ints can be passed to collapse for multiple results
    guess_list = []
    sonar_list = []

    # gives an extra chance when dying if close upon death

    low_keys = 3
    high_keys = 3

    ascii_sonar_status = pyfiglet.figlet_format("SONAR", font="digital")

    time.sleep(1)
    print("The NEXUS KEY is encrypted between node 1 and 100.")
    print(
        "Type in any number in this range, and I'll hack that node to look for the NEXUS KEY."
    )

    time.sleep(1)
    ascii_jam_online = pyfiglet.figlet_format("JAMMER   ONLINE", font="bubble")
    print(ascii_jam_online)
    print(
        "DEFENSE RANGE ESTABLISHED.\nSELECTING A NODE WITHIN THE DEFENSE RANGE WILL TRIGGER THE JAMMER."
    )

    if chances == 5:
        sonar = False
        time.sleep(1)
        print(random.choice(msg.chances5))
        print(
            "I would choose either a low node, or a high node to start with."
        )

    print(
        "\nWe have a maximum of 5 chances to locate the key. We can do this."
    )
    print(
        "You can select a node on either side of the NEXUS KEY only 3 times before the AI finds you, so be careful.\n(Do not be consistently high or low.)"
    )

    time.sleep(0.5)
    print(
        "\n\nTo view your hacking history in this system, enter '0' at any point."
    )
    time.sleep(0.5)

    print(
        "----------------------------------------------\nENTER A NODE (between 1 and 100):\n"
    )

    while chances != 0:
        make_guess()

        if guess != 0:
            guess_list.append(guess)
        # Compare the user entered number
        # with the number to be guessed
        if guess == 0:

            def hacker_history():
                """provide history of choices"""
                helpmenu = True
                status_splash = True
                while helpmenu == True:
                    while status_splash == True:
                        time.sleep(1)
                        print("\nBOOTING NETWORK INFORMATION")
                        time.sleep(1)
                        print("--------------------------")
                        time.sleep(1)
                        print("--------------------------" * 2)
                        time.sleep(1)
                        print("--------------------------" * 3)
                        ascii_intel = pyfiglet.figlet_format("HACKING HISTORY")
                        print(ascii_intel)
                        print("\nEntry Information:")
                        if guess_list == []:
                            print("NO ENTRIES COMMITTED YET")
                        if guess_list != []:
                            print("ENTRIES SO FAR: " + str(guess_list))
                        print(
                            "MAXIMUM ENTRIES REMAINING UNTIL SYSTEM LOCK: "
                            + str(chances)
                        )
                        print("LOW ENTRIES REMAINING: " + str(high_keys))
                        print("HIGH ENTRIES REMAINING: " + str(low_keys))

                        print("\nJAMMER Information:")
                        if firstchance == True:
                            print(
                                "DEFENSE RANGE UNKNOWN. PROCEED WITH CAUTION."
                            )
                        if firstchance == False:
                            print(
                                "DEFENSE RANGE: "
                                + str(barrier_low)
                                + " to "
                                + str(barrier_high)
                            )
                        if chances <= 2 and barrier_inside == 2:
                            print("The NEXUS KEY is INSIDE the defense range.")
                        elif chances <= 2 and barrier_inside == 1:
                            print(
                                "The NEXUS KEY is OUTSIDE the defense range."
                            )
                        else:
                            print(
                                "We do not know if the NEXUS KEY is in the defense range."
                            )

                        print("\nSonar Information:")
                        if sonar == False:
                            print("SONAR OFFLINE")
                        if sonar == True:
                            print("SONAR ONLINE")
                            if chances == 3:
                                print("ACCURACY: 30 NUMBER RANGE")
                            if chances == 2:
                                print("ACCURACY: 20 NUMBER RANGE")
                            if chances == 1:
                                print("ACCURACY: 10 NUMBER RANGE")
                        if sonar_list == []:
                            print("NO SONAR HISTORY")
                        if sonar_list != []:
                            print("SONAR HISTORY: " + str(sonar_list))

                        time.sleep(2)
                        print("\nReturning to hacking interface...")
                        time.sleep(1)
                        print(
                            "\n----------------------------------------------\nENTER A KEY (between 1 and 100):\n"
                        )

                        status_splash = False
                        helpmenu = False

            hacker_history()

        else:
            ascii_nodeguess = pyfiglet.figlet_format("NODE  " + str(guess))
            print(ascii_nodeguess)

            sfx.click.play()
            # play sfx
            time.sleep(1)
            sfx.hack_node()
            minigame_chance = randint(1, 2)
            if minigame_chance == 1:
                hacking_minigame.node_hacking_minigame()
            if minigame_chance == 2:
                print("NO FIREWALL DETECTED.")
            # play hacking sound
            print(random.choice(msg.hacking_lines))
            time.sleep(2)
            print(random.choice(msg.hacked_lines))

            if guess == entry_key:
                # if number entered by user
                # is same as the generated
                # number by randint function then
                # break from loop using loop
                # control statement "break"
                print("NEXUS KEY LOCATED.")
                time.sleep(2)
                print("EXTRACTING DATA")
                time.sleep(1)
                ascii_win = pyfiglet.figlet_format("KEY ACQUIRED")
                print(ascii_win)
                time.sleep(5)
                print("Excellent job.")
                time.sleep(2)
                decode_key()

            if (
                firstchance == True
                and chances == 5
                and barrier_low < guess < barrier_high
                and collapse == 2
            ):
                time.sleep(1)
                tripwire = True
                ascii_jammer = pyfiglet.figlet_format(
                    "JAMMER TRIGGERED", font="bubble"
                )
                print(ascii_jammer)
                print(
                    "\n\nENTRY DETECTED IN JAMMER RANGE. SCRAMBLING DATA\n\n"
                )
                time.sleep(3)
                print(
                    "Well... it looks like you landed right in the middle of the defense range.\nThat's going to cost us some valuable information, but it's not the end of the world.\nNext time, I would reccomend starting with a node on the high or low end of the spectrum."
                )
                time.sleep(1)

            """
            if firstchance == True and chances == 5 and barrier_low<=guess<=barrier_high and collapse != 2:
                time.sleep(1)
                print('SYSTEM MALFUNCTION: JAMMER COUNTERMEASURES ATTEMPTED AND FAILED.')
                time.sleep(2)
                print("Wow... that was a close one. You certainly like to play it risky. That key was right in the middle of the defense range. Be glad you weren't caught, and make sure to go higher or lower next time you make your first move.")
            """
            # ABOVE: An alternate jammer condition if I want collapse to be set to multiple variables

            print("\n----------------------------------------------\n")

            if tripwire == False:
                if guess < entry_key:
                    """if guess is lower than the nexus key"""
                    high_keys -= 1
                    if high_keys != 0:
                        print(
                            "LOW NODE ENTRY DETECTED: "
                            + str(high_keys)
                            + " LOW ENTRIES UNTIL SYSTEM LOCK"
                        )
                        time.sleep(0.5)
                        if high_keys == 1:
                            print(
                                "APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE SYSTEM LOCK."
                            )
                        time.sleep(1)
                        print(random.choice(msg.lowermessage))
                        guess_list.append("(LOW)")

                else:
                    """if guess is higher than the nexus key"""
                    low_keys -= 1
                    if low_keys != 0:
                        print(
                            "HIGH NODE ENTRY DETECTED: "
                            + str(low_keys)
                            + " HIGH ENTRIES UNTIL SYSTEM LOCK"
                        )
                        time.sleep(0.5)
                        if low_keys == 1:
                            print(
                                "APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE SYSTEM LOCK."
                            )
                        time.sleep(1)
                        print(random.choice(msg.highermessage))
                        guess_list.append("(HIGH)")

            if tripwire == True:
                """punishment for landing in defense range"""
                high_keys -= 1
                low_keys -= 1
                print("JAMMED: NO NODE INFORMATION POSSIBLE")
                print("LOW NODE GUESSES REDUCED BY 1")
                print("HIGH NODE GUESSES REDUCED BY 1")
                guess_list.append("(JAMMED)")
                tripwire = False

            # Increase the value of chance by 1
            if firstchance == True and chances == 5:
                """disable defense protocol, tripmine"""
                time.sleep(1)
                ascii_jam_offline = pyfiglet.figlet_format(
                    "JAMMER   OFFLINE", font="bubble"
                )
                print(ascii_jam_offline)
                print("\n\n" + random.choice(msg.knockout))
                time.sleep(1)
                print(
                    "The DEFENSE RANGE was covering "
                    + str(barrier_low)
                    + " to "
                    + str(barrier_high)
                    + ".\nYou should safely be able to access this range of nodes now.\nThere is a 50% chance that the NEXUS KEY is contained within this DEFENSE RANGE."
                )

            chances -= 1
            firstchance = False

            if chances == 3:
                """activate sonar"""
                sonar = True
                time.sleep(1)
                print("\n\n" + random.choice(msg.chances3))
                time.sleep(1)
                print(" ")
                ascii_sonar = pyfiglet.figlet_format(
                    "SONAR   ONLINE", font="digital"
                )
                print(ascii_sonar)

                print(
                    "Sonar tells if you are within range of the NEXUS KEY.\nStarting now, it will tell you if your entry is within range of the NEXUS KEY.\nThis range will tighten by 10 NUMBERS each time."
                )

            if chances == 3:
                if sonar == True and (
                    ((guess - 30) <= entry_key <= (guess + 30))
                    and (0 < guess < 101)
                ):
                    time.sleep(1)
                    print(" ")
                    print(ascii_sonar_status)
                    print("NEXUS KEY WITHIN 30 NODES")
                    sonar_list.append("KEY WITHIN 30 NODES OF " + str(guess))
                else:
                    time.sleep(1)
                    print(" ")
                    print(ascii_sonar_status)
                    print("NEXUS KEY FURTHER THAN 30 NODES AWAY")
                    sonar_list.append(
                        "KEY MORE THAN 30 NODES FROM  " + str(guess)
                    )

            if chances == 2:
                if sonar == True and (
                    ((guess - 20) <= entry_key <= (guess + 20))
                    and (0 < guess < 101)
                ):
                    time.sleep(1)
                    print(" ")
                    print(ascii_sonar_status)
                    print("NEXUS KEY WITHIN 20 NODES")
                    sonar_list.append("KEY WITHIN 20 NODES OF " + str(guess))
                else:
                    time.sleep(1)
                    print(" ")
                    print(ascii_sonar_status)
                    print("NEXUS KEY FURTHER THAN 20 NODES AWAY")
                    sonar_list.append(
                        "KEY MORE THAN 20 NODES FROM " + str(guess)
                    )

            if chances == 2:
                if low_keys != 0 and high_keys != 0:
                    time.sleep(1)
                    print(
                        "\n\nI just confirmed where the NEXUS KEY is situated."
                    )
                    time.sleep(1)
                    if barrier_inside == 2:
                        print("It's inside the defense range!")
                    if barrier_inside == 1:
                        print("It's outside the defense range!")

            if chances == 1:
                if low_keys != 0 and high_keys != 0:
                    print(
                        "\nFINAL NODE ENTRY REACHED. LOCKING SYSTEM UPON NEXT FAILURE TO LOCATE NEXUS KEY.\n"
                    )
                    if sonar == True and (
                        ((guess - 10) <= entry_key <= (guess + 10))
                        and (0 < guess < 101)
                    ):
                        sonar10 = True
                        time.sleep(1)
                        print(" ")
                        print(ascii_sonar_status)
                        print("NEXUS KEY WITHIN 10 NODES")
                        sonar_list.append(
                            "KEY WITHIN 10 NODES OF " + str(guess)
                        )
                    else:
                        time.sleep(1)
                        print(" ")
                        print(ascii_sonar_status)
                        print("NEXUS KEY FURTHER THAN 10 NODES AWAY")
                        sonar_list.append(
                            "KEY MORE THAN 10 NODES FROM " + str(guess)
                        )

            if high_keys == 0 or low_keys == 0:
                chances = 0

            if chances > 0:
                print(
                    "\n----------------------------------------------\nENTER A NODE (between 1 and 100):\n"
                )

    # Check whether the user
    # guessed the correct number
    if extra_chance == True:
        if chances == 0 and ((guess - 2) <= entry_key <= (guess + 2)):
            print(
                "The system is falling apart... but it seems like you're so close to the NEXUS KEY that the system is hesitating to kick you out-- It must not want to delete the NEXUS KEY's node by accident.\nIt looks like we have time for one more chance!"
            )
            print("SYSTEM LOCK DELAYED. RECALIBRATING...")
            time.sleep(1)
            print(ascii_sonar_status)
            print("NEXUS KEY WITHIN 2 NODES")
            sonar_list.append("KEY WITHIN 2 NODES OF " + str(guess))
            time.sleep(1)
            print("Let's finish this...")
            print(
                "----------------------------------------------\nENTER A NODE (between 1 and 100):\n"
            )
            make_guess()
            if guess == entry_key:
                print("NEXUS KEY LOCATED.")
                time.sleep(2)
                print("EXTRACTING DATA")
                time.sleep(1)
                ascii_win = pyfiglet.figlet_format("KEY ACQUIRED")
                print(ascii_win)
                time.sleep(5)
                print("Excellent job.")
                time.sleep(2)
                decode_key()

            extra_chance = False

    if chances == 0:
        """kill the game if guesses run out"""
        if high_keys == 0:
            print("LOCKING SYSTEM: LOW ENTRY OVERLOAD")
        if low_keys == 0:
            print("LOCKING SYSTEM: HIGH ENTRY OVERLOAD")
        if chances == 0:
            print("MAXIMUM NODE ENTRIES REACHED")
        print("\n\n Denying Nexus entry.\n\nRELEASING KEY CODE: ", entry_key)
        time.sleep(6)
        ascii_locked = pyfiglet.figlet_format("SYSTEMS LOCKED")
        print(ascii_locked)
        print("THANK YOU FOR VISITING.")
        time.sleep(1000)
        sys.exit()


def decode_key():

    digits = 3
    attempts = 10
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
    # print(str(number))
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

    while True:
        print("\nATTEMPT #" + str(counter) + "\n" + "-" * 20 + "\n\n")
        input_crack = input()

        if len(input_crack) != digits:
            time.sleep(1)
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
            print("NO ACCESS TOKENS DETECTED")
        else:
            print(" ".join(clues))

        counter += 1

        if counter == 4:
            ascii_fw_online = pyfiglet.figlet_format(
                "FIREWALL   ONLINE", font="bubble"
            )
            print(ascii_fw_online)
            print("The system has found out we're in the Nexus Key's node.")
            time.sleep(1)
            print(
                "From here on out, you're going to have to bypass FIREWALL CHECKS."
            )
            time.sleep(1)
            print(
                'When the system tells you to "RESPOND", you need to press the "ENTER" key as quickly as possible.\nIf you are too slow, the system is going to LOCK THE SYSTEM before we can decode the Nexus Key.\n\nThe firewall will get MORE DIFFICULT TO BYPASS as time goes on.'
            )
        if counter == 5 or counter == 6:
            key_monitor = True
            print("FIREWALL CHECK ENGAGED: EASY (.5 SECOND RESPONSE)")
            time.sleep(4)
            print("PREPARE TO RESPOND")
            time.sleep(3)
            print("<<<TEST BEGINNING SOON>>>")
            time.sleep(random.randint(2, 5))
            ascii_respond = pyfiglet.figlet_format("RESPOND")
            print(ascii_respond)
            tic = time.perf_counter()
            a = input()
            toc = time.perf_counter()
            cheat_check = input(
                "RESPONSE RECORDED.\nTYPE 'submit' AND PRESS 'ENTER' TO COMMIT YOUR RESPONSE\n\n"
            )
            timeSpent = toc - tic
            if timeSpent > 0.5 or "submit" not in cheat_check.lower():
                time.sleep(2)
                if "submit" not in cheat_check:
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
                print(ascii_locked)
                print("THANK YOU FOR VISITING.")
                time.sleep(1000)
                sys.exit()
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
            time.sleep(4)
            print("PREPARE TO RESPOND")
            time.sleep(3)
            print("<<<TEST BEGINNING SOON>>>")
            time.sleep(random.randint(2, 5))
            ascii_respond = pyfiglet.figlet_format("RESPOND")
            print(ascii_respond)
            tic = time.perf_counter()
            a = input()
            toc = time.perf_counter()
            cheat_check = input(
                "RESPONSE RECORDED.\nTYPE 'submit' AND PRESS 'ENTER' TO COMMIT YOUR RESPONSE\n\n"
            )
            timeSpent = toc - tic
            if timeSpent > 0.4 or "submit" not in cheat_check.lower():
                time.sleep(2)
                if "submit" not in cheat_check:
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
                print(ascii_locked)
                print("THANK YOU FOR VISITING.")
                time.sleep(1000)
                sys.exit()
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
            time.sleep(4)
            print("PREPARE TO RESPOND")
            time.sleep(3)
            print("<<<TEST BEGINNING SOON>>>")
            time.sleep(random.randint(2, 5))
            ascii_respond = pyfiglet.figlet_format("RESPOND")
            print(ascii_respond)
            tic = time.perf_counter()
            a = input()
            toc = time.perf_counter()
            cheat_check = input(
                "RESPONSE RECORDED.\nTYPE 'submit' AND PRESS 'ENTER' TO COMMIT YOUR RESPONSE\n\n"
            )
            timeSpent = toc - tic
            if timeSpent > 0.35 or "submit" not in cheat_check.lower():
                time.sleep(2)
                if "submit" not in cheat_check:
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
                print(ascii_locked)
                print("THANK YOU FOR VISITING.")
                time.sleep(1000)
                sys.exit()
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
            time.sleep(4)
            print("PREPARE TO RESPOND")
            time.sleep(3)
            print("<<<TEST BEGINNING SOON>>>")
            time.sleep(random.randint(2, 5))
            ascii_respond = pyfiglet.figlet_format("RESPOND")
            print(ascii_respond)
            tic = time.perf_counter()
            a = input()
            toc = time.perf_counter()
            cheat_check = input(
                "RESPONSE RECORDED.\nTYPE 'submit' AND PRESS 'ENTER' TO COMMIT YOUR RESPONSE\n\n"
            )
            timeSpent = toc - tic
            if timeSpent > 0.30 or "submit" not in cheat_check.lower():
                time.sleep(2)
                if "submit" not in cheat_check:
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
                print("THANK YOU FOR VISITING.")
                time.sleep(1000)
                sys.exit()
            if timeSpent < 0.30 and "submit" in cheat_check.lower():
                time.sleep(2)
                print(
                    "RESPONSE TIME SATISFACTORY. ("
                    + str(timeSpent)
                    + ") \nYOU MAY PROCEED"
                )

        if input_crack == number:
            print("Wait a second...")
            time.sleep(1)
            print("The NEXUS KEY is decrypting!")
            time.sleep(2)
            ascii_win = pyfiglet.figlet_format("KEY DECODED: YOU WIN")
            print(ascii_win)
            time.sleep(2)
            print("Welcome... to the Nexus.")
            print("CONGRATULATIONS")
            time.sleep(5)

            def success_asciimatic(screen):
                """victory screen via asciimatics"""
                while True:
                    screen.print_at(
                        "Welcome to the NEXUS",
                        randint(0, screen.width),
                        randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1),
                    )
                    ev = screen.get_key()
                    if ev in (ord("Q"), ord("q")):
                        return
                    screen.refresh()

            Screen.wrapper(success_asciimatic)
            sys.exit()

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
            time.sleep(1000)
            sys.exit()
            break


minigame_hack()
