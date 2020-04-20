import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x500")
root.resizable(0, 0)
root.title("Tic Tac Toe Game by Siddharth")

btnrow1 = Frame(root, bg='black')
btnrow1.pack(expand=True, side=TOP)

btnrow2 = Frame(root, bg='green')
btnrow2.pack(expand=True, side=BOTTOM)

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 'X'
stop_game = False


def callback(r, c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X', fg='pink', bg='blue')
        states[r][c] = 'X'
        player = 'O'

    if player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='O', fg='yellow', bg='blue')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()


def check_for_winner():
    global stop_game
    for i in range(3):
        # checking horizontaly
        if states[i][0] == states[i][1] == states[i][2] != 0:
            b[i][0].config(bg='red')
            b[i][1].config(bg='red')
            b[i][2].config(bg='red')
            stop_game = True

    for i in range(3):
        # checking vertically
        if states[0][i] == states[1][i] == states[2][i] != 0:
            b[0][i].config(bg='red')
            b[1][i].config(bg='red')
            b[2][i].config(bg='red')
            stop_game = True

        # Left daigonal
        if states[0][0] == states[1][1] == states[2][2] != 0:
            b[0][0].config(bg='red')
            b[1][1].config(bg='red')
            b[2][2].config(bg='red')
            stop_game = True

        # Right Daigonal
        if states[0][2] == states[1][1] == states[2][0] != 0:
            b[0][2].config(bg='red')
            b[1][1].config(bg='red')
            b[2][0].config(bg='red')
            stop_game = True

    if stop_game == True:
        if player == 'X':
            messagebox.showinfo(" ", "PLayer 2 wins")
        else:
            messagebox.showinfo(" ", "PLayer 1 wins")


def restart():
    global b
    global states
    global stop_game
    global player
    b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 'X'
    stop_game = False
    game()


def game():
    global b
    global states
    global stop_game
    global player
    for i in range(3):
        for j in range(3):
            b[i][j] = Button(btnrow1, font=('comic sans', 50), width=3,
                             bg='white', command=lambda r=i, c=j: callback(r, c))
            b[i][j].grid(row=i, column=j)


game()

restart = Button(btnrow2, text='RESTART', font=(
    'comic sans', 10), width=10, height=2, command=restart)
restart.pack(side=LEFT, expand=True, fill='both')
root.mainloop()
