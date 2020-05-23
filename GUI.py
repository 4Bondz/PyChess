from tkinter import *
import os
import boardv2 as game
import time
import math

root = Tk()
root.title("Chess")

loc = os.getcwd()
print(loc)

clickState = 0
selectedPiece = 0
do_move = 0
move_string = ''
B = game.Board()
turn = 'w'
board = []
hold = []

def test():
    pass


pieces = ["./BlackBishop.png", "./BlackKing.png", "./BlackKnight.png", "./BlackPawn.png", "./BlackQueen.png",
          "./BlackRook.png", "./WhiteBishop.png", "./WhiteKing.png", "./WhiteKnight.png", "./WhitePawn.png",
          "./WhiteQueen.png", "./WhiteRook.png"]

short_pieces  = {"P":"Pawn", "Q":"Queen", "B":"Bishop", "R":"Rook", "N":"Knight", "K":"King"}

names = ["bBishop", "bKing", "bKnight", "bPawn", "bQueen", "bRook", "wBishop", "wKing", "wKnight", "wPawn",
         "wQueen", "wRook"]

piece_images = dict(zip(names, pieces))


def onclick(val):
    # BOARD IS FLIPPED ON X AXIS -> PERFORM 7 - X Negation
    global clickState
    global selectedPiece
    global do_move
    global move_string
    global B
    global turn
    global short_pieces
    global hold

    if clickState == 1:  # Val = DST
        SRC_l = 8 - selectedPiece // 8
        SRC_n = selectedPiece % 8
        DST_l = 8 - val // 8
        DST_n = val % 8
        print("SRC ", SRC_l, chr(SRC_n + 65))
        print("DST ", DST_l, chr(DST_n + 65))
        move_string = chr(SRC_n + 65) + str(SRC_l) + chr(DST_n + 65) + str(DST_l)
        print(move_string)
        clickState = 0

        x = B.move_piece(move_string, turn)
        if x:
            DST = piece_images[turn + short_pieces[x]]
            MT = "./empty.png"
            DSTp = PhotoImage(file=DST).subsample(2, 2)
            MTp = PhotoImage(file=MT).subsample(2, 2)
            hold.append(DSTp)
            hold.append(MTp)
            board[8 - DST_l][DST_n].configure(image=DSTp)
            board[8 - SRC_l][SRC_n].configure(image=MTp)
            # TODO : GET The piece from somewhere
            # TODO : Load up that piece into the SRC square
            #
            if turn == 'w':
                turn = 'b'
            else:
                turn = 'w'
        else:
            print("BAD MOVE")
        print(clickState)
    else:
        clickState = 1  # Selected a piece
        selectedPiece = val
        print(clickState)
    # Piece + Location (CHESS)

    # root.update_idletasks()
    # root.update()
    # board[y][x].configure(image=p) # CONFIGURE THE IMAGE
    # Manual Update:     root.update_idletasks()
    #                    root.update()
    # Numbers are Vertical, Letters are Horizontal
    # White is on Bottom, Black is on Top
    # Number * 8 + (Horizontal - A)
    # for l in range(8):
    #    for n in range(8):
    #        board[l][n].grid(row=l, column=n)


def main():
    global board
    # Perform Total Reset of board

    # Board stored in the "board" variable, a 2-D List of buttons
    for l in range(8):
        board.append([])
        for n in range(8):
            board[l].append(
                Button(root, text=int(l) * 8 + n, padx=40, pady=40, command=lambda l=l, n=n: onclick(int(l) * 8 + n)))
            board[l][n].grid(row=l, column=n)
            # figure out WTF a closure
    bRook = piece_images["bRook"]
    bRookp = PhotoImage(file=bRook).subsample(2, 2)
    board[0][0].configure(image=bRookp)
    board[0][7].configure(image=bRookp)

    bBishop = piece_images["bBishop"]
    bBishopp = PhotoImage(file=bBishop).subsample(2, 2)
    board[0][2].configure(image=bBishopp)
    board[0][5].configure(image=bBishopp)

    bKnight = piece_images["bKnight"]
    bKnightp = PhotoImage(file=bKnight).subsample(2, 2)
    board[0][1].configure(image=bKnightp)
    board[0][6].configure(image=bKnightp)

    bQueen = piece_images["bQueen"]
    bQueenp = PhotoImage(file=bQueen).subsample(2, 2)
    board[0][3].configure(image=bQueenp)

    bKing = piece_images["bKing"]
    bKingp = PhotoImage(file=bKing).subsample(2, 2)
    board[0][4].configure(image=bKingp)

    wRook = piece_images["wRook"]
    wRookp = PhotoImage(file=wRook).subsample(2, 2)
    board[7][0].configure(image=wRookp)
    board[7][7].configure(image=wRookp)

    wBishop = piece_images["wBishop"]
    wBishopp = PhotoImage(file=wBishop).subsample(2, 2)
    board[7][2].configure(image=wBishopp)
    board[7][5].configure(image=wBishopp)

    wKnight = piece_images["wKnight"]
    wKnightp = PhotoImage(file=wKnight).subsample(2, 2)
    board[7][1].configure(image=wKnightp)
    board[7][6].configure(image=wKnightp)

    wQueen = piece_images["wQueen"]
    wQueenp = PhotoImage(file=wQueen).subsample(2, 2)
    board[7][4].configure(image=wQueenp)

    wKing = piece_images["wKing"]
    wKingp = PhotoImage(file=wKing).subsample(2, 2)
    board[7][3].configure(image=wKingp)


    label = Label(root)
    label.images = [[], [], []]

    for t in range(8):  # Generate references to the images so they don't get garbage collected, stupid but effective
        bPawn = piece_images["bPawn"]
        wPawn = piece_images["wPawn"]
        label.images[0].append(PhotoImage(file=bPawn).subsample(2, 2))
        label.images[1].append(PhotoImage(file=wPawn).subsample(2, 2))
        board[1][t].configure(image=label.images[0][t])
        board[6][t].configure(image=label.images[1][t])
    root.update_idletasks()
    root.update()

    for q in range(32):
        bempty = "./empty.png"
        label.images[2].append(PhotoImage(file=bempty).subsample(2, 2))
        board[2 + (q // 8)][q % 8].configure(image=label.images[2][q])

    while True:
        root.update_idletasks()
        root.update()

    '''while True:
        w = input("White to Move: ")
        x = B.move_piece(w, 'w')
        while not x:
            w = input("White to Move: ")
            x = B.move_piece(w, 'w')
        b = input("Black to Move: ")
        y = B.move_piece(b, 'b')
        while not y:
            b = input("Black to Move: ")
            y = B.move_piece(b, 'b')
'''


# while True:
#    root.update_idletasks()
#    root.update()
if __name__ == '__main__':
    main()
