def isClear(pos, move, board):
    x = pos[0] + move[0]
    y = pos[1] + move[1]
    if not 0 <= x <= 7 or not 0 <= y <= 7:
        return False
    else:
        return board[pos[0] + move[0]][pos[1] + move[1]] == 'X'


def occButDif(pos, move, color, board):
    x = pos[0] + move[0]
    y = pos[1] + move[1]
    if not 0 <= x <= 7 or not 0 <= y <= 7:
        return False
    t = board[x][y]
    return t != "X" and t.player != color


class Pawn:
    pos = (0, 0)
    possible_moves = []
    player = ''
    p_id = 'P'

    def __init__(self, x, y, p):
        self.pos = (x, y)
        self.player = p

    def get_possible_moves(self, board):
        self.possible_moves.clear()
        if self.player == 'b':
            DIR = -1
        else:
            DIR = 1
        sshifts = [(DIR, 0)]
        ashifts = [(DIR, -1), (DIR, 1)]
        # A pawn can move 3 ways
        # Standard Move - Always, when space is available
        for move in sshifts:
            if isClear(self.pos, move, board):
                self.possible_moves.append(move)
        for move in ashifts:
            if occButDif(self.pos, move, self.player, board):
                self.possible_moves.append(move)
        if DIR == 1:
            if self.pos[0] == 1 and isClear(self.pos, move, board):
                self.possible_moves.append((2 * DIR, 0))
        else:
            if self.pos[0] == 6 and isClear(self.pos, move, self.player, board):
                self.possible_moves.append((2 * DIR, 0))
        ret = []
        for each in self.possible_moves:
            i = each[0] + self.pos[0]
            j = each[1] + self.pos[1]
            ret.append((i, j))
        self.possible_moves = ret
        return self.possible_moves



class Knight:
    pos = (0, 0)
    possible_moves = []
    player = ''
    p_id = 'N'

    def __init__(self, x, y, p):
        self.pos = (x, y)
        self.player = p

    def get_possible_moves(self, board):
        self.possible_moves.clear()
        sshifts = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
        for move in sshifts:
            if isClear(self.pos, move, board) or occButDif(self.pos, move, self.player, board):
                self.possible_moves.append(move)
        ret = []
        for each in self.possible_moves:
            i = each[0] + self.pos[0]
            j = each[1] + self.pos[1]
            ret.append((i, j))
        self.possible_moves = ret
        return self.possible_moves


class Bishop:
    pos = (0, 0)
    possible_moves = []
    player = ''
    p_id = 'B'

    def __init__(self, x, y, p):
        self.pos = (x, y)
        self.player = p

    def get_possible_moves(self, board):
        OK = [1, 1, 1, 1]
        for l in range(1, 8):
            # TODO - Add in all OK == 0
            M = [(l, l), (l, -l), (-l, l), (-l, -l)]
            for k in range(len(M)):
                if OK[k] and isClear(self.pos, M[k], board):
                    self.possible_moves.append(M[k])
                elif OK[k] and occButDif(self.pos, M[k], self.player, board):
                    self.possible_moves.append(M[k])
                    OK[k] = False
                else:
                    OK[k] = False
        ret = []
        for each in self.possible_moves:
            i = each[0] + self.pos[0]
            j = each[1] + self.pos[1]
            ret.append((i, j))
        self.possible_moves = ret
        return self.possible_moves


class Rook:
    pos = (0, 0)
    possible_moves = []
    player = ''
    p_id = 'R'

    def __init__(self, x, y, p):
        self.pos = (x, y)
        self.player = p

    def get_possible_moves(self, board):
        OK = [1, 1, 1, 1]
        for l in range(1, 8):
            M = [(l, 0), (0, -l), (-l, 0), (0, l)]
            for k in range(len(M)):
                if OK[k] and isClear(self.pos, M[k], board):
                    self.possible_moves.append(M[k])
                elif OK[k] and occButDif(self.pos, M[k], self.player, board):
                    self.possible_moves.append(M[k])
                    OK[k] = False
                else:
                    OK[k] = False
        ret = []
        for each in self.possible_moves:
            i = each[0] + self.pos[0]
            j = each[1] + self.pos[1]
            ret.append((i, j))
        self.possible_moves = ret
        return self.possible_moves


class King:
    pos = (0, 0)
    possible_moves = []
    player = ''
    p_id = 'K'

    def __init__(self, x, y, p):
        self.pos = (x, y)
        self.player = p

    def get_possible_moves(self, board):
        l = 1
        if isClear(self.pos, (l, 0), board) or occButDif(self.pos, (l, 0), self.player, board):
            self.possible_moves.append((l, 0))
        if isClear(self.pos, (-l, 0), board) or occButDif(self.pos, (-l, 0), self.player, board):
            self.possible_moves.append((-l, 0))
        if isClear(self.pos, (0, -l), board) or occButDif(self.pos, (0, -l), self.player, board):
            self.possible_moves.append((0, -l))
        if isClear(self.pos, (0, l), board) or occButDif(self.pos, (0, l), self.player, board):
            self.possible_moves.append((0, l))
        if isClear(self.pos, (l, l), board) or occButDif(self.pos, (l, l), self.player, board):
            self.possible_moves.append((l, l))
        if isClear(self.pos, (-l, l), board) or occButDif(self.pos, (-l, l), self.player, board):
            self.possible_moves.append((-l, l))
        if isClear(self.pos, (l, -l), board) or occButDif(self.pos, (l, -l), self.player, board):
            self.possible_moves.append((l, -l))
        if isClear(self.pos, (-l, -l), board) or occButDif(self.pos, (-l, l), self.player, board):
            self.possible_moves.append((-l, -l))
        ret = []
        for each in self.possible_moves:
            i = each[0] + self.pos[0]
            j = each[1] + self.pos[1]
            ret.append((i, j))
        self.possible_moves = ret
        return self.possible_moves


class Queen:
    pos = (0, 0)
    possible_moves = []
    player = ''
    p_id = 'Q'

    def get_possible_moves(self, board):
        OK = [1, 1, 1, 1, 1, 1, 1, 1]
        for l in range(1, 8):
            M = [(l, l), (l, -l), (-l, l), (-l, -l), (l, 0), (0, -l), (-l, 0), (0, l)]
            for k in range(len(M)):
                if OK[k] and isClear(self.pos, M[k], board):
                    self.possible_moves.append(M[k])
                elif OK[k] and occButDif(self.pos, M[k], self.player, board):
                    self.possible_moves.append(M[k])
                    OK[k] = False
                else:
                    OK[k] = False
        ret = []
        for each in self.possible_moves:
            i = each[0] + self.pos[0]
            j = each[1] + self.pos[1]
            ret.append((i, j))
        self.possible_moves = ret
        return self.possible_moves

    def __init__(self, x, y, p):
        self.pos = (x, y)
        self.player = p


def chess_to_matrix(chessLocation):
    cl_lower = chessLocation.lower()
    row = int(ord(cl_lower[0]) - 97)
    column = int(cl_lower[1]) - 1
    return column, row


class Board:
    chessboard = []

    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.chessboard = []
        for i in range(8):
            self.chessboard.append([])
        row = 0
        for p in range(8):
            self.chessboard[1].append(Pawn(1, p, 'w'))
        self.chessboard[row].append(Rook(row, 0, 'w'))
        self.chessboard[row].append(Knight(row, 1, 'w'))
        self.chessboard[row].append(Bishop(row, 2, 'w'))
        self.chessboard[row].append(Queen(row, 3, 'w'))
        self.chessboard[row].append(King(row, 4, 'w'))
        self.chessboard[row].append(Bishop(row, 5, 'w'))
        self.chessboard[row].append(Knight(row, 6, 'w'))
        self.chessboard[row].append(Rook(row, 7, 'w'))
        row = 7
        for x in range(2, 6):
            for y in range(8):
                self.chessboard[x].append('X')

        for p in range(8):
            self.chessboard[6].append(Pawn(6, p, 'b'))
        self.chessboard[row].append(Rook(row, 0, 'b'))
        self.chessboard[row].append(Knight(row, 1, 'b'))
        self.chessboard[row].append(Bishop(row, 2, 'b'))
        self.chessboard[row].append(King(row, 3, 'b'))
        self.chessboard[row].append(Queen(row, 4, 'b'))
        self.chessboard[row].append(Bishop(row, 5, 'b'))
        self.chessboard[row].append(Knight(row, 6, 'b'))
        self.chessboard[row].append(Rook(row, 7, 'b'))

    def get_all_locations(self, piece, color):
        piece = piece.upper()
        piece_locations = []
        for x in range(8):
            for y in range(8):
                r = self.chessboard[x][y]
                if r != "X" and r.p_id == piece and r.player == color:
                    piece_locations.append(r.pos)
        return piece_locations

    def move_piece(self, move, player):
        # Piece + Location + "+" (if check)
        move.replace("x", "")
        move.replace("X", "")
        move = move.upper()
        possible_movers = []
        if len(move) == 3:
            # Standard Move : piece, newLocation
            P = move[0]
            NL = chess_to_matrix(move[1] + move[2])
            all_pieces_location = self.get_all_locations(P, player)
            for i in all_pieces_location:
                M = self.chessboard[i[0]][i[1]].get_possible_moves(self.chessboard)
                if NL in M:
                    possible_movers.append(i)
            if len(possible_movers) == 0:
                print("BAD MOVE")
                return False
            elif len(possible_movers) != 1:
                # You can either ask, or make them do it again, this will be obsolete when the GUI is implemented
                CL = input("Enter Location of Piece to Move: ").upper()
            else:
                CL = possible_movers[0]
            self.move_to(CL, NL)

        elif len(move) == 5:
            # Disambiguation Move: piece, currentLocation, newLocation
            P = move[0]
            CL = chess_to_matrix(move[1] + move[2])
            NL = chess_to_matrix(move[3] + move[4])
            M = self.chessboard[CL[0]][CL[1]].get_possible_moves(self.chessboard)
            if NL in M:
                self.move_to(CL, NL)
            else:
                print("Bad Move")
                return False

    def move_to(self, CL, NL):
        # CL = current location
        # NC = new location
        self.chessboard[NL[0]][NL[1]] = self.chessboard[CL[0]][CL[1]]
        self.chessboard[CL[0]][CL[1]] = "X"
        self.chessboard[NL[0]][NL[1]].pos = NL[0], NL[1]
        self.chessboard[NL[0]][NL[1]].get_possible_moves(self.chessboard)

        for y in range(0, 8):
            for x in range(0, 8):
                if self.chessboard[y][x] == "X":
                    print("X", end="")
                else:
                    print(self
                          .chessboard[y][x].p_id, end="")
            print("")

        pass







def startgame():
    B = Board()

    while True:
        w = input("White to Move: ")
        B.move_piece(w, 'w')




def main():
    startgame()

    '''
    for y in range(0, 8):
        for x in range(0, 8):
            if B.chessboard[y][x] == "X":
                print("X", end="")
            else:
                print(B.chessboard[y][x].p_id, end="")
        print("")

    print(B.get_all_locations('K', 'w'))
    '''

    print("Done")


if __name__ == "__main__":
    # execute only if run as a script
    main()
