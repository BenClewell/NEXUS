import time
import random
import sys
import pyfiglet

import message_random as msg

# NEXUS CHAPTER 1:
'''
1) Don't enter in this code
2) Binary  code cypher (5 digits)
3) 'Hello' upside down riddle (5 digits)
4) 'Each ear plays different codes' riddle
5) ''

minigame:

tight security: tell player if they're within 30, 20, 10 units of the key.
medium security: tell player if
'''
ascii_nexus = pyfiglet.figlet_format("THE    NEXUS")
print(ascii_nexus)





barrier_low = random.randint(25,50)
barrier_high = random.randint(50,75)
# sets the low and high defense paramters
barrier_inside = random.randint(1,2)
#sets 50-50 chance for whether number is in thres or outside
if barrier_inside == 2:
    entry_key = random.randint(barrier_low,barrier_high)
    #between the two barrier params
if barrier_inside == 1:
    #outside the two barrier params
    low_high = random.randint(1,2)
    #if outside, is it lower or higher?
    if low_high == 1:
        entry_key = random.randint(1,barrier_low)
        #it's lower, between one and the low thres
    if low_high == 2:
        entry_key = random.randint(barrier_high,100)
        #it's higher, between one and the high thres

# view entry key, and the two defense ranges by enabling below
# print(str(entry_key) + " " + str(barrier_low) + " " + str(barrier_high))






# chances are 5 or 3
chance_options = [5]
chances = random.choice(chance_options)
firstchance= True
collapse = random.randint(1,3)
guess_list = []

low_keys = 3
high_keys = 3


time.sleep(1)
print("The NEXUS KEY is encrypted between node 1 and 100.")
print("Type in any number in this range, and I'll hack that node to look for the NEXUS KEY.")


time.sleep(1)
print('\nDEFENSE RANGE ESTABLISHED.\n33% CHANCE OF TRIPWIRE COUNTERMEASURES IF DEFENSE RANGE IS SELECTED DURING YOUR FIRST HACK.')



if chances == 5:
    sonar = False
    time.sleep(1)
    print (
        random.choice(msg.chances5)
        )
    print('I would choose either a low node, or a high node to start with.')






    print('\nWe have a maximum of 5 chances to locate the key. We can do this.')
    print('You can select a node on either side of the NEXUS KEY only 3 times before the AI finds you, so be careful.\n(Do not be consistently high or low.)')

    time.sleep(.5)
    print("\n\nTo view your hacking history in this system, enter '0' at any point.")
    time.sleep(.5)


    print("----------------------------------------------\nENTER A NODE (between 1 and 100):\n")


