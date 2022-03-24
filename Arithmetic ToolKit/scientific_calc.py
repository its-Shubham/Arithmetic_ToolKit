from tkinter import *
import math


calculator = Tk()
calculator.configure(bg="snow4", bd=10)
calculator.geometry("460x580+0+0")
calculator.resizable(width=False, height=False)
calculator.title("Scientific calculator")


def ClickButton(char):
    global operator
    operator += str(char)
    InputText.set(operator)


def ClearAllData():
    global operator
    text = operator[:-1]
    operator =text
    InputText.set(text)


def SquareRoot():
    global operator
    if int(operator)>=0:
        temp = str(eval(operator+'**(1/2)'))
        operator = temp
    else:
        temp = "ERROR"
    InputText.set(temp)


def ThirdRoot():
    global operator
    if int(operator) >= 0:
        temp = str(eval(operator + '**(1/3)'))
        operator = temp
    else:
        temp = "ERROR"
    InputText.set(temp)


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


def CalculateFactorial():
    global operator
    result = str(factorial(int(operator)))
    operator = result
    InputText.set(result)


def ChangeSign():
    global operator
    if operator[0]=='-':
        temp = operator[1:]
    else:
        temp = '-'+operator
    operator = temp
    InputText.set(temp)


def percent():
    global operator
    temp = str(eval(operator+'/100'))
    operator = temp
    InputText.set(temp)


def CalculateSin():
    global operator
    result = str(math.sin(math.radians(int(operator))))
    operator = result
    InputText.set(result)


def CalculateCos():
    global operator
    result = str(math.cos(math.radians(int(operator))))
    operator = result
    InputText.set(result)


def CalculateTan():
    global operator
    result = str(math.tan(math.radians(int(operator))))
    operator = result
    InputText.set(result)


def CalculateCot():
    global operator
    result = str(1/int(math.tan(math.radians(int(operator)))))
    operator = result
    InputText.set(result)


def EqualButton():
    global operator
    temp = str(eval(operator))
    operator = temp
    InputText.set(temp)


log, ln =math.log10 , math.log
sin, cos, tan = math.sin, math.cos, math.tan
e = math.exp
p = math.pi
E = '*10**'


operator = ""
InputText = StringVar()

display = Entry(calculator, font="Verdana 20 bold", textvariable=InputText, bd=10, insertwidth=6, bg='white', justify='right')
display.grid(columnspan=5, padx=20, pady=20)

FunctionButtonConfig = {'bd':5, 'fg':'black', 'bg':'grey','font':('Verdana',15,'bold')}
NumberButtonConfig = {'bd':5, 'fg':'#000', 'bg':'#BBB','font':('Verdana',15,'bold')}

sine = Button(calculator, FunctionButtonConfig , text="sin", command=CalculateSin)
sine.grid(row=1, column=0, sticky="nsew")

cosine = Button(calculator, FunctionButtonConfig , text="cos", command=CalculateCos)
cosine.grid(row=1, column=1, sticky="nsew")

tangent = Button(calculator, FunctionButtonConfig , text="tan", command=CalculateTan)
tangent.grid(row=1, column=2, sticky="nsew")

cotangent = Button(calculator, FunctionButtonConfig , text="cot", command=CalculateCot)
cotangent.grid(row=1, column=3, sticky="nsew")

PiNumberButton = Button(calculator, FunctionButtonConfig , text="π", command=lambda:ClickButton(str(math.pi)))
PiNumberButton.grid(row=1, column=4, sticky="nsew")

AbsValueButton = Button(calculator, FunctionButtonConfig, text='abs', command=lambda:ClickButton('abs('))
AbsValueButton.grid(row=2, column=0, sticky="nsew")

EulersNumButton = Button(calculator, FunctionButtonConfig, text='e', command=lambda :ClickButton(str(math.exp(1))))
EulersNumButton.grid(row=2, column=1, sticky="nsew")

FactorialButton = Button(calculator, FunctionButtonConfig, text='x!', command=CalculateFactorial)
FactorialButton.grid(row=2, column=2, sticky="nsew")

DivButton = Button(calculator, FunctionButtonConfig, text='/', command=lambda:ClickButton('//'))
DivButton.grid(row=2, column=3, sticky="nsew")

ModuleButton = Button(calculator, FunctionButtonConfig, text='mod', command=lambda:ClickButton('%'))
ModuleButton.grid(row=2, column=4, sticky="nsew")

SecondPowerButton = Button(calculator, FunctionButtonConfig, text='x\u00B2', command=lambda:ClickButton('**2'))
SecondPowerButton.grid(row=3, column=0, sticky="nsew")

ThirdPowerbutton = Button(calculator, FunctionButtonConfig, text='x\u00B3', command=lambda:ClickButton('**3'))
ThirdPowerbutton.grid(row=3, column=1, sticky="nsew")

nthPowerButton = Button(calculator, FunctionButtonConfig, text='x^n', command=lambda:ClickButton('**'))
nthPowerButton.grid(row=3, column=2, sticky="nsew")

InvPowerButton = Button(calculator, FunctionButtonConfig, text='x\u207b\xb9', command=lambda:ClickButton('**(-1)'))
InvPowerButton.grid(row=3, column=3, sticky="nsew")

