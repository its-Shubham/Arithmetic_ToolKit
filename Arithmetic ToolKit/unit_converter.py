from tkinter import *

units = {
#________________Lengths__________________________________
    "cm" : 0.01,
    "m" : 1.0,
    "Km" : 1000.0,
    "feet" : 0.3048,
    "miles" :1609.344,
    "inches" : 0.0254,
#________________Weights__________________________________
    "grams" : 1.0,
    "kg" : 1000.0,
    "quintals": 100000.0,
    "tonnes" : 1000000.0,
    "pounds" : 453.592,
#________________Areas___________________________________
    "sq. m" : 1.0,
    "sq. km": 1000000.0,
    "are" : 100.0,
    "hectare" : 10000.0,
    "acre" : 4046.856,
    "sq. mile" : 2590000.0,
    "sq. foot" : 0.0929,
    "cu. cm" : 0.001,
#________________Volumes_________________________________
    "Litre" : 1.0,
    "ml" : 0.001,
    "gallon": 3.785
}

lengths = ["cm", "m", "Km", "feet", "miles", "inches"]
weights = ["kg", "grams", "quintals", "tonnes", "poounds"]
areas = ["sq. m", "sq. km", "are", "hectare", "acre", "sq. mile", "sq. foot"]
volumes = ["cu. cm", "Litre", "ml", "gallon"]
temps = ["Celsius", "Fahrenheit"]

OPTIONS = ["select units",
            "cm",
            "m",
            "Km",
            "feet",
            "miles",
            "inches",
            "kg",
            "grams",
            "quintals",
            "tonnes",
            "pounds",
            "Celsius",
            "Fahrenheit",
            "sq. m",
            "sq. km",
            "are",
            "hectare",
            "acre",
            "sq. mile",
            "sq. foot",
            "cu. cm",
            "Litre",
            "ml",
            "gallon"]
root = Tk()
root.geometry("420x320")
root.resizable(width=False, height=False)
root.title("Unit Converter")

def convert():
    inp = float(inputEntry.get())
    inp_unit = inputopt.get()
    out_unit = outputopt.get()

    cons = [inp_unit in lengths and out_unit in lengths,
            inp_unit in weights and out_unit in weights,
            inp_unit in temps and out_unit in temps,
            inp_unit in areas and out_unit in areas,
            inp_unit in volumes and out_unit in volumes,
            ]
    if any(cons):
        if inp_unit == "Celsius" and out_unit == "Fahrenheit":
            outputEntry.delete(0,END)
            outputEntry.insert(0,(inp*1.8) + 32)
        elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
            outputEntry.delete(0, END)
            outputEntry.insert(0, (inp - 32) * (5/9))
        else:
            outputEntry.delete(0, END)
            outputEntry.insert(0, round(inp * units[inp_unit]/units[out_unit], 5))

    else:
        outputEntry.delete(0, END)
        outputEntry.insert(0, "ERROR")


inputopt = StringVar()
inputopt.set(OPTIONS[0])

outputopt = StringVar()
outputopt.set(OPTIONS[0])

#______________________Widgets________________________
inputlabel = Label(root, text="From", font="comicsansms 12 bold", relief=RAISED, bg="snow4")
inputlabel.grid(row = 0, column = 0, pady = 20)

inputEntry = Entry(root, font="comicsansms 12", justify="center")
inputEntry.grid(row = 1, column = 0, padx = 35, ipady = 5)

inputMenu = OptionMenu(root, inputopt, *OPTIONS)
inputMenu.grid(row = 1, column = 1)
inputMenu.config(font ="comicsansms 12")

outputlabel = Label(root, text="Output",font="comicsansms 12 bold", relief=RAISED, bg="snow4")
outputlabel.grid(row = 2, column = 0, pady = 20)

outputEntry = Entry(root, justify="center", font="comicsansms 12")
outputEntry.grid(row = 3, column = 0, padx = 35, ipady = 5)

outputMenu = OptionMenu(root,outputopt, *OPTIONS)
outputMenu.grid(row = 3, column = 1)
outputMenu.config(font ="comicsansms 12")

convertbtn = Button(root, text="Convert", command=convert, relief=RAISED, padx=80, pady=2)
convertbtn.grid(row=4, column=0, columnspan=2, pady=50)


root.mainloop()