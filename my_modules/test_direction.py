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


going = True
number_turns = 1
while going == True:
    chosen_direction = randint(1,4)
    if chosen_direction == 1:
        direction = 'NORTH'
    elif chosen_direction ==2:
        direction = 'EAST'
    elif chosen_direction ==3:
        direction = 'SOUTH'
    elif chosen_direction == 4:
        direction = 'WEST' 
    else:
        pass

    print('\nDATA PACKET ({})\n'.format(number_turns))
    print('--ORIENTED {}--'.format(direction))
    deplete = number_turns # lower number as we go
    turn_list = []
    while deplete>0:
        if number_turns <4:
            turn = randint(0,1)
        if number_turns >3:
            turn = randint(0,2)
        if turn ==0:
            turn_list.append('LEFT')
            chosen_direction-=1
            if chosen_direction ==0:
                chosen_direction = 4 # reset to west

        elif turn ==1:
            turn_list.append('RIGHT')
            chosen_direction+=1
            if chosen_direction ==5:
                chosen_direction = 1 #reset to north
        else:
            turn_list.append('REVERSED')
            chosen_direction+=2
            if chosen_direction ==5:
                chosen_direction = 1
            if chosen_direction ==6:
                chosen_direction = 2

        deplete -=1
    if chosen_direction == 1:
            direction = 'NORTH'
    elif chosen_direction ==2:
        direction = 'EAST'
    elif chosen_direction ==3:
        direction = 'SOUTH'
    elif chosen_direction == 4:
        direction = 'WEST' 
    else:
        pass
    print('LOG: {}'.format(turn_list))
    where_am_i = input('PACKET TRAJECTORY: ')
    if where_am_i == direction:
        print('correct')
    else:
        print('incorrect: IT IS {}'.format(direction))
    number_turns+=1