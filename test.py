import pynput
from pynput import keyboard
import time


def on_press(key):
    if key == keyboard.Key.enter:
        print("enter pressed".format(key))


listener = keyboard.Listener(on_press=on_press)
listener.start()

time.sleep(5)
print("listener stopped")
listener.stop()
time.sleep(3)
listener = keyboard.Listener(on_press=on_press)
listener.start()
print("listener started again")
time.sleep(3)