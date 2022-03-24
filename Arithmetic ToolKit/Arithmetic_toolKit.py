from tkinter import *
from currency_convrt import *
import currency_convrt
import subprocess


def sci():
    subprocess.call("scientific_calc.py", shell=True)


def simp():
    subprocess.call("simple_calc.py", shell=True)


def unit():
    subprocess.call("unit_converter.py", shell=True)
# _______________________________GUI _____________________________________________


root = Tk()
root.geometry("620x200")
root.title("Arithmatic Tool")
root.resizable(width=False, height=False)

heading = Label(text='''Arithmatic Tool''', bg="grey", font="comicsansms 15 bold", relief=GROOVE, borderwidth=5)
heading.pack(side=TOP, fill=X)
statement = Label(text='''Select operation from below''', pady=25, font="cosmicsansms 12 bold")
statement.pack(side=TOP)

# ________________________ FRAME _____________________________________________
frame1 = Frame(root, relief=SUNKEN)
frame1.pack(side=TOP, padx=20)

# ________________________ BUTTON _____________________________________________
b1 = Button(frame1, text="currency converter", borderwidth=5, command=currency_convrt.main)
b1.pack(side=LEFT, padx=10)


b2 = Button(frame1, text="unit converter", borderwidth=5, command=unit)
b2.pack(side=LEFT, padx=10)


b3 = Button(frame1, text="scientific calculator", borderwidth=5, command=sci)
b3.pack(side=LEFT, padx=10)


b4 = Button(frame1, text="simple calculator", borderwidth=5, command=simp)
b4.pack(side=LEFT, padx=10)


b5 = Button(frame1, text="quit", borderwidth=5, command=quit)
b5.pack(side=LEFT, padx=10)


root.mainloop()