def choose_node():
    while chances != 0:
        guess = int(input())
        if guess !=0:
            guess_list.append(guess)
        # Compare the user entered number
        # with the number to be guessed
        if guess == 0:
            helpmenu = True
            status_splash = True
            while helpmenu == True:
                while status_splash == True:
                    time.sleep(1)
                    print('\nBOOTING MAINFRAME INFORMATION')
                    time.sleep(1)
                    print('--------------------------')
                    time.sleep(1)
                    print('--------------------------'*2)
                    time.sleep(1)
                    print('--------------------------'*3)

                    print('\nEntry Information:')
                    if guess_list == []:
                        print('NO ENTRIES COMMITTED YET')
                    if guess_list != []:
                        print('ENTRIES SO FAR: ' + str(guess_list))
                    print('MAXIMUM ENTRIES REMAINING UNTIL COUNTERMEASURES: ' + str(chances))
                    print('LOW ENTRIES REMAINING: ' + str(high_keys))
                    print('HIGH ENTRIES REMAINING: ' + str(low_keys))

                    print('\nTripwire Information:')
                    if firstchance == True:
                        print('DEFENSE RANGE UNKNOWN. PROCEED WITH CAUTION.')
                    if firstchance == False:
                        print('DEFENSE RANGE: ' + str(barrier_low) + ' to ' + str(barrier_high))

                    print('\nSonar Information:')
                    if sonar == False:
                        print('SONAR OFFLINE')
                    if sonar == True:
                        print('SONAR ONLINE')
                        if chances == 3:
                            print('ACCURACY: 30 NUMBER RANGE')
                        if chances == 2:
                            print('ACCURACY: 20 NUMBER RANGE')
                        if chances == 1:
                            print('ACCURACY: 10 NUMBER RANGE')

                    time.sleep(2)
                    print('\nReturning to hacking interface...')
                    time.sleep(1)
                    print("\n----------------------------------------------\nENTER A KEY (between 1 and 100):\n")

                    status_splash = False
                    helpmenu = False


                ''' ALTERNATIVE MENU OPTIONS FOR LATER 
                menu_choice = input('\n*********************************************\nI know a lot about these systems. Enter any of the following words to learn more...\n\nTRIPMINE, SONAR or COUNTERMEASURES\n\nOtherwise, type EXIT to resume hacking.\n\nResponse: ')
                if 'exit' in menu_choice.lower():
                    time.sleep(1)
                    print("I'll be here if you need me. Just enter in 0 as your key at any time.")
                    time.sleep(.5)
                    helpmenu=False
                    print("\n----------------------------------------------\nENTER A KEY (between 1 and 100):\n")

                elif 'tripmine' in menu_choice.lower():
                    print('Check this out:')
                    time.sleep(1)
                    print('DATAFILE//\n TRIPMINE: IF WITHIN THE GUARDED RANGE,  FIRST KEvY ENTRY HAS A 33% CHANCE OF TRIGGERING AI COUNTERMEASURES\n\n GUARDED RANGE MUST AVOID SYSTEM EXTREMES.')

                    time.sleep(1)
                    print("I would suggest always picking a number near the far-top or far-bottom of the range to start with, since the AI almost always leaves the extremes alone.\nWhen choosing the NEXUS KEY, the system's AI always has a 50/50 chance of placing the key inside of the GUARDED RANGE. Once you find out what that range is, this can inform where you want to focus your hacking.\n\nAlso, it's worth noting that while the guarded range is scary, it only has a 1/3 chance of getting you during a trespass.")
                else:
                    time.sleep(1)
                    print("\nI'm not sure what you meant... let's try this again...\n")'''
        else:


            if guess == entry_key:

                # if number entered by user
                # is same as the generated
                # number by randint function then
                # break from loop using loop
                # control statement "break"
                print('NEXUS KEY LOCATED.')
                time.sleep(2)
                print('EXTRACTING DATA')
                time.sleep(1)
                ascii_win = pyfiglet.figlet_format("SUCCESS")
                print(ascii_win) 
                time.sleep(1)
                print("Welcome to the Nexus.")
                time.sleep(10)
                sys.exit()
                first_trial()

            if firstchance == True and chances == 5 and barrier_low<guess<barrier_high and collapse == 2:
                time.sleep(1)
                print('TRIPWIRE ACTIVATED\n\nENTRY DETECTED IN DEFENSE RANGE: ' + str(barrier_low) + ' TO ' + str(barrier_high) + ". ENGAGING CONTERMEASURES.\n\n Denying Nexus entry.\n\nRELEASING KEY CODE: ", entry_key)
                time.sleep(6)
                print('COUNTERMEASURES PREVENT HACKERS LIKE YOU FROM ENTERING THE NEXUS. PRAISE COUNTERMEASURES.')
                time.sleep(4)
                sys.exit()
            if firstchance == True and chances == 5 and barrier_low<=guess<=barrier_high and collapse != 2:
                time.sleep(1)
                print('SYSTEM MALFUNCTION: TRIPWIRE COUNTERMEASURES ATTEMPTED AND FAILED.')
                time.sleep(2)
                print("Wow... that was a close one. You certainly like to play it risky. That key was right in the middle of the defense range. Be glad you weren't caught, and make sure to go higher or lower next time you make your first move.")

            print("\n----------------------------------------------\n")

            if guess < entry_key:
                high_keys -=1
                if high_keys!=0:
                    print('LOW NODE ENTRY DETECTED: ' + str(high_keys) + ' LOW ENTRIES UNTIL COUNTERMEASURES')
                    time.sleep(.5)
                    if high_keys == 1:
                        print('APPROACHING LOW NODE OVERLOAD. ONE MORE LOW NODE WILL ENGAGE COUNTERMEASURES.')
                    time.sleep(1)
                    print (random.choice(msg.lowermessage))
                    guess_list.append('(LOW)')


            else:
                low_keys -=1
                if low_keys!=0:
                    print('HIGH NODE ENTRY DETECTED: ' + str(low_keys) + ' HIGH ENTRIES UNTIL COUNTERMEASURES')
                    time.sleep(.5)
                    if low_keys == 1:
                        print('APPROACHING HIGH NODE OVERLOAD. ONE MORE HIGH NODE WILL ENGAGE COUNTERMEASURES.')
                    time.sleep(1)
                    print (random.choice(msg.highermessage))
                    guess_list.append('(HIGH)')






            # Increase the value of chance by 1
            if firstchance == True and chances == 5:
                '''disable defense protocol, tripmine'''
                time.sleep(1)
                print("\n\n" + random.choice(msg.knockout))
                time.sleep(1)
                print('The DEFENSE RANGE was covering ' + str(barrier_low) + " to " + str(barrier_high) + ".\nIf you want, you should safely be able to access this range of nodes now.\nThere is a 50% chance that the NEXUS KEY is contained in this DEFENSE RANGE, and a 50% chance that it's contained outside this range. Use this information wisely.")



            chances -= 1
            firstchance = False

            if chances == 3:
                '''activate sonar'''
                sonar= True
                time.sleep(1)
                print ("\n\n" +
                    random.choice(msg.chances3)
                    )
                time.sleep(1)
                print('\nSONAR ONLINE\n')
                time.sleep(.5)
                print('Sonar tells if you are within range of the NEXUS KEY.\nStarting now, it will tell you if your entry is within range of the NEXUS KEY.\nThis range will tighten by 10 NUMBERS each time.')


            if chances ==3:
                if sonar ==True and (
                    ((guess-30)<=entry_key<=(guess+30)) and (0<guess<101)
                    ):
                    time.sleep(1)
                    print('\nSONAR: NEXUS KEY WITHIN 30 NODES')
                else:
                    time.sleep(1)
                    print('\nSONAR: NEXUS KEY FURTHER THAN 30 NODES AWAY')



            if chances == 2:
                if sonar ==True and (
                    ((guess-20)<=entry_key<=(guess+20)) and (0<guess<101)
                    ):
                    time.sleep(1)
                    print('\nSONAR: NEXUS KEY WITHIN 20 NODES')
                else:
                    time.sleep(1)
                    print('\nSONAR: NEXUS KEY FURTHER THAN 20 NODES AWAY')


            if chances ==1:
                if low_keys!=0 and high_keys!=0:
                    print('\nFINAL NODE ENTRY REACHED. ENGAGING COUNTERMEASURES UPON FAILURE TO LOCATE NEXUS KEY.\n')
                    if sonar ==True and (
                        ((guess-10)<=entry_key<=(guess+10)) and (0<guess<101)
                        ):
                        sonar10 = True
                        time.sleep(1)
                        print('\nSONAR: NEXUS KEY WITHIN 10 NODES')
                    else:
                        time.sleep(1)
                        print('\nSONAR: NEXUS KEY FURTHER THAN 10 NODES AWAY')

            if chances == 2:
                if low_keys!=0 and high_keys!=0:
                    time.sleep(1)
                    print('\n\nI just found out where the NEXUS KEY is situated.')
                    time.sleep(1)
                    if barrier_inside==2:
                        print("It's inside the defense range!")
                    if barrier_inside==1:
                        print("It's outside the defense range!")

            if high_keys ==0 or low_keys ==0:
                chances = 0

            if chances>0:
                print("\n----------------------------------------------\nENTER A NODE (between 1 and 100):\n")



    # Check whether the user
    # guessed the correct number
    if chances == 0:
        '''kill the game if guesses run out'''
        if high_keys ==0:
            print('COUNTERMEASURES: LOW ENTRY OVERLOAD')
        if low_keys ==0:
            print('COUNTERMEASURES: HIGH ENTRY OVERLOAD')
        if chances ==0:
            print('MAXIMUM NODE ENTRIES REACHED')
        print('\n\n Denying Nexus entry.\n\nRELEASING KEY CODE: ', entry_key)
        time.sleep(6)
        print('COUNTERMEASURES PREVENT HACKERS LIKE YOU FROM ENTERING THE NEXUS. PRAISE COUNTERMEASURES. PRAISE THE NEXUS.')
        time.sleep(6)
        sys.exit()


