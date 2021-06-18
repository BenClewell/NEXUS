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

affirm_sound = pygame.mixer.Sound("sounds/affirms/affirm_1.wav")
affirm_sound.set_volume(.6)
# for part 2...
enable_firewall = pygame.mixer.Sound("sounds/appear_blips/enable.wav")

# ONE LINERS FOR THE ENDING SEQUENCE:
gotta_decrypt = pygame.mixer.Sound("sounds/narration/one_liners/pt2_start.wav")
three_aligned = pygame.mixer.Sound(
    "sounds/narration/one_liners/all_aligned.wav"
)  # start pt3
found_node = pygame.mixer.Sound(
    "sounds/narration/one_liners/pt1_nodefound.wav"
)  # on the nexus node
first_jam = pygame.mixer.Sound("sounds/narration/one_liners/firstjam.wav")  # 33 percent
first_jam_check = pygame.mixer.Sound(
    "sounds/narration/one_liners/firstjam_check.wav"
)  # more firewall. oh no!
second_jam_start = pygame.mixer.Sound(
    "sounds/narration/one_liners/secondjam_start.wav"
)  # hack again
second_jam_blocked = pygame.mixer.Sound(
    "sounds/narration/one_liners/secondjam_blocked.wav"
)  # stopped at 66!
third_jam_start = pygame.mixer.Sound(
    "sounds/narration/one_liners/thirdjam_start.wav"
)  # hack again
third_jam_blocked = pygame.mixer.Sound(
    "sounds/narration/one_liners/thirdjam_blocked.wav"
)  # stopped at 99!
fourth_jam_final = pygame.mixer.Sound(
    "sounds/narration/one_liners/fourthjam_final.wav"
)  # encourage!
omg_did_it = pygame.mixer.Sound("sounds/narration/one_liners/omg.wav")  # encourage!
good_hacker = pygame.mixer.Sound(
    "sounds/narration/one_liners/compliment_player.wav"
)  # amazing job!
welcome_nexus = pygame.mixer.Sound(
    "sounds/narration/one_liners/WELCOME.wav"
)  # WELCOME TO THE NEXUS


def hack_node():
    """ access all calculation sounds, and pick one randomly using random module"""
    calc_sound_number = random.randint(1, 21)
    # how many variations of calc_sounds that there are
    node_sound = pygame.mixer.Sound(
        "sounds/audio_16_bit/PM_CSPH_Calculations_" + str(calc_sound_number) + ".wav"
    )
    node_sound.play()


def burst_sound():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 10)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/burst_noise/PM_AG_" + str(sound_number) + "_1_ABSTRACT_GUNS.wav"
    )
    burst_sound.set_volume(.4)
    burst_sound.play()


def gentle_ui():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 20)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/gentle_ui_sounds/gentle_ui (" + str(sound_number) + ").wav"
    )
    burst_sound.set_volume(.7)
    burst_sound.play()


def gentle_lofi(noise= 'none'):
    """ pick one of eight lofi gentle sounds """
    sound_number = random.randint(1, 8)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/gentle_ui_sounds/lofi_gentle (" + str(sound_number) + ").wav"
    )
    if noise == 'Quiet':
        burst_sound.set_volume(.2)
    burst_sound.set_volume(.7)
    burst_sound.play()


def fail_corrupt():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 4)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/hack_sounds/fail (" + str(sound_number) + ").wav"
    )
    burst_sound.set_volume(.35)
    burst_sound.play()


def voice_introduction():
    sound_number = random.randint(1, 21)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/narration/introductions/intro-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/narration/introductions/intro-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(.6)
    burst_sound.play()


def voice_nodehack():
    """ play when hacking node"""
    sound_number = random.randint(2, 11)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/node_hacking/nodehack (" + str(sound_number) + ").wav"
    )
    burst_sound.set_volume(.6)
    burst_sound.play()


def voice_node_fail():
    """ failed to hack"""
    sound_number = random.randint(2, 9)
    # how many variation s of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/jammer_fail/node_fail (" + str(sound_number) + ").wav"
    )
    burst_sound.set_volume(.6)
    burst_sound.play()


def voice_too_high():
    """ high entry"""
    sound_number = random.randint(1, 4)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/too_high/too_high (" + str(sound_number) + ").wav"
    )
    burst_sound.set_volume(.6)
    burst_sound.play()


def voice_too_low():
    """ low entry"""
    sound_number = random.randint(1, 4)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/too_low/too_low (" + str(sound_number) + ").wav"
    )
    burst_sound.set_volume(.6)
    burst_sound.play()


