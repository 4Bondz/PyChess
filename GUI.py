from tkinter import *
import os
import math

root = Tk()
root.title("Chess")

pieces = ["\BlackBishop.png", "./BlackKing.png", "./BlackKnight.png", "./BlackPawn.png", "./BlackQueen.png",
          "./BlackRook.png", "./WhiteBishop.png", "./WhiteKing.png", "./WhiteKnight.png", "./WhitePawn.png",
          "./WhiteQueen.png", "./WhiteRook.png"]

loc = os.getcwd()
print(loc)
board = []


def test():
    pass


for l in range(8):
    board.append([])
    for n in range(8):
        board[l].append(Button(root, text=int(l) * 8 + n, padx=40, pady=40, command=test,
                               image=loc + pieces[0]))  # figure out WTF a closure is

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