print('I have encountered an error. Please try to re-enter your node')
time.sleep(2)

choose_node()

































def arg_main():
    pass
    kill_switch = str(random.randint(1,10))
    if kill_switch == '2':
        print("FUN FACT: I quit this program 1/10 times you get to a code entry prompt.\n")
        time.sleep(3)
        print("I could choose not to do this, but I do anyway.")
        time.sleep(2)
        print("Goodbye.")
        time.sleep(1)
        sys.exit()


    code = input('Enter your code now:\n\n')
    if code == '1234':
        first_trial()
    else:
        print("That is not a code. Don't play games with me.")
        arg_main()




def first_trial():
    pass


    key1 = input("TRIAL 1a:\nThough my flesh runs warm with fur, I still deposit spheres, life's core. Of my type there stand just five, one of which can swim and dive.\n\nWhat am I?\n\n")

    if 'MONOTREME' in key1.upper():
        print('Correct.')
        monotreme = True
        time.sleep(1)
        number_choice = str(random.randint(1,5))
        key2 = input('Correct. I am now thinking of a number between 1 and 5. What is that number?\n\n')
        if key2 == number_choice:
            print('Lucky. Your new code is 345789.')
            time.sleep(2)
            arg.main()
        else:
            print('Incorrect. I was thinking of ' + number_choice + '. Exiting trial.')
            time.sleep(2)
            arg_main()
    else:
        print('Sorry, that is not right. Exiting trial.\n\n')
        time.sleep(2)
        arg_main()