TensPowerButton = Button(calculator, FunctionButtonConfig, text='10^x', font="Verdana 15 bold", command=lambda:ClickButton('10**'))
TensPowerButton.grid(row=3, column=4, sticky="nsew")

SquareRoot = Button(calculator,FunctionButtonConfig, text='\u00B2\u221A', command=SquareRoot)
SquareRoot.grid(row=4, column=0, sticky="nsew")

ThirdRoot = Button(calculator, FunctionButtonConfig, text='\u00B3\u221A', command=ThirdRoot)
ThirdRoot.grid(row=4, column=1, sticky="nsew")

nthRoot = Button(calculator, FunctionButtonConfig, text='\u221A', command=lambda:ClickButton('**(1/'))
nthRoot.grid(row=4, column=2, sticky="nsew")

LogBase_10 = Button(calculator, FunctionButtonConfig, text='log\u2081\u2080',font="Verdana 16 bold", command=lambda:ClickButton('log('))
LogBase_10.grid(row=4, column=3, sticky="nsew")

LogBase_e = Button(calculator, FunctionButtonConfig, text='ln', command=lambda:ClickButton('ln('))
LogBase_e.grid(row=4, column=4, sticky="nsew")

LeftBracker = Button(calculator, FunctionButtonConfig, text='(', command=lambda:ClickButton('('))
LeftBracker.grid(row=5, column=0, sticky="nsew")

RightBracker = Button(calculator, FunctionButtonConfig, text=')', command=lambda:ClickButton(')'))
RightBracker.grid(row=5, column=1, sticky="nsew")

Signs = Button(calculator, FunctionButtonConfig, text='\u00B1', command=lambda:ChangeSign)
Signs.grid(row=5, column=2, sticky="nsew")

Percentage = Button(calculator, FunctionButtonConfig, text='%', command=lambda:percent)
Percentage.grid(row=5, column=3, sticky="nsew")


ex = Button(calculator, FunctionButtonConfig, text='e^x', command=lambda:ClickButton('e('))
ex.grid(row=5, column=4, sticky="nsew")

button_7 = Button(calculator, NumberButtonConfig, text='7', command=lambda:ClickButton('7'))
button_7.grid(row=6, column=0, sticky="nsew")

button_8 = Button(calculator, NumberButtonConfig, text='8', command=lambda:ClickButton('8'))
button_8.grid(row=6, column=1, sticky="nsew")

button_9 = Button(calculator, NumberButtonConfig, text='9', command=lambda:ClickButton('9'))
button_9.grid(row=6, column=2, sticky="nsew")

Deleteone = Button(calculator, NumberButtonConfig, text='DEL', command=lambda:ClickButton('DEL'))
Deleteone.grid(row=6, column=3, sticky="nsew")

DeleteAll = Button(calculator, NumberButtonConfig, text='AC', command=lambda:ClearAllData())
DeleteAll.grid(row=6, column=4, sticky="nsew")

button_4 = Button(calculator, NumberButtonConfig, text='4', command=lambda:ClickButton('4'))
button_4.grid(row=7, column=0, sticky="nsew")

button_5 = Button(calculator, NumberButtonConfig, text='5', command=lambda:ClickButton('5'))
button_5.grid(row=7, column=1, sticky="nsew")

button_6 = Button(calculator, NumberButtonConfig, text='6', command=lambda:ClickButton('6'))
button_6.grid(row=7, column=2, sticky="nsew")

mul = Button(calculator, NumberButtonConfig, text='*', command=lambda:ClickButton('*'))
mul.grid(row=7, column=3, sticky="nsew")

div = Button(calculator, NumberButtonConfig, text='/', command=lambda:ClickButton('/'))
div.grid(row=7, column=4, sticky="nsew")

button_1 = Button(calculator, NumberButtonConfig, text='1', command=lambda:ClickButton('1'))
button_1.grid(row=8, column=0, sticky="nsew")

button_2 = Button(calculator, NumberButtonConfig, text='2', command=lambda:ClickButton('2'))
button_2.grid(row=8, column=1, sticky="nsew")

button_3 = Button(calculator, NumberButtonConfig, text='3', command=lambda:ClickButton('3'))
button_3.grid(row=8, column=2, sticky="nsew")

add = Button(calculator, NumberButtonConfig, text='+', command=lambda:ClickButton('+'))
add.grid(row=8, column=3, sticky="nsew")

sub = Button(calculator, NumberButtonConfig, text='-', command=lambda:ClickButton('-'))
sub.grid(row=8, column=4, sticky="nsew")

button_0 = Button(calculator, NumberButtonConfig, text='0', command=lambda:ClickButton('0'))
button_0.grid(row=9, column=0, sticky="nsew")

point = Button(calculator, NumberButtonConfig, text='.', command=lambda:ClickButton('.'))
point.grid(row=9, column=1, sticky="nsew")

exp = Button(calculator, NumberButtonConfig, text='EXP', command=lambda:ClickButton('E'))
exp.grid(row=9, column=2, sticky="nsew")

equal = Button(calculator, NumberButtonConfig, text='=', command=lambda:EqualButton())
equal.grid(row=8, column=2, sticky="nsew")


calculator.mainloop()