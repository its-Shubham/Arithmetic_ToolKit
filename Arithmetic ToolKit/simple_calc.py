from tkinter import *

sim_root = Tk()
sim_root.geometry("330x352")
sim_root.resizable(width=False, height=False)
sim_root.title("Calculator")


###################Starting with functions ####################


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


# 'bt_equal':This method calculates the expression
# present in input field

def bt_equal():
    global expression
    result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""


expression = ""

# 'StringVar()' :It is used to get the instance of input field

input_text = StringVar()

# Let us creating a frame for the input field

input_frame = Frame(sim_root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

# Let us create a input field inside the 'Frame'

input_field = Entry(input_frame, font=('Courier', 18, 'bold'), textvariable=input_text, width=50, bg="white", bd=0, justify=RIGHT, borderwidth=5)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field


btns_frame = Frame(sim_root, width=312, height=272.5, bg="snow")
btns_frame.pack()

# first row

clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: bt_clear(), borderwidth=2)
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/"), borderwidth=2)
divide.grid(row=0, column=3, padx=1, pady=1)

# second row

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(7), borderwidth=2)
seven.grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(8), borderwidth=2)
eight.grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9), borderwidth=2)
nine.grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("*"), borderwidth=2)
multiply.grid(row=1, column=3, padx=1, pady=1)

# third row

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(4), borderwidth=2)
four.grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(5), borderwidth=2)
five.grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(6), borderwidth=2)
six.grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("-"), borderwidth=2)
minus.grid(row=2, column=3, padx=1, pady=1)

# fourth row

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(1), borderwidth=2)
one.grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(2), borderwidth=2)
two.grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(3), borderwidth=2)
three.grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("+"), borderwidth=2)
plus.grid(row=3, column=3, padx=1, pady=1)

# fourth row

zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0), borderwidth=2)
zero.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("."), borderwidth=2)
point.grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: bt_equal(), borderwidth=2)
equals.grid(row=4, column=3, padx=1, pady=1)

sim_root.mainloop()