# NEXUS: An Exciting Hacking Adventure!
![Title Card](demo_resources/2021-06-02%2014-38-55.gif)
In NEXUS, you're playing as a professional hacker who is trying to search for the NEXUS KEY, a data packet that contains all the information you need to gain access to the network you're trying to infiltrate. 

In a blend between longer-term decision making, and short-term problem solving and reaction measurement, you'll be facing  all manner of challenges at the hands of the system's security, which is determined to lock you out of the NEXUS forever.

This has been a very fun personal project for me, without too much focus on polish and finesse. Just pure, exploratory fun! :)



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

In the first part of the experience, you are trying to locate a node that contains the **nexus key** (*the game's McGuffin!*)-- but in order to locate that node, you're going to have to use a couple of tools at your disposal. To start off the first part of the game, you're greeted by the soothing voice of the **network assistant**, who provides helpful audio cues and feedback as you conduct your hack on the network. You will be prompted to select a number between ONE and ONE HUNDRED, which dictates your selected node. Once you select your first node, you will start being introduced, round by round-- to new mechanics that will assist you in finding your prize!

* * * 
###  ROUND ONE
In the first round, you will have no information available to you. You must simply select a node (between 1 and 100) to begin your first hack.

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


RESULTS:

* You will be faced with a NODE ENTRY CHALLENGE. This is a result of every attempted hack. You are given an insertion range briefing (a ten-digit range of numbers) to press the ENTER KEY within. Shortly thereafter, you will be given a SECURITY LEVEL, which is the speed that the challenge will proceed at. (1 is slowest, 9 is fastest).

* If you either FAIL the NODE ENTRY CHALLENGE, or lose against a JAMMER FIREWALL (if applicable), you will not learn directionality of the **Nexus Key**. However, if you SUCCEED, you will learn whether your entry is **higher** or **lower** than the **Nexus Key**.

* You will then notice that either your HIGH or LOW chances have been diminished by ONE. If you succeeded at your NODE ENTRY CHALLENGE and any applicable JAMMERS, this will be relative to your directionality to the **Nexus Key**. If you did not find out directionality of the **Key**, you will lose one chance from whichever set of chances you have more of-- and if both chances have equivilent amounts, either a high or a low guess will be randomly lost. 

POINTERS:
* If you enter '0' at any point during a node entry, you will be brought to the HACKER HISTORY screen. This is a useful summary of any hacks you have conducted so far, as well as any information you have discovered about the target node, and any abilities you have activated. 

* You must balance your HIGH and LOW entries appropriately. If you are consistently high, or consistently low, the game can end early before all 5 rounds have been completed. (You can be high 3 times before the game is over, and low 3 times before the game is over.)

* * * 
###  ROUND TWO
After your first round, you will notice that you have unlocked SPECIAL SONAR, which is a modification on the more generalized SONAR. 



STRATEGY:
* On top of any directional information you hopefully discovered in ROUND ONE, you must now consider the information that SONAR will give you going forward. 

 * MECHANIC: SONAR

        After you search one node, your ability to use SONAR will be unlocked. SONAR tells you if compared to the node that you just entered, you are within a certain range of the NEXUS KEY. 

        (For example, if I enter "40" as my target node, and the SONAR is set to an accuracy of 30-- it will tell you if the NEXUS KEY is within 30 nodes of 40 -- so, if the key is between 10 and 70.)

        Every time you enter a target node, the sonar's accuracy will narrow by 10. (30, 20, 10 is the order.) However, you may at any time equip your SPECIAL SONAR by entering '101' during target node selection.

        SPECIAL SONAR allows you to specify a custom SONAR ACCURACY, that will replace the normal sonar accuracy for a given turn.

        (For example, if I enter '5' as my SPECIAL SONAR, I will learn if my TARGET NODE is within 5 nodes of the NEXUS KEY.)

        SPECIAL SONAR is disabled  for the rest of the game if the NEXUS key is outside of the range that you provided. 

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
If you have balanced HIGH and LOW ENTRIES up to this point, the assistant will warn you that this is your LAST ATTEMPT. You will have one final opportunity to locate the **Nexus Key** before you are locked out of the system, and the game is over. 

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
