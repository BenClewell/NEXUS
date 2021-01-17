from os import environ

environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
from pygame import mixer
import time
import random

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.init()


def play_mp3(track):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("sounds/" + track)
    pygame.mixer.music.play(-1)
def play_mp3_once(track):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("sounds/" + track)
    pygame.mixer.music.play(1)

click = pygame.mixer.Sound("sounds/audio_16_bit/PM_FSSF_UI_CLICKS_1.wav")
rumble = pygame.mixer.Sound(
    "sounds/audio_16_bit/PM_FSSF_AMBIENCE_SOUNDSCAPE_LOOP_2.wav"
)

startup = pygame.mixer.Sound("sounds/audio_16_bit/PM_CSPH_Loading_9.wav")

bad_sound_hack = pygame.mixer.Sound("sounds/bad_sounds/bad_sound.wav")

sonar = pygame.mixer.Sound("sounds/alarms/sonar.wav")

# for part 2...
enable_firewall = pygame.mixer.Sound("sounds/appear_blips/enable.wav")


def hack_node():
    """ access all calculation sounds, and pick one randomly using random module"""
    calc_sound_number = random.randint(1, 21)
    # how many variations of calc_sounds that there are
    node_sound = pygame.mixer.Sound(
        "sounds/audio_16_bit/PM_CSPH_Calculations_"
        + str(calc_sound_number)
        + ".wav"
    )
    node_sound.play()


def burst_sound():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 10)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/burst_noise/PM_AG_"
        + str(sound_number)
        + "_1_ABSTRACT_GUNS.wav"
    )
    burst_sound.play()


def gentle_ui():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 20)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/gentle_ui_sounds/gentle_ui (" + str(sound_number) + ").wav"
    )
    burst_sound.play()

def gentle_lofi():
    """ pick one of eight lofi gentle sounds """
    sound_number = random.randint(1, 8)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/gentle_ui_sounds/lofi_gentle (" + str(sound_number) + ").wav"
    )
    burst_sound.play()


def fail_corrupt():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 4)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/hack_sounds/fail (" + str(sound_number) + ").wav"
    )
    burst_sound.play()


def success():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 3)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/hack_sounds/win (" + str(sound_number) + ").wav"
    )
    burst_sound.play()


def alarm_loop(alarm_type):
    """global variable to stop looping"""
    """ pick one of 5 cyberphere alarms"""
    alarm_sound = pygame.mixer.Sound(
        "sounds/alarms/PM_CSPH_Alarms_" + str(alarm_type) + ".wav"
    )
    alarm_sound.play(-1)
#
#
def loading_loop():
    """for loading bars in-game"""
    sound_number = random.randint(1, 28)
    alarm_sound = pygame.mixer.Sound(
        "sounds/bar_loops/bar_loop (" + str(sound_number) + ").wav"
    )
    alarm_sound.play(-1)

def appear_blip():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 10)
    # how many variations of burst_sounds that there are
    appear_sound = pygame.mixer.Sound(
        "sounds/appear_blips/appear_blip_" + str(sound_number) + ".wav"
    )
    appear_sound.play()

    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 10)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/burst_noise/PM_AG_"
        + str(sound_number)
        + "_1_ABSTRACT_GUNS.wav"
    )
    burst_sound.play()


def play_p1_bgm():
    track = "sounds/bgm/bgm_" + str(random.randint(0, 3)) + ".mp3"
    pygame.mixer.music.stop()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)


def play_p2_bgm():
    track = "sounds/bgm/bgm_" + str(random.randint(4, 5)) + ".mp3"
    pygame.mixer.music.stop()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)