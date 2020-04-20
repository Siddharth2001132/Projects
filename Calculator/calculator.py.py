import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""


def btn1_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn2_clicked():
    global val
    val = val + "2"
    data.set(val)


def btn3_clicked():
    global val
    val = val + "3"
    data.set(val)


def btn4_clicked():
    global val
    val = val + "4"
    data.set(val)


def btn5_clicked():
    global val
    val = val + "5"
    data.set(val)


def btn6_clicked():
    global val
    val = val + "6"
    data.set(val)


def btn7_clicked():
    global val
    val = val + "7"
    data.set(val)


def btn8_clicked():
    global val
    val = val + "8"
    data.set(val)


def btn9_clicked():
    global val
    val = val + "9"
    data.set(val)


def btn0_clicked():
    global val
    val = val + "0"
    data.set(val)


def btnC_clicked():
    global val
    global A
    global operator
    val = ""
    A = 0
    operator = ""
    data.set(val)


def btnplus__clicked():
    global val
    global A
    global operator
    if val.isdigit() == False:
        if operator == "+":
            val = str(int((val.split('+')[0])) + int((val.split('+')[1])))
        elif operator == "-":
            val = str(int((val.split('-')[0])) - int((val.split('-')[1])))
        elif operator == "*":
            val = str(int((val.split('*')[0])) * int((val.split('*')[1])))
        elif operator == "/":
            val = str(int((val.split('/')[0])) // int((val.split('/')[1])))
    if val.isdigit():
        operator = "+"
        val = val + "+"
        data.set(val)
    else:
        val = str(int((val.split('+')[0])) + int((val.split('+')[1])))
        operator = "+"
        val = val + "+"
        data.set(val)


def btnminus__clicked():
    global val
    global A
    global operator
    if val.isdigit() == False:
        if operator == "+":
            val = str(int((val.split('+')[0])) + int((val.split('+')[1])))
        elif operator == "-":
            val = str(int((val.split('-')[0])) - int((val.split('-')[1])))
        elif operator == "*":
            val = str(int((val.split('*')[0])) * int((val.split('*')[1])))
        elif operator == "/":
            val = str(int((val.split('/')[0])) // int((val.split('/')[1])))

    if val.isdigit():
        operator = "-"
        val = val + "-"
        data.set(val)
    else:
        val = str(int((val.split('-')[0])) - int((val.split('-')[1])))
        operator = "-"
        val = val + "-"
        data.set(val)


def btnmulti__clicked():
    global val
    global A
    global operator
    if val.isdigit() == False:
        if operator == "+":
            val = str(int((val.split('+')[0])) + int((val.split('+')[1])))
        elif operator == "-":
            val = str(int((val.split('-')[0])) - int((val.split('-')[1])))
        elif operator == "*":
            val = str(int((val.split('*')[0])) * int((val.split('*')[1])))
        elif operator == "/":
            val = str(int((val.split('/')[0])) // int((val.split('/')[1])))

    if val.isdigit():
        operator = "*"
        val = val + "*"
        data.set(val)
    else:
        val = str(int((val.split('*')[0])) * int((val.split('*')[1])))
        operator = "*"
        val = val + "*"
        data.set(val)


def btndiv__clicked():
    global val
    global A
    global operator
    if val.isdigit() == False:
        if operator == "+":
            val = str(int((val.split('+')[0])) + int((val.split('+')[1])))
        elif operator == "-":
            val = str(int((val.split('-')[0])) - int((val.split('-')[1])))
        elif operator == "*":
            val = str(int((val.split('*')[0])) * int((val.split('*')[1])))
        elif operator == "/":
            val = str(int((val.split('/')[0])) // int((val.split('/')[1])))

    if val.isdigit():
        operator = "/"
        val = val + "/"
        data.set(val)
    else:
        val = str(int((val.split('/')[0])) // int((val.split('/')[1])))
        operator = "/"
        val = val + "/"
        data.set(val)


def result_clicked():
    global val
    global A
    global operator
    store = val
    if operator == '+':
        ans = int((store.split('+')[0])) + int((store.split('+')[1]))
        data.set(ans)
        val = str(ans)

    elif operator == '-':
        ans = int((store.split('-')[0])) - int((store.split('-')[1]))
        data.set(ans)
        val = str(ans)
    elif operator == '*':
        ans = int((store.split('*')[0])) * int((store.split('*')[1]))
        data.set(ans)
        val = str(ans)
    elif operator == '/':
        val2 = int((store.split('/')[1]))
        if val2 != 0:
            ans = int(int((store.split('/')[0])) // val2)
            data.set(ans)
            val = str(ans)
        else:
            messagebox.showerror("Error", "Division by 0 not supported")
            A = ""
            val = ""
            data.set(val)


root = tkinter.Tk()
root.geometry("300x500")
root.resizable(0, 0)
root.title("Claculator")

data = StringVar()

lbl = Label(root, text='Values', anchor=SE, font=(
    "comic sans", 30), bg='white', textvariable=data)
lbl.pack(expand=True, fill='both')
# Frames
btnrow1 = Frame(root, bg='white')
btnrow1.pack(expand=True, fill='both')

btnrow2 = Frame(root, bg='white')
btnrow2.pack(expand=True, fill='both')

btnrow3 = Frame(root, bg='white')
btnrow3.pack(expand=True, fill='both')

btnrow4 = Frame(root, bg='white')
btnrow4.pack(expand=True, fill='both')

# btnnrow1 buttons

btn1 = Button(btnrow1, text='1', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btn1_clicked)
btn1.pack(side=LEFT, expand=True, fill='both')

btn2 = Button(btnrow1, text='2', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btn2_clicked)
btn2.pack(side=LEFT, expand=True, fill='both')

btn3 = Button(btnrow1, text='3', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btn3_clicked)
btn3.pack(side=LEFT, expand=True, fill='both')

btn4 = Button(btnrow1, text='+', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btnplus__clicked)
btn4.pack(side=LEFT, expand=True, fill='both')

# btnnrow2 buttons

btn5 = Button(btnrow2, text='4', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btn4_clicked)
btn5.pack(side=LEFT, expand=True, fill='both')

btn6 = Button(btnrow2, text='5', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btn5_clicked)
btn6.pack(side=LEFT, expand=True, fill='both')

btn7 = Button(btnrow2, text='6', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btn6_clicked)
btn7.pack(side=LEFT, expand=True, fill='both')

btn8 = Button(btnrow2, text='-', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btnminus__clicked)
btn8.pack(side=LEFT, expand=True, fill='both')

# btnnrow3 buttons

btn9 = Button(btnrow3, text='7', font=("comic sans", 20),
              relief=GROOVE, border=0, command=btn7_clicked)
btn9.pack(side=LEFT, expand=True, fill='both')

btn10 = Button(btnrow3, text='8', font=("comic sans", 20),
               relief=GROOVE, border=0, command=btn8_clicked)
btn10.pack(side=LEFT, expand=True, fill='both')

btn11 = Button(btnrow3, text='9', font=("comic sans", 20),
               relief=GROOVE, border=0, command=btn9_clicked)
btn11.pack(side=LEFT, expand=True, fill='both')

btn12 = Button(btnrow3, text='x', font=(
    "comic sans", 20), relief=GROOVE, border=0, command=btnmulti__clicked)
btn12.pack(side=LEFT, expand=True, fill='both')

# btnnrow4 buttons

btn13 = Button(btnrow4, text='C', font=(
    "comic sans", 20), relief=GROOVE, border=0, command=btnC_clicked)
btn13.pack(side=LEFT, expand=True, fill='both')

btn14 = Button(btnrow4, text='0', font=("comic sans", 20),
               relief=GROOVE, border=0, command=btn0_clicked)
btn14.pack(side=LEFT, expand=True, fill='both')

btn15 = Button(btnrow4, text='=', font=(
    "comic sans", 20), relief=GROOVE, border=0, command=result_clicked)
btn15.pack(side=LEFT, expand=True, fill='both')

btn16 = Button(btnrow4, text='/', font=("comic sans", 20),
               relief=GROOVE, border=0, command=btndiv__clicked)
btn16.pack(side=LEFT, expand=True, fill='both')

root.mainloop()
