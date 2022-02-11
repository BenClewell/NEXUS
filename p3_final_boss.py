import my_modules.sfx as sfx
from pynput import keyboard
import time
import pygame
from pygame import mixer
from alive_progress import alive_bar
import random
import pyfiglet
import pyfiglet.fonts

class P3:
    too_many_presses = False
    threshold = .5
    player_lives = 3
    insertion_finished = False
    damage_value = 0
    success_state = False
    bosshealth = 100
    def multi_stage_nodehack():
        P3.insertion_finished = False
        if P3.bosshealth >90:
            node_progress_speed = random.choice([0.05,0.04])
        elif P3.bosshealth >75:
            node_progress_speed = random.choice([0.05,0.04, 0.03])
        elif P3.bosshealth >50:
            node_progress_speed = random.choice([0.05,0.04, 0.03, 0.025])
        elif P3.bosshealth >25:
            node_progress_speed = random.choice([0.04, 0.035, 0.025])
        else:
            node_progress_speed = random.choice([0.04, 0.03, 0.025])
        #node_progress_speed = random.choice([0.02, 0.03, 0.04, 0.05])
        start_insert = (
            random.choice(
                (
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
        def on_press(key):
            insert_middle = start_insert + 6
            if key == keyboard.Key.enter and P3.node_vulnerable == True:
                sfx.burst_sound()
                P3.node_failed_state = False  # user hacked node successfully
                P3.insertion_finished = True
                time.sleep(.25)
                if P3.entered_node == insert_middle:
                    print("[PERFECT INSERTION (+3 NEXUS CORRUPTION)]")
                    P3.damage_value = 4
                    P3.success_state = True

                elif ((insert_middle + 1) == P3.entered_node) or (
                    (insert_middle - 1) == P3.entered_node
                ):
                    print("[PRECISE INSERTION (+2.5 NEXUS CORRUPTION)]")
                    P3.damage_value = 3
                    P3.success_state = True
                elif ((insert_middle + 2) == P3.entered_node) or (
                    (insert_middle - 2) == P3.entered_node
                ):
                    print("[GOOD INSERTION (+2 NEXUS CORRUPTION)]")
                    P3.damage_value = 2
                    P3.success_state = True
                else:
                    print("[VALID INSERTION (+1 NEXUS CORRUPTION)]")
                    P3.damage_value = 1
                    P3.success_state = True
            if key == keyboard.Key.enter and P3.node_vulnerable == False:
                P3.damage_value = 0
                P3.success_state = False
                sfx.burst_sound()
                P3.node_failed_state = True
                P3.insertion_finished = True
                print("[INVALID TEST RESPONSE (-1 USER INTEGRITY)]")



        """the area in which you can perform a node hack"""
        '''multiple things to hack'''
        sfx.burst_sound()
        print("\n\nNode security level [REDACTED]")
        print("|| DATA LOCUS: {} ||".format(end_insert - 5))
        print(
            "\nPress ENTER between {} and {} to enter node.".format(
                (start_insert + 1), (end_insert)
            )
        )  # +1, to expand range
        time.sleep(.5)
        #sfx.voice_nodehack()
        time.sleep(0)
        sfx.hack_node()
        #
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        sfx.loading_loop()
        with alive_bar(
            total=100,
            length=int(random.choice((25,150))),
            bar="squares",

            spinner="dots_waves2",
            enrich_print=False,
        ) as bar:  # default setting
            for i in range(100):
                if P3.insertion_finished == False:
                    if i in range(start_insert, end_insert):
                        P3.node_vulnerable = True
                    else:
                        P3.node_vulnerable = False
                    time.sleep(node_progress_speed)
                    bar()
                    P3.entered_node = i + 1  # know what node the player entered
        time.sleep(.5)
        pygame.mixer.stop()
        absorb_input = input(
            ""
        )  # pressing enter to hack counts as entering a node, I guess lol
        listener.stop()
        if P3.node_failed_state == True:
            sfx.antivirus_jamfail()

    def multistage_firewall():
        threshold = P3.threshold
        if P3.bosshealth >90:
            threshold -= 0
        elif P3.bosshealth >75:
            threshold -= .1
        elif P3.bosshealth >50:
            threshold -= .15
        elif P3.bosshealth >25:
            threshold -= .2
        else:
            threshold -= .25
        print("FIREWALL CHECK ENGAGED: HARD ({} SECOND RESPONSE)".format(threshold))
        sfx.sonar.play()
        time.sleep(1)
        if P3.too_many_presses == False:
            print("\n\nPREPARE TO RESPOND.")
            #sfx.voice_fw_check()  # more fw checks
        time.sleep(0.5)
        if P3.too_many_presses == False:
            print("<<<TEST BEGINNING SOON>>>")
            time.sleep(random.randint(1, 3))
        if P3.too_many_presses == False:
            ascii_respond = pyfiglet.figlet_format("RESPOND")
            sfx.burst_sound()
            print(ascii_respond)
            tic = time.perf_counter()
            P3.allowed_range = True
            a = input()
            P3.allowed_range = False
            toc = time.perf_counter()
            sfx.gentle_ui()
            timeSpent = toc - tic
            if timeSpent > threshold:
                P3.success_state = False
                print(
                    "RESPONSE TIME TOO SLOW. ("
                    + str(timeSpent)
                    + ") \nLOCKING SYSTEM."
                )
                #
            if timeSpent < threshold:
                P3.success_state = True
                time.sleep(1)
                print(
                    "RESPONSE TIME SATISFACTORY. (+1 NEXUS CORRUPTION)"
                    + str(timeSpent)
                    + ") \nCONTINUING...")
                P3.bosshealth -= 1


    def bossfight():
        '''fight the boss of the nexus'''
        from my_modules.test_modules import intermission_1
        from my_modules.test_modules import intermission_2
        #import sys
        #del sys.modules["my_modules.test_modules.bullethellnaked2"]
        #from my_modules.test_modules import bullethellnaked2 as bullethellnaked3
        def nodehack_portion():
            endpoint = random.choice((2,5))
            for i in range(0,endpoint):
                P3.multi_stage_nodehack()
                if P3.success_state == False:
                    print('it is over: {}'.format(P3.bosshealth))
                    time.sleep(100)
                else:
                    P3.bosshealth = P3.bosshealth - P3.ddamage_value
                    print('\nBOSS HEALTH: {}'.format(P3.bosshealth))
                    if P3.bosshealth <=0:
                        print('You have won.')
                        time.sleep(100)
        def firewall_portion():
            endpoint = random.choice((2,3))
            for i in range(0,endpoint):
                P3.multistage_firewall()
                if P3.success_state == False:
                    print('it is over: {}'.format(P3.bosshealth))
                    time.sleep(100)
                else:
                    P3.bosshealth = P3.bosshealth - P3.damage_value
                    print('\nBOSS HEALTH: {}'.format(P3.bosshealth))
                    if P3.bosshealth <=0:
                        print('You have won.')
                        time.sleep(100)
            print('\nATTACK COMPLETE')
        thing = True
        while thing == True:
            attack_choice = random.choice((1,2))
            if attack_choice == 1:
                # pyfiglet text
                ascii_node_announce = pyfiglet.figlet_format("NODES ACTIVATED")
                print(ascii_node_announce)
                nodehack_portion()
            if attack_choice == 2:
                ascii_firewall_announce = pyfiglet.figlet_format("FIREWALLS ACTIVATED")
                print(ascii_firewall_announce)
                firewall_portion()







P3.bossfight()