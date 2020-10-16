from tkinter import *

window = Tk()
window.geometry("310x150")
name = Entry(window, width=25)
frstgrade = Entry(window, width=25)
secgrade = Entry(window, width=25)
trdgrade = Entry(window, width=25)
resultbx = Text(window, height=1, width=25)

lbnme = Label(window, text="Name:")
lbfst = Label(window, text="First grade:")
lbscnd = Label(window, text="Second grade:")
lbthrd = Label(window, text="Third grade:")
lbrbx = Label(window, text="Result:")


def res():
    avg = round(((int(frstgrade.get()) + int(secgrade.get()) + int(trdgrade.get())) / 3))
    if avg > 50:
        resultbx.insert(END, name.get() + " got " + str(avg) + " has passed")

    elif avg < 50:
        resultbx.insert(END, name.get() + " got " + str(avg) + " has failed")


resBtn = Button(window, text="Get result", command=res)

name.grid(row=1, column=1)
frstgrade.grid(row=2, column=1)
secgrade.grid(row=3, column=1)
trdgrade.grid(row=4, column=1)
resultbx.grid(row=5, column=1)
resBtn.grid(row=6, column=0, sticky=W)
lbnme.grid(row=1, column=0, sticky=W)
lbfst.grid(row=2, column=0, sticky=W)
lbscnd.grid(row=3, column=0, sticky=W)
lbthrd.grid(row=4, column=0, sticky=W)
lbrbx.grid(row=5, column=0, sticky=W)
window.mainloop()
