import random
from tkinter import *

rnd = random.randrange(1, 100)

window = Tk()

gb = Entry(window)

lb = Label(text="answer")
lbG = Label(text="guesses")
rndL = Label(text="The number")
guesses = 0


def guess():
    global guesses
    guesses += 1
    if int(gb.get()) < rnd:
        lb.config(text="Too low")
    elif int(gb.get()) > rnd:
        lb.config(text="Too high")
    elif int(gb.get()) == rnd:
        lb.config(text="Correct")
        rndL.config(text=rnd)
    lbG.config(text="Guesses:" + str(guesses))


guessBt = Button(window, height=1, width=15, text="guess", command=guess)


gb.pack()
guessBt.pack()
lb.pack()
lbG.pack()
rndL.pack()
window.mainloop()
