from tkinter import *
import math

root = Tk()
root.title("Chess")

pieces = []

p = PhotoImage(file='./WhiteBishop.png')



board = []

def test():
    pass

for l in range(8):
    board.append([])
    for n in range(8):
        board[l].append(Button(root, text=int(l)*8+n, padx=40, pady=40, command=test, image=p))  # figure out WTF a closure is

# Numbers are Vertical, Letters are Horizontal
# White is on Bottom, Black is on Top
# Number * 8 + (Horizontal - A)

for l in range(8):
    for n in range(8):
        board[l][n].grid(row=l, column=n)


root.mainloop()
# while True:
#    root.update_idletasks()
#    root.update()
