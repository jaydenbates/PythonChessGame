from board import Board
from piece import Queen


class GameState():
    def __init__(self):
        self.board = Board()
        self.turn = True
    
    def promotion(self, upgrade, place):
        if upgrade:
            player = self.board.board[place[0]][place[1]].player
            self.board.board[place[0]][place[1]] = Queen(player, [place[0], place[1]])
        else:
            print("error in promotion")

    def move(self, currentPlace, nextPlace):
        if self.board.board[currentPlace[0]][currentPlace[1]].isMoveValid(self.board.board, currentPlace, nextPlace):
            return True
        else:
            print("This is not a valid move")
            return False

    # am going to check by finding the kings then looking at every direction tell it hits a piece. if that piece can move in the direction then check
    def check(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pass


    # if king moves in any direction if it will still be in check then end game
    def checkMate(self):
        pass