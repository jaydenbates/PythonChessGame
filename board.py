import piece
    # background: f"\u001b[48;2;{r};{g};{b}m" brown = f"\u001b[48;2;165;42;42m", black = f"\u001b[48;2;0;0;0m", white = f"\u001b[38;2;225;225;225m"
BGLIGHTGRAY = '\033[47m'
REMOVECOLOR = "\033[00m"
class Board():
    def __init__(self):
        self.board = [[piece.Rook(True, [0,0]), piece.Knight(True, [0,1]), piece.Bishop(True, [0,2]), piece.Queen(True, [0,3]), piece.King(True, [0,4]), piece.Bishop(True, [0,5]), piece.Knight(True, [0,6]), piece.Rook(True, [0,7])], 
        [piece.Pawn(True, [1, 0]), piece.Pawn(True, [1, 1]), piece.Pawn(True, [1, 2]), piece.Pawn(True, [1, 3]), piece.Pawn(True, [1, 4]), piece.Pawn(True, [1, 5]), piece.Pawn(True, [1, 6]), piece.Pawn(True, [1, 7])], 
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [piece.Pawn(False, [6, 0]), piece.Pawn(False, [6, 1]), piece.Pawn(False, [6, 2]), piece.Pawn(False, [6, 3]), piece.Pawn(False, [6, 4]), piece.Pawn(False, [6, 5]), piece.Pawn(False, [6, 6]), piece.Pawn(False, [6, 7])],
        [piece.Rook(False, [7,0]), piece.Knight(False, [7,1]), piece.Bishop(False, [7,2]), piece.Queen(False, [7,3]), piece.King(False, [7,4]), piece.Bishop(False, [7,5]), piece.Knight(False, [7,6]), piece.Rook(False, [7,7])]]
   
            
    def drawBoard(self):
        # make a string builder
        pieceSportIsBGLIGHTGRAY = False
        stars = "  ****************************************"
        sb = ""
        sb += stars + "\n"
        for i in range(len(self.board)):
            if i == 0:
                sb += str(len(self.board)) + " "
            for j in range(len(self.board[i])):
                if i % 2 == 0:
                    if j % 2 == 1: 
                        sb += BGLIGHTGRAY
                        pieceSportIsBGLIGHTGRAY = True
                elif i % 2 == 1:
                    if j % 2 == 0:
                        sb += BGLIGHTGRAY
                        pieceSportIsBGLIGHTGRAY = True
                if self.board[i][j] == None:
                    if j != len(self.board[i]) - 1:
                        sb += "|   |"
                    else:
                        sb += "|   |"  +  REMOVECOLOR + "\n" + str(len(self.board) - i - 1) + " "
                else:
                    if j != len(self.board[i]) - 1:
                        if pieceSportIsBGLIGHTGRAY:
                            sb += "| " + self.board[i][j].__str__(True) + BGLIGHTGRAY + " |"
                            pieceSportIsBGLIGHTGRAY = False
                        else:
                            sb += "| " + self.board[i][j].__str__(False) + " |"
                    else:
                        if i != len(self.board) - 1:
                            if pieceSportIsBGLIGHTGRAY:
                                sb += "| " + self.board[i][j].__str__(True) + BGLIGHTGRAY +" |" +  REMOVECOLOR + "\n" + str(len(self.board) - i - 1) + " "
                                pieceSportIsBGLIGHTGRAY = False
                            else:
                                sb += "| " + self.board[i][j].__str__(False) + " |" +  REMOVECOLOR + "\n" + str(len(self.board) - i - 1) + " "
                        else:
                            if pieceSportIsBGLIGHTGRAY:
                                sb += "| " + self.board[i][j].__str__(True) + BGLIGHTGRAY + " |" + REMOVECOLOR +  "\n" 
                                pieceSportIsBGLIGHTGRAY = False
                            else:
                                sb += "| " + self.board[i][j].__str__(False) + " |\n"
                pieceSportIsBGLIGHTGRAY = False
                sb += REMOVECOLOR
        sb += stars
        sb += "\n  "
        for i in range(len(self.board)):
            sb += "  " + str(i + 1) + "  "
        print(sb)