def voice_warning_high_entries():
    """ one more high entry"""
    sound_number = random.randint(1, 2)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/warnings/warning_high_" + str(sound_number) + ".wav"
    )
    burst_sound.set_volume(.6)
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
    burst_sound.set_volume(.6)
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
    burst_sound.set_volume(.6)
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
    burst_sound.set_volume(.7)
    burst_sound.play()
    #


def voice_found_data():
    """ token aligned"""
    sound_number = random.randint(1, 9)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/data_found/found_data-00" + str(sound_number) + ".wav"
    )
    burst_sound.play()
    #


def voice_done_data():
    """ token aligned"""
    sound_number = random.randint(1, 8)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/narration/data_done/done_data-00" + str(sound_number) + ".wav"
    )
    burst_sound.play()


def success():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 3)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/hack_sounds/win (" + str(sound_number) + ").wav"
    )
    burst_sound.set_volume(.6)
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
    alarm_sound.set_volume(.5)
    alarm_sound.play(-1)


def data_loop():
    """for loading bars in-game"""
    alarm_sound = pygame.mixer.Sound("sounds/bar_loops/intercept.wav")
    alarm_sound.play(-1)


def appear_blip():
    """ pick one of ten burst sounds """
    sound_number = random.randint(1, 10)
    # how many variations of burst_sounds that there are
    appear_sound = pygame.mixer.Sound(
        "sounds/appear_blips/appear_blip_" + str(sound_number) + ".wav"
    )
    appear_sound.set_volume(.2)
    appear_sound.play()


def play_p1_bgm():
    track = "sounds/bgm/bgm_" + str(random.randint(-8, 2)) + ".mp3"
    pygame.mixer.music.stop()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.8)


def play_p2_bgm():
    track = "sounds/bgm/bgm_" + str(random.randint(3, 10)) + ".mp3"
    pygame.mixer.music.stop()
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.8)


def villian_jammerland():
    """ token aligned"""
    sound_number = random.randint(1, 7)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/villain/jammer_landed-00" + str(sound_number) + ".wav"
    )
    burst_sound.set_volume(.6)
    burst_sound.play()
    #


def villian_jammer_active():
    """ token aligned"""
    sound_number = random.randint(1, 12)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/villain/jammer_active-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/villain/jammer_active-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(.7)
    burst_sound.play()


def villian_timer_start():
    """ token aligned"""
    sound_number = random.randint(1, 3)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/villain/timer_start-00" + str(sound_number) + ".wav"
    )
    burst_sound.play()
    #


def villian_timer_end():
    """ token aligned"""
    sound_number = random.randint(1, 2)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/villain/timer_over-00" + str(sound_number) + ".wav"
    )
    burst_sound.play()
    #


def villian_system_lock():
    """ token aligned"""
    sound_number = random.randint(1, 6)
    # how many variations of burst_sounds that there are
    burst_sound = pygame.mixer.Sound(
        "sounds/villain/sytem_lock-00" + str(sound_number) + ".wav"
    )
    burst_sound.play()

def antivirus_activated():
    # microsoft neerja online natural english indiea voicegenerator.io on microsoft edge
    """ token aligned"""
    sound_number = random.randint(1, 22)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_intro/antivirus_voice-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_intro/antivirus_voice-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(10.00)
    burst_sound.play()

def antivirus_block():
    """ token aligned"""
    sound_number = random.randint(1, 30)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_errors/antivirus_voice-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_errors/antivirus_voice-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(10.00)
    burst_sound.play()
def antivirus_disabled():
    """ token aligned"""
    sound_number = random.randint(1, 21)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_defeat/antivirus_voice-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_defeat/antivirus_voice-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(10.00)
    burst_sound.play()

def antivirus_pass():
    """ token aligned"""
    sound_number = random.randint(1, 37)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_pass/antivirus_voice-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_pass/antivirus_voice-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(10.00)
    burst_sound.play()
def antivirus_welcome():
    """ token aligned"""
    sound_number = random.randint(1, 27)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_greetings/antivirus_voice-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_greetings/antivirus_voice-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(10.00)
    burst_sound.play()

def antivirus_firewall():
    """ token aligned"""
    sound_number = random.randint(1, 30)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_firewall/antivirus_voice-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_firewall/antivirus_voice-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(10.00)
    burst_sound.play()

def antivirus_jammer():
    """ token aligned"""
    sound_number = random.randint(1, 44)
    # how many variations of burst_sounds that there are
    if sound_number > 0 and sound_number < 10:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_jammer/antivirus_voice-00" + str(sound_number) + ".wav"
        )
    else:
        burst_sound = pygame.mixer.Sound(
            "sounds/antivirus/antivirus_jammer/antivirus_voice-0" + str(sound_number) + ".wav"
        )
    burst_sound.set_volume(10.00)
    burst_sound.play()
