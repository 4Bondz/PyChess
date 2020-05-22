import time


class ChessBoard:
    board = [[]]
    gamestate = 'Normal'  # States include, (Normal) , (W_inCheck) , (B_inCheck) , (W_win) , (B_win)

    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        ChessBoard.setupboard(self)

    def setupboard(self):
        row = 0
        for pawn in range(8):
            self.board[1][pawn] = "wP"
        self.board[row][0] = "wR"
        self.board[row][7] = "wR"
        self.board[row][1] = "wN"
        self.board[row][6] = "wN"
        self.board[row][5] = "wB"
        self.board[row][2] = "wB"
        self.board[row][3] = "wQ"
        self.board[row][4] = "wK"

        row = 7
        for pawn in range(8):
            self.board[6][pawn] = "bP"
        self.board[row][0] = "bR"
        self.board[row][7] = "bR"
        self.board[row][1] = "bN"
        self.board[row][6] = "bN"
        self.board[row][5] = "bB"
        self.board[row][2] = "bB"
        self.board[row][3] = "bQ"
        self.board[row][4] = "bK"

    def validmovecoordinates(self, t1, t2):
        x = t1[0] + t2[0]
        y = t1[1] + t2[1]
        if x < 0 or y < 0 or x > 7 or y > 7:  # Off board
            return None
        elif self.board[x][y] != 0:
            if self.board[t1[0]][t1[1]][0] == self.board[x][y][0]:
                return None
            else:
                return x, y
        else:
            return x, y

    def printraw(self):
        for row in range(8):
            print(row + 1, "| ", end="")
            for column in range(8):
                if self.board[row][column] == 0:
                    print(" 0  ", end="")
                else:
                    print("", self.board[row][column], "", end="")
            print("\n")
        print("  ", end=" ")
        for char in range(65, 73):
            print(" ", chr(char), end=" ")
        print("\n")

    def printboard(self):
        for row in range(8):
            # print("  --------------------------------")
            print(7 - row + 1, "| ", end="")
            for column in range(8):
                if self.board[7 - row][column] == 0:
                    print(" 0  ", end="")
                else:
                    print("", self.board[7 - row][column][1], " ", end="")
            if row == 0:
                print("     <- Black", end="")
            if row == 7:
                print("     <- White", end="")
            print('\n')
        # print("  --------------------------------")
        # print("W")
        print("  ", end=" ")
        for char in range(65, 73):
            print(" ", chr(char), end=" ")
        print("\n")

    def checkmove(self, piece, pieceLocationList, destinationMatrixLocation, player):
        if piece == 'n' or piece == 'N':
            possibleMoveShift = [(2, 1), (2, -1), (-2, 1), (-2, -1), (-1, -2), (-1, 2), (1, 2), (1, -2)]
            piecesThatMove = self.findpieces(destinationMatrixLocation, pieceLocationList, possibleMoveShift)
            if len(piecesThatMove) != 1:
                p = input("What are the coordinates of the piece that moves? ")
                p = self.chesstomatrix(p)
                if p in piecesThatMove:
                    piecesThatMove = [p]
                else:
                    print("Bad Move")
                    return False
            self.setpiece(piecesThatMove[0], destinationMatrixLocation, piece,
                          player)  # TODO: CHANGE piecesThatMove[0] to piecesThatmove -> After you make sure they don't have two possible pieces that move
        elif piece == 'b' or piece == 'B':
            # Bishop
            # Bishops can move diagonally, max (7,7)
            possibleMoveShift = self.bishopCheck(pieceLocationList)
            piecesThatMove = self.findpieces(destinationMatrixLocation, pieceLocationList, possibleMoveShift)
            if len(piecesThatMove) != 1:
                p = input("What are the coordinates of the piece that moves? ")
                p = self.chesstomatrix(p)
                if p in piecesThatMove:
                    piecesThatMove = [p]
                else:
                    print("Bad Move")
                    return False

                pass
            self.setpiece(piecesThatMove[0], destinationMatrixLocation, piece, player)
        elif piece == 'r' or piece == 'R':
            # Rook
            possibleMoveShift = self.rookCheck(pieceLocationList)
            piecesThatMove = self.findpieces(destinationMatrixLocation, pieceLocationList, possibleMoveShift)
            if len(piecesThatMove) != 1:
                p = input("What are the coordinates of the piece that moves? ")
                p = self.chesstomatrix(p)
                if p in piecesThatMove:
                    piecesThatMove = [p]
                else:
                    print("Bad Move")
                    return False
                pass
            self.setpiece(piecesThatMove[0], destinationMatrixLocation, piece, player)
            pass
        elif piece == 'k' or piece == 'K':
            # King TODO write King Code
            possibleMoveShift = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            piecesThatMove = self.findpieces(destinationMatrixLocation, pieceLocationList, possibleMoveShift)
            if len(piecesThatMove) != 1:
                p = input("What are the coordinates of the piece that moves? ")
                p = self.chesstomatrix(p)
                if p in piecesThatMove:
                    piecesThatMove = [p]
                else:
                    print("Bad Move")
                    return False
            self.setpiece(piecesThatMove[0], destinationMatrixLocation, piece, player)
            pass
        elif piece == 'q' or piece == 'Q':
            possibleMoveShift = self.rookCheck(pieceLocationList)
            p2 = self.bishopCheck(pieceLocationList)
            possibleMoveShift.extend(x for x in p2 if x not in possibleMoveShift) # Combine lists into a master list
            piecesThatMove = self.findpieces(destinationMatrixLocation, pieceLocationList, possibleMoveShift)
            if len(piecesThatMove) != 1:
                p = input("What are the coordinates of the piece that moves? ")
                p = self.chesstomatrix(p)
                if p in piecesThatMove:
                    piecesThatMove = [p]
                else:
                    print("Bad Move")
                    return False
                pass
            self.setpiece(piecesThatMove[0], destinationMatrixLocation, piece, player)
            # TODO write Queen Code - uses rook and bishop mode
        elif piece == 'p' or piece == 'P':
            # Add +1 Move
            if player == 'w':
                possibleMoveShift = [(1, 0)]
            else:
                possibleMoveShift = [(-1, 0)]
            # white pawn = 1 : black pawn = 6
            if player == 'w' and (destinationMatrixLocation[0] - 2) == 1:
                possibleMoveShift.append((2, 0))
            elif player == 'b' and (destinationMatrixLocation[0] + 2) == 6:
                possibleMoveShift.append((-2, 0))

            if player == 'w' and destinationMatrixLocation[0] < 7 and 7 > destinationMatrixLocation[1] > 0:
                    if self.board[destinationMatrixLocation[0] + 1][destinationMatrixLocation[1] + 1] != 0 or\
                            self.board[destinationMatrixLocation[0] + 1][destinationMatrixLocation[1] - 1] != 0:
                        possibleMoveShift.append((1, 1))
                        possibleMoveShift.append((1, -1))
            elif player == 'b' and destinationMatrixLocation[0] > 0 and 0 < destinationMatrixLocation[1] < 7:
                    if self.board[destinationMatrixLocation[0] - 1][destinationMatrixLocation[1] - 1] != 0 or\
                            self.board[destinationMatrixLocation[0] - 1][destinationMatrixLocation[1] + 1] != 0:
                        possibleMoveShift.append((-1, -1))
                        possibleMoveShift.append((-1, 1))
            piecesThatMove = self.findpieces(destinationMatrixLocation, pieceLocationList, possibleMoveShift)
            if len(piecesThatMove) != 1:
                return False
            self.setpiece(piecesThatMove[0], destinationMatrixLocation, piece, player)
            # if ( White pawn == starting row or Black pawn == starting row) => Add +2 Move
            # if (Piece @ diagonal) => Add Diagonal Move
        return True

    def checkcheck(self):
        pass

    def move(self, playerTurn, command):
        command: str  # Chess notation that represents the move
        check = 0
        dst = 0
        piece = command[0]

        if 'x' == command[1]:
            dst = command[2] + command[3]
        else:
            dst = command[1] + command[2]

        check = True if command.find("+") != -1 else False


        # Find on the board , all of the locations of the specific piece
        pieceLocations = []
        pieceName = playerTurn + piece.upper()
        for row in range(8):
            for column in range(8):
                if self.board[row][column] == pieceName:
                    pieceLocations.append((row, column))
        if len(pieceLocations) == 0:
            print("Piece Does Not Exist")
            return False
        destinationMatrixLocation = self.chesstomatrix(dst)
        validMove = self.checkmove(piece, pieceLocations, destinationMatrixLocation, playerTurn)
        if not validMove:
            return False
        if check:
            actuallyCheck = self.checkcheck()
            # TODO IMPLEMENT CHECK CHECKER

        # TODO : LIST OF ITEMS BELOW:

        # Update Game State? -> Check , Checkmake , Stalemate
        # Clear Screen , Print Action , Print Board

        pass

    # INTERNAL FUNC
    def chesstomatrix(self, chessLocation):
        cl_lower = chessLocation.lower()
        row = int(ord(cl_lower[0]) - 97)
        column = int(cl_lower[1]) - 1
        # self.board[row][column] = "xN"
        # self.printboard()
        return (column, row)

    def setpiece(self, src, dst, piece, player):
        # TODO : SAY SOMETHING LIKE -> "X TAKES Y ON Z !!! OOOOOOO SHIEEEEETT
        self.board[dst[0]][dst[1]] = player + piece
        self.board[src[0]][src[1]] = 0
        self.printboard()
        #self.printraw()
        print("x")
        pass

    def findpieces(self, destinationMatrixLocation, pieceLocationList, possibleMoveShift):
        pieceThatMoves = []
        for piece in pieceLocationList:
            # For each piece, make the 4 possible move list
            possibleMoves = list(self.validmovecoordinates(piece, shift) for shift in possibleMoveShift)
            for endCoor in possibleMoves:
                if endCoor != None and endCoor == destinationMatrixLocation:
                    if piece not in pieceThatMoves:
                        pieceThatMoves.append(piece)
        return pieceThatMoves

    def bishopCheck(self, pieceLocationList):
        possibleMoveShift = []
        for p in pieceLocationList:
            a = True
            b = True
            c = True
            d = True
            for x in range(1, 8):
                if not a and not b and not c and not d:
                    break
                # 4 quadrants, were going to test each one.
                if a:
                    r = self.validmovecoordinates(p, (x, x))
                    if r == None:  # Bad Move
                        a = False  # Stop checking, any further move will be invalid!
                    else:
                        possibleMoveShift.append((x, x))
                if b:
                    r = self.validmovecoordinates(p, (-x, x))
                    if r == None:
                        b = False
                    else:
                        possibleMoveShift.append((-x, x))
                if c:
                    r = self.validmovecoordinates(p, (-x, -x))
                    if r == None:
                        c = False
                    else:
                        possibleMoveShift.append((-x, -x))
                if d:
                    r = self.validmovecoordinates(p, (x, -x))
                    if r == None:
                        d = False
                    else:
                        possibleMoveShift.append((x, -x))
                if not a and not b and not c and not d:
                    break
        return possibleMoveShift

    def rookCheck(self, pieceLocationList):
        possibleMoveShift = []
        for p in pieceLocationList:
            a = True
            b = True
            c = True
            d = True
            for x in range(1, 8):
                if not a and not b and not c and not d:
                    break
                for y in range(1, 8):
                    # 4 quadrants, were going to test each one.
                    if a:
                        r = self.validmovecoordinates(p, (x, 0))
                        if r == None:  # Bad Move
                            a = False  # Stop checking, any further move will be invalid!
                        else:
                            possibleMoveShift.append((x, 0))
                    if b:
                        r = self.validmovecoordinates(p, (0, y))
                        if r == None:
                            b = False
                        else:
                            possibleMoveShift.append((0, y))
                    if c:
                        r = self.validmovecoordinates(p, (-x, 0))
                        if r == None:
                            c = False
                        else:
                            possibleMoveShift.append((-x, 0))
                    if d:
                        r = self.validmovecoordinates(p, (0, -y))
                        if r == None:
                            d = False
                        else:
                            possibleMoveShift.append((0, -y))
                    if not a and not b and not c and not d:
                        break
        return possibleMoveShift
                # 256 possible moves to test, this can be done better but its fine
    # INTERNAL FUNC


class white:
    pass


class black:
    pass


class game:
    board = ChessBoard()
    player_white = white()
    player_black = black()
    gameState = 0  # 0 = White, 1 = Black
    # GAME STATE: START
    # on init, board is setup

    board.printboard()
    #board.printraw()

    print("White to Go First")
    print("Use Chess Notation + P for Pawns")
    while True:
        move = input("White Move: ").upper()
        ret = board.move('w', move)
        while ret == False:
            move = input("White Move: ").upper()
            ret = board.move('w', move)
        move = input("Black Move: ").upper()
        ret = board.move('b', move)
        while ret == False:
            move = input("Black Move: ").upper()
            ret = board.move('w', move)

