import random
from random import sample, shuffle, choice
from random import randint

import pyfiglet
import pyfiglet.fonts

import time


from my_modules import title_screen


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
    print(number)

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
            time.sleep(1000)
            sys.exit()
            break
