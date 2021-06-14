from tkinter import *
import random

popup_quotes = [
    "IT IS OVER",
    "INTRUDER",
    "I FOUND YOU",
    "ILLEGAL ACTIVITY",
    "HELLO THERE",
]

my_window = Tk()
my_window.overrideredirect(True)
my_window.geometry("700x250")


label_1 = Label(
    my_window,
    text=("{}".format(random.choice(popup_quotes))),
    bd=1,
    font="ariel 30",
    width=15,
    height=4,
)
btn = Button(
    my_window, text="SUPPRESS COUNTERMEASURES", bd="5", command=my_window.destroy
)

label_1.pack()
btn.pack()

my_window.mainloop()