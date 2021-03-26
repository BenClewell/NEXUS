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

# ONE LINERS FOR THE ENDING SEQUENCE:
gotta_decrypt = pygame.mixer.Sound("sounds/narration/one_liners/pt2_start.wav")
three_aligned = pygame.mixer.Sound("sounds/narration/one_liners/all_aligned.wav") #start pt3
found_node = pygame.mixer.Sound("sounds/narration/one_liners/pt1_nodefound.wav") #on the nexus node
first_jam = pygame.mixer.Sound("sounds/narration/one_liners/firstjam.wav") #33 percent
first_jam_check = pygame.mixer.Sound("sounds/narration/one_liners/firstjam_check.wav") #more firewall. oh no!
second_jam_start = pygame.mixer.Sound("sounds/narration/one_liners/secondjam_start.wav") #hack again
second_jam_blocked = pygame.mixer.Sound("sounds/narration/one_liners/secondjam_blocked.wav") #stopped at 66!
third_jam_start = pygame.mixer.Sound("sounds/narration/one_liners/thirdjam_start.wav") #hack again
third_jam_blocked = pygame.mixer.Sound("sounds/narration/one_liners/thirdjam_blocked.wav") #stopped at 99!
fourth_jam_final = pygame.mixer.Sound("sounds/narration/one_liners/fourthjam_final.wav") #encourage!
omg_did_it = pygame.mixer.Sound("sounds/narration/one_liners/omg.wav") #encourage!
good_hacker = pygame.mixer.Sound("sounds/narration/one_liners/compliment_player.wav") #amazing job!
welcome_nexus = pygame.mixer.Sound("sounds/narration/one_liners/WELCOME.wav") #WELCOME TO THE NEXUS
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
def voice_introduction():
    """ play at entry screen"""
    sound_number = random.randint(1, 5)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/introductions/intro_" + str(sound_number) + ".wav"
    )
    burst_sound.play()

def voice_nodehack():
    """ play when hacking node"""
    sound_number = random.randint(2, 11)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/node_hacking/nodehack (" + str(sound_number) + ").wav"
    )
    burst_sound.play()
def voice_node_fail():
    """ failed to hack"""
    sound_number = random.randint(2, 9)
    # how many variation s of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/jammer_fail/node_fail (" + str(sound_number) + ").wav"
    )
    burst_sound.play()
def voice_too_high():
    """ high entry"""
    sound_number = random.randint(1, 4)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/too_high/too_high (" + str(sound_number) + ").wav"
    )
    burst_sound.play()
def voice_too_low():
    """ low entry"""
    sound_number = random.randint(1, 4)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/too_low/too_low (" + str(sound_number) + ").wav"
    )
    burst_sound.play()
def voice_warning_high_entries():
    """ one more high entry"""
    sound_number = random.randint(1, 2)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/warnings/warning_high_" + str(sound_number) + ".wav"
    )
    burst_sound.play()
    #
    #
def voice_warning_low_entries():
    """ one more low entry"""
    sound_number = random.randint(1, 2)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/warnings/warning_low_" + str(sound_number) + ".wav"
    )
    burst_sound.play()
    #
    #
def voice_nexus_found():
    """ nexus key acquired"""
    sound_number = random.randint(1, 3)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/key_found/found_" + str(sound_number) + ".wav"
    )
    burst_sound.play()
    #
    #  
def voice_fw_check():
    """ fw check incoming"""
    sound_number = random.randint(1, 8)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/fw_check/fwcheck_-00" + str(sound_number) + ".wav"
    )
    burst_sound.play()
    #
    #  
def voice_alligned():
    """ token aligned"""
    sound_number = random.randint(1, 6)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/alignment/oneliner-00" + str(sound_number) + ".wav"
    )
    burst_sound.play()
    #
    #  
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
    track = "sounds/bgm/bgm_" + str(random.randint(-3, 3)) + ".mp3"
    pygame.mixer.music.stop()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)


def play_p2_bgm():
    track = "sounds/bgm/bgm_" + str(random.randint(4, 6)) + ".mp3"
    pygame.mixer.music.stop()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)