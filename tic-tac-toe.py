from tkinter import *
from tkinter import messagebox
import random as r

def button(frame): 
    b = Button(frame, padx=1, bg="white", width=3, text="   ", font=('arial', 60, 'bold'), relief="raised", bd=5)
    return b

def change_a(): 
    global a
    a = 'O' if a == 'X' else 'X'

def reset(): 
    global a
    a = r.choice(['O', 'X'])
    label.config(text=a + "'s Chance")
    for i in range(3):
        for j in range(3):
            b[i][j]["text"] = " "
            b[i][j]["state"] = NORMAL

def check():
    for i in range(3):
        if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] == a:
            messagebox.showinfo("Congrats!!", "'" + a + "' has won")
            reset()
            return
    if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == a:
        messagebox.showinfo("Congrats!!", "'" + a + "' has won")
        reset()
        return
    elif all(b[i][j]["state"] == DISABLED for i in range(3) for j in range(3)):
        messagebox.showinfo("Tied!!", "The match ended in a draw")
        reset()

def click(row, col):  
    b[row][col].config(text=a, state=DISABLED, disabledforeground=colour[a])
    check()
    change_a()
    label.config(text=a + "'s Chance")

root = Tk()  
root.title("Tic-Tac-Toe")  
a = r.choice(['O', 'X'])  
colour = {'O': "deep sky blue", 'X': "lawn green"}
b = [[button(root) for _ in range(3)] for _ in range(3)]  #3x3 grid 

for i in range(3):
    for j in range(3):
        b[i][j].config(command=lambda row=i, col=j: click(row, col))
        b[i][j].grid(row=i, column=j)

label = Label(text=a + "'s Chance", font=('arial', 20, 'bold'))
label.grid(row=3, column=0, columnspan=3)
root.mainloop()
