# NEXUS: A Simulated Hacking Experience in Python
![Title Card](demo_resources/ezgif.com-gif-maker.gif)
In NEXUS, you are a professional hacker who is trying to search for the NEXUS KEY, a guarded data packet with information your organization needs.
With countless novel gameplay mechanics that utilize the terminal in creative and exhilarating ways, you'll be facing difficult challenges at the hands of the system's security, which is determined to lock you out of the NEXUS forever.

This has been a very fun personal project for me, and I hope you feel the same heart-pumping excitement that I still feel when I play!



#
## REQUIREMENTS
asciimatics==1.12.0

pywin32==300

alive_progress==1.6.2

pynput==1.7.2

pygame==2.0.0

pyfiglet==0.8.post1

keyboard==0.13.5

soundfile==0.10.3.post1

#

## PART ONE: LOCATING THE NEXUS KEY

CODE: https://github.com/BenClewell/NEXUS/blob/alpha2/my_modules/pt1_combined.py

In the first part of the experience, you are trying to locate a node that contains the **nexus key** (*the game's McGuffin!*)-- but in order to locate that node, you're going to have to use a couple of tools at your disposal. To start off the first part of the game, you're greeted by the soothing voice of the **network assistant**, who provides helpful audio cues and feedback as you conduct your hack on the network. You will be prompted to select a number between ONE and ONE HUNDRED, which dictates your selected node. Once you select your first node, you will start being introduced, round by round-- to new mechanics that will assist you in finding your prize!

Additionally, you will initially receive 2000 DATA, which is used to measure performance and skill in your hacking abilities. 

You will receive and lose data depending on your performance as you go through your playtrhough.

* * * 
###  ROUND ONE
In the first round, you are introduced to an early obstacle: the ANTIVIRUS. For the first two rounds of gameplay, you may only makes entries based on an INSERTION POOL that is provided to you at the start of the game. 

* MECHANIC: ANTIVIRUS
                
        To introduce more variety into the early game, you must adhere to the rules of the antivirus-- which will allow you to enter (2) TWO-DIGIT entries comprised of numbers in the INSERTION POOL. Once one number is consumed, you will only have THREE REMAINING digits for round two, and ONE DIGIT for round three. Mind your consumption carefully.

STRATEGY:

* Every game, a range of numbers, clustered around the center of the 100-number range (the low end will be between 1 and 50, and the high end will be between 51 and 100)-- will be designated as the JAMMER RANGE. Selecting a node within this initially-unknown range will trigger the JAMMER (a minigame that pits you against the system's firewall in order to gain directional intelligence about your hack!), and make hacking the system more challenging for you.
    
    * MECHANIC: JAMMER
            
            There is a 50% chance of the NEXUS KEY spawning within  the JAMMER RANGE. Keep this in mind when evaluating probable locations. Jammer range is revealed after round 3.

            If you select a node within the JAMMER RANGE, you will have to complete several fast tasks to defeat the firewall, which could be one of the following four activities:

            * SYSTEM COMMANDS: Type, in exact words, what the system instructs you to type.
            * CODE CRACKING: Re-alphabetize a scrambled 4-letter key.
            * DDOS: Type the 'I' key an exact, specified number of times.
            * BLOCKCHAIN: Solve basic math problems.

            Every wrong entry is penalized by advancing the firewall forward by an increasing factor.
            
            If you reach the end of the screen before the firewall, you will SUCCEED and find out the directionality of your node entry. Keep in mind that the firewall will now increase in security by ONE UNIT, which means the next time you face the firewall, it will be slightly FASTER.
            
            If the firewall reaches the end of the screen before you, you will FAIL and the directionality of your node entry will not be available to you. However, the firewall will now decrease in security by TWO UNITS, which means the next time you face the firewall, it will be significantly SLOWER.

            'Intermediate Security' is the default speed for the firewall. High security is easier, low security is more difficult.

            You will gain or lose data based on your performance. 


RESULTS:

* You will be faced with a NODE ENTRY CHALLENGE. This is a result of every attempted hack. You are given an insertion range briefing (a ten-digit range of numbers) to press the ENTER KEY within. Shortly thereafter, you will be given a SECURITY LEVEL, which is the speed that the challenge will proceed at. (1 is slowest, 9 is fastest).

* If you either FAIL the NODE ENTRY CHALLENGE, or lose against a JAMMER FIREWALL (if applicable), you will not learn directionality of the **Nexus Key**. However, if you SUCCEED, you will learn whether your entry is **higher** or **lower** than the **Nexus Key**. You will gain or lose DATA based on your performance.

* You will then notice that either your HIGH or LOW chances have been diminished by ONE. If you succeeded at your NODE ENTRY CHALLENGE and any applicable JAMMERS, this will be relative to your directionality to the **Nexus Key**. If you did not find out directionality of the **Key**, you will lose one chance from whichever set of chances you have more of-- and if both chances have equivilent amounts, either a high or a low guess will be randomly lost. 

POINTERS:
* If you enter '0' at any point during a node entry, you will be brought to the HACKER HISTORY screen. This is a useful summary of any hacks you have conducted so far, as well as any information you have discovered about the target node, and any abilities you have activated. 

* You must balance your HIGH and LOW entries appropriately. If you are consistently high, or consistently low, the game can end early before all 5 rounds have been completed. (You can be high 3 times before the game is over, and low 3 times before the game is over.)

* Consider your entry balance when creating your initial two entries from the Antivirus INSERTION POOL.

* * * 
###  ROUND TWO
After your first round, you will notice that you have unlocked SPECIAL SONAR, which is a modification on the more generalized SONAR. Additionally, you will only have two numbers in which to construct your next node entry.  



STRATEGY:
* On top of any directional information you hopefully discovered in ROUND ONE, you must now consider the information that SONAR will give you going forward. 

 * MECHANIC: SONAR

        After you search one node, your ability to use SONAR will be unlocked. SONAR tells you if compared to the node that you just entered, you are within a certain range of the NEXUS KEY. 

        (For example, if I enter "40" as my target node, and the SONAR is set to an accuracy of 30-- it will tell you if the NEXUS KEY is within 30 nodes of 40 -- so, if the key is between 10 and 70.)

        Every time you enter a target node, the sonar's accuracy will narrow by 10. (30, 20, 10 is the order.) However, you may at any time equip your SPECIAL SONAR by entering '101' during target node selection.

        SPECIAL SONAR allows you to specify a custom SONAR ACCURACY, that will replace the normal sonar accuracy for a given turn.

        (For example, if I enter '5' as my SPECIAL SONAR, I will learn if my TARGET NODE is within 5 nodes of the NEXUS KEY.)

        SPECIAL SONAR is disabled if the NEXUS key is outside of the range that you provided. It may be rebooted for DATA when lost. 

RESULTS:
* In addition to directionality, you will now receive a SONAR READING. Sonar will activate whether or not you have failed or succeeded at ascertaining direction of the **Nexus Key**. 

* You will be revealed the upper and lower limits of the **Jammer Range**.

POINTERS:
* It is important to consider when it is worth taking the risk to enable SPECIAL SONAR (By entering '101' as your node to toggle it on and off), and when it is better to go with the default sonar range progression-- which can be seen as a forecast in HACKER HISTORY.

* Remember, there is a 50% chance that the key will spawn the **Jammer Range**. If the range is very narrow or wide, you can make important decisions in focusing your future entries, now knowing concrete limits to the range.


* * * 
###  ROUND THREE
Hopefully by now, you have learned importance intelligence about the general location of the **Nexus Key**. However, you will now gain confirmation as to whether the Key is inside of the Jammer Range, or outside of the Jammer Range.

STRATEGY:
* Continue using directionality and sonar information to narrow down your search, and plan on soon knowing on what side of the JAMMER RANGE the **Nexus Key** is contained within. 

POINTERS: 

* Check your HACKER HISTORY to gain a summary on your work so far. 

* Now is a good time to take advantage of the narrow ranges afforded by SPECIAL SONAR, if you still have the ability to activate it. 

* * * 
###  ROUND FOUR
You now have complete access to all modules and information that you can use to locate the Nexus Key. 

STRATEGY:
* Be very mindful of your HIGH and LOW chances at this point. Although your information bank should be large, you can easily end your run early by failing to balance your node entries. 
* * * 
###  FINAL ROUND
If you have balanced HIGH and LOW ENTRIES up to this point, the assistant will warn you that this is your LAST ATTEMPT. You will have one final opportunity to locate the **Nexus Key** before you are locked out of the system, and the game is over. Additionally, you will be given the option to forfeit DATA in exchange for knowledge on whether the NEXUS NODE is EVEN or ODD. 

MECHANIC: FINAL CHANCE
        
        If you are within 2 NODES of the Nexus Key at any point in which you would normally end your run, you will have ONE FINAL CHANCE to locate the Nexus Key. 

        If FINAL CHANCE is triggered during the final round, you will not be alerted to the DIRECTIONALITY of the Nexus Key. 

        However, if FINAL CHANCE is triggered before the final round, you will be alerted to the DIRECTIONALITY of the Nexus Key.

* * * 
###  LOCATING THE NEXUS NODE
If you have located the Nexus Key's node, you will receive an audio and text cue alerting you to your discovery.

If you succeed at the resultant NODE ENTRY CHALLENGE, you will move to the next chapter of NEXUS.

You MUST succeed the node entry challenge to access the **Nexus Key**.

Good luck!
#
## TRANSITION: DATA BREACH

When you locate the NEXUS KEY, you will be given a short amount of time to gather  DATA. 

Data is transmitted globally USING CARDINAL DIRECTIONS: North, East, South, and West.
The system will provide a LEDGER of where a data packet has moved. You must respond with N, E, S, or W to triangulate each data packet.
RIGHT TURNS move CLOCKWISE around the compass.
LEFT TURNS move COUNTERCLOCKWISE.
Finally, REVERSE MOVEMENTS move you OPPOSITE on the compass.
LOST DATA will SUBTRACT the total value of the FAILED TARGET. (So be careful.)

When the system tracks your position, you will be unable to harvest any more data, and will move onto PART TWO. 

## PART TWO: DECRYPTING THE KEY

CODE: https://github.com/BenClewell/NEXUS/blob/alpha2/my_modules/pt2_code_cracker.py

There are fewer mechanics to consider in Part 2, but it is important to understand how the three main mechanics function. You will have to code-crack along the lines of Mastermind, or more aptly, 'Fermi Pico Bagels'! (Which is directly where this section finds inspiration in core mechanics. )



**CORE GAMEPLAY LOOP**
* You must enter a three-digit code of non-repeating numbers between ZERO and NINE. You will receive text notifications regarding each of your character entries. 'MISALIGNED TOKEN' refers to correct integers in the wrong spot. 'ALIGNED TOKEN' refers to correct integers in the right spot. Additionally, you will have to complete a generally-easy NODE ENTRY CHALLENGE, like in Part 1-- that progressively becomes more difficult.

* After your first entry, a 5-MINUTE TIMER will be activated. Once this timer runs out, your run will end as a loss after the next entry reaches completion.

* You will have access to your HACKER HISTORY (Pressing '0'), which will show current timer conditions and previous entries, as well as their associated clues.

**EARLY GAMPLAY**

* While you will not be facing FIREWALL CHECKS, you will have to deal with the reactivation of the ANTIVIRUS. You will need all integers of your entry to add up to an amount specified by the ANTIVIRUS to proceed forward. Unfortunately, this can make your list of entries more disorganized-- but if you keep your methodology straight, this is no big issue.

**LATER GAMEPLAY**
        
* After THREE ENTRIES, you will have to complete FIREWALL CHECKS after each completed entry. When you see the word 'RESPOND' appear after a randomly-generated wait time, press ENTER as quickly as possible to avoid being locked out of the NEXUS. You will receive a visual and auditory warning prior to the FIREWALL CHECK.
  * Firewall checks will become increasingly challenging over time.  

**TRANSITION: DATA BREACH**

* You will receive a DATA BONUS if the system did not locate you before you decrypted the key, and further bonuses for performing the decryption faster. As in the first part, you will have another opportunity to collect DATA via a data breach event. This opportunity is a temporary condition, and will eventually end before the game's final sequence. 

**ENDGAME**

* Once you have matched your TOKEN ENTRY to the NEXUS KEY, you will enter the final section of the game-- which in my opinion, is super fun! With the game's assistant nervously coaching you through a final decryption, you'll complete a series of subsequent FIREWALL CHECKS until the NEXUS KEY is 100% decrypted, and you've hacked the system!

  * You will then be able to enter your NAME and record your DATA SCORE in the included JSON file, so you can track your hacking proficiency as you revisit the NEXUS again!


# FOOTNOTES
Overall, I look forward to you exploring NEXUS! I've worked hard on coming up with a lot of fun mechanics to the best of my ability. 

I hope you have a great time playing! :) 

