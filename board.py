import piece
class Board():
    def __init__(self):
        self.board = []
        player2Setup = [piece.Rook(True, [0,0])], [piece.Knight(True, [0,1])], [piece.Bishop(True, [0,2])], [piece.Queen(True, [0,3])], [piece.King(True, [0,4])], [piece.Bishop(True, [0,5])], [piece.Knight(True, [0,6])], [piece.Rook(True, [0,7])]
        player1Setup = [piece.Rook(False, [7,0])], [piece.Knight(False, [7,1])], [piece.Bishop(False, [7,2])], [piece.Queen(False, [7,3])], [piece.King(False, [7,4])], [piece.Bishop(False, [7,5])], [piece.Knight(False, [7,6])], [piece.Rook(False, [7,7])]
        for i in range(8):
            if i == 0: #player2
                self.board.append(player2Setup)
            elif i == 1: 
                for j in range(8):
                    self.board.append([piece.Pawn(True, [1, j])])
            elif i == 6: #player1
                for j in range(8):
                    self.board.append([piece.Pawn(False, [6, j])] * 8)
            elif i == 7:
                self.board.append(player1Setup)
            

            


    def drawBoard(self):
       pass