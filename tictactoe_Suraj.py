from tkinter import *
from tkinter import messagebox
import math
import copy

root = Tk()
root.geometry('320x360')
root.title('TicTacToe')


player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player2 = copy.copy(player1)

player_success = []

e = Entry(root, width=22, borderwidth=0, justify=RIGHT,
          bg='#eeeeee', font=('Arial', 13))
e.grid(row=3, column=0, columnspan=4)
f = Entry(root, width=22, borderwidth=0, justify=CENTER,
          bg='#eeeeee', font=('Arial', 13))
f.grid(row=4, column=0, columnspan=4)
count = 0
e.insert(0, "Player1->X     Player2->O")
f.insert(0, "Player1's turn")


def textbuttons():
    btn_text1.set("")
    btn_text2.set("")
    btn_text3.set("")
    btn_text4.set("")
    btn_text5.set("")
    btn_text6.set("")
    btn_text7.set("")
    btn_text8.set("")
    btn_text9.set("")


def reset():
    global count
    for i in range(0, 9):
        player1[i] = 0
        player2[i] = 0
    f.delete(0, END)
    f.config({"background": "#eeeeee"})
    count = 0
    textbuttons()


def popup():
    response = messagebox.askyesno('End', 'Would you like to play again?')
    if response == 0:
        stats()
        root.quit()
    else:
        reset()


def stats():
    messagebox.showinfo('Game Stats', 'Game summary\nPlayer1 wins {} game(s)\nPlayer2 wins {} game(s)\nThe game has ended'.format(
        player_success.count('one'), player_success.count('two')))


def player_win_check(player1):
    if   player1[0] == player1[1] == player1[2] == 1:
        return True
    elif player1[0] == player1[4] == player1[8] == 1:
        return True
    elif player1[0] == player1[3] == player1[6] == 1:
        return True
    elif player1[1] == player1[4] == player1[7] == 1:
        return True
    elif player1[2] == player1[5] == player1[8] == 1:
        return True
    elif player1[3] == player1[4] == player1[5] == 1:
        return True
    elif player1[6] == player1[7] == player1[8] == 1:
        return True
    elif player1[2] == player1[4] == player1[6] == 1:
        return True


def check_win():
    global count
    if player_win_check(player1):
        f.delete(0, END)
        f.config({"background": "#ff5722"})
        f.insert(0, 'WINNER : PLAYER1')
        player_success.append('one')
        popup()

    elif player_win_check(player2):
        f.delete(0, END)
        f.config({"background": "#ff5722"})
        f.insert(0, 'WINNER : PLAYER2')
        player_success.append('two')
        popup()
    elif count == 9:
        print(count)
        f.delete(0, END)
        f.insert(0, 'DRAW!')
        popup()


def button_click(btn_text,i):
    global count
    if (count % 2 == 0):
        f.delete(0, END)
        f.insert(0, "Player2's turn")
        btn_text.set("X")
        player1[i] = 1

    else:
        f.delete(0, END)
        f.insert(0, "Player1's turn")
        btn_text.set("O")
        player2[i] = 1
    count += 1
    check_win()



btn_text1 = StringVar()
btn_text2 = StringVar()
btn_text3 = StringVar()
btn_text4 = StringVar()
btn_text5 = StringVar()
btn_text6 = StringVar()
btn_text7 = StringVar()
btn_text8 = StringVar()
btn_text9 = StringVar()


button1 = Button(root, textvariable=btn_text1, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, bg="#323232", fg="#abedd8", relief=GROOVE, command=lambda:button_click(btn_text1,0)).grid(row=0, column=1)
button2 = Button(root, textvariable=btn_text2, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, relief=GROOVE, bg="#323232", fg="#abedd8", command=lambda:button_click(btn_text2,1)).grid(row=0, column=2)
button3 = Button(root, textvariable=btn_text3, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, relief=GROOVE, bg="#323232", fg="#abedd8", command=lambda:button_click(btn_text3,2)).grid(row=0, column=3)

button4 = Button(root, textvariable=btn_text4, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, relief=GROOVE, bg="#323232", fg="#abedd8", command=lambda:button_click(btn_text4,3)).grid(row=1, column=1)
button5 = Button(root, textvariable=btn_text5, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, relief=GROOVE, bg="#323232", fg="#abedd8", command=lambda:button_click(btn_text5,4)).grid(row=1, column=2)
button6 = Button(root, textvariable=btn_text6, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, relief=GROOVE, bg="#323232", fg="#abedd8", command=lambda:button_click(btn_text6,5)).grid(row=1, column=3)

button7 = Button(root, textvariable=btn_text7, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, relief=GROOVE, bg="#323232", fg="#abedd8", command=lambda:button_click(btn_text7,6)).grid(row=2, column=1)
button8 = Button(root, textvariable=btn_text8, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, relief=GROOVE, bg="#323232", fg="#abedd8", command=lambda:button_click(btn_text8,7)).grid(row=2, column=2)
button9 = Button(root, textvariable=btn_text9, font=('Verdana', 17), activebackground='#bbbbbb', border=1,
                 height=3, width=7, relief=GROOVE, bg="#323232", fg="#abedd8", command=lambda:button_click(btn_text9,8)).grid(row=2, column=3)


root.mainloop()